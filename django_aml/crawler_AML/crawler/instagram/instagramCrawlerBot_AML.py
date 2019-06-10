# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from crawler_AML.crawler.instagram import instagram_insert_AML
from AML.models import InstagramInfo, InstagramPost, InstagramFollower, InstagramFollow
import logging.handlers
import time


hereWork = 'Instagram'

currentTime = str(time.localtime().tm_year) + '_' + str(time.localtime().tm_mon) + '_' + str(
    time.localtime().tm_mday) + '_' + str(time.localtime().tm_hour)

logger = logging.getLogger(hereWork+'_logging')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

file_max_bytes = 10*1024*1024

fileHandler = logging.handlers.RotatingFileHandler(
    'C://Users/micro/DevelopCode_1905/django_aml/crawler_AML/crawler/log/' + hereWork + '_log_'
    + currentTime, maxBytes=file_max_bytes, backupCount=10)

streamHandler = logging.StreamHandler()

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

logger.addHandler(fileHandler)


def start(origin_ph, user_id, user_pw):
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    mobile_emulation = {"deviceName": "iPhone 8 Plus"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=path)

    driver.get('https://www.instagram.com/accounts/login/')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "password")))
    driver.find_element_by_name('username').send_keys(user_id)
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_class_name('HmktE').submit()

    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._8qite")))
    except Exception as e:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "article._8Rm4L ")))
        except Exception as e:
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".piCib ")))
                # 비밀번호 오류
                data = driver.find_element_by_css_selector('._08v79').text
                driver.close()
                return data,
            except Exception as e:
                try:
                    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#slfErrorAlert ")))
                    data = driver.find_element_by_css_selector('#slfErrorAlert').text
                    # 아이디 오류
                    driver.close()
                    return data,
                except Exception as e:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".O4QwN")))
                    driver.close()
                    return '보안문제',
    start_time_all = time.time()
    driver.get('https://www.instagram.com/')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.piCib")))

    driver.find_element_by_css_selector('div.mt3GC > button:nth-of-type(2)').click()
    driver.find_element_by_css_selector('div.BvyAW > div:nth-of-type(5) > a').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fx7hk")))

    i_data = instagram_crawler_start(driver, user_id, origin_ph)

    return i_data


def instagram_crawler_start(driver, user_id, origin_ph):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    page_id = soup.select("header.HVbuG h1")[0].text

    try:
        # 이름
        username = soup.select("div.-vDIg > h1")[0].text
    except Exception as e:
        username = ''

    try:
        # 소개
        intro = soup.select("div.-vDIg > span")[0].text
    except Exception as e:
        intro = ''

    try:
        # 홈페이지
        homepage = soup.select("div.-vDIg > a.yLUwa")[0].text
    except Exception as e:
        homepage = ''
    # 게시물 수
    post_cnt = int(soup.select("li:nth-of-type(1) > span > span")[0].text.replace(',', ''))
    # 팔로워 수
    follower_cnt = int(soup.select("li:nth-of-type(2) > a > span")[0]['title'].replace(',', ''))
    # 팔로우 수
    follow_cnt = int(soup.select("li:nth-of-type(3) > a > span")[0].text.replace(',', ''))

    profile_img = soup.select('img.be6sR')[0]['src']

    print("page_id : " + page_id)
    print("이름 : " + username)
    print("소개 : " + intro)
    print("홈페이지 : " + homepage)
    print("게시물 수 :", post_cnt)
    print("팔로워 : ", follower_cnt)
    print("팔로우 : ", follow_cnt)
    print()

    insta_dict = dict()
    if username != '':
        insta_dict['name'] = username
    if intro != '':
        insta_dict['intro'] = intro
    if homepage != '':
        insta_dict['homepage'] = homepage
    if post_cnt > 0:
        insta_dict['post_cnt'] = post_cnt
    if follower_cnt > 0:
        insta_dict['follower_cnt'] = follower_cnt
    if follow_cnt > 0:
        insta_dict['follow_cnt'] = follow_cnt
    if page_id != '':
        insta_dict['page_id'] = page_id


    # 인스타그램 기본정보 insert
    InstagramInfo(
        user_id=user_id,
        origin_ph=origin_ph,
        page_id=page_id,
        username=username,
        intro=intro,
        homepage=homepage,
        post_cnt=post_cnt,
        follower_cnt=follower_cnt,
        follow_cnt=follow_cnt
    ).save()

    # 스크롤내리는 횟수
    scroll_count = 3
    # 중복 href 카운트
    same_count = 0
    # 게시물마다 href 를 담을 리스트
    href = []

    for i in range(0, scroll_count):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        href_html = soup.select('div > div > div.v1Nh3 > a')
        for href_list in href_html:
            if href_list['href'] in href:
                same_count += 1
            else:
                href.append(href_list['href'])
        time.sleep(1)
        print("Scrolling... "+str(i+1)+"/"+str(scroll_count) + ", 현재: " + str(len(href)) + ", 중복: " + str(same_count))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(str(len(href)) + "개의 결과를 찾았습니다.")

    # 팔로워 리스트
    time.sleep(1)
    driver.find_element_by_css_selector("html").send_keys(Keys.HOME)
    time.sleep(1)
    driver.find_element_by_css_selector("li:nth-of-type(2) > a").click()
    time.sleep(1)
    soup = auto_scroll2(driver)

    following_list = list()
    follower_list = soup.select('ul > div > li')
    print('follower cnt :', len(follower_list))
    for i in range(len(follower_list)):
        try:
            follower_id = soup.select('ul > div > li:nth-of-type(' + str(i+1) + ') div.enpQJ > div.d7ByH')[0].text
        except Exception as e:
            try:
                follower_id = soup.select('ul > div > li:nth-of-type(' + str(i + 1) + ') > div > div:nth-of-type(2) a')[0].text
            except Exception as e:
                follower_id = ''
        try:
            follower_name = soup.select('ul > div > li:nth-of-type(' + str(i+1) + ') div.enpQJ > div.wFPL8')[0].text
        except Exception as e:
            try:
                follower_name = soup.select('ul > div > li:nth-of-type('
                                            + str(i + 1) + ') > div > div:nth-of-type(2) > div:nth-of-type(2)')[0].text
            except Exception as e:
                follower_name = ''


        # django db insert
        InstagramFollower(
            user_id=user_id,
            origin_ph=origin_ph,
            follower_id=follower_id,
            follower_name=follower_name
        ).save()

    # 팔로우 리스트
    driver.get('https://www.instagram.com/' + page_id)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fx7hk")))
    time.sleep(1)
    driver.find_element_by_css_selector("html").send_keys(Keys.HOME)
    time.sleep(1)
    driver.find_element_by_css_selector("li:nth-of-type(3) > a").click()
    time.sleep(1)
    soup = auto_scroll2(driver)



    follow_list = soup.select('ul > div > li')
    print('follow_cnt :', len(follow_list))
    for i in range(len(follow_list)):
        try:
            follow_id = soup.select('ul > div > li:nth-of-type(' + str(i+1) + ') div.enpQJ > div.d7ByH')[0].text
        except Exception as e:
            try:
                follow_id = soup.select('ul > div > li:nth-of-type(' + str(i + 1) + ') > div > div:nth-of-type(2) a')[0].text
            except Exception as e:
                follow_id = ''
        try:
            follow_name = soup.select('ul > div > li:nth-of-type(' + str(i+1) + ') div.enpQJ > div.wFPL8')[0].text
        except Exception as e:
            try:
                follow_name = soup.select('ul > div > li:nth-of-type('
                                          + str(i + 1) + ') > div > div:nth-of-type(2) > div:nth-of-type(2)')[0].text
            except Exception as e:
                follow_name = ''

        following_dict = dict()
        following_dict['name'] = follow_name
        following_dict['id'] = follow_id
        following_list.append(following_dict)

        # django db insert
        InstagramFollow(
            user_id=user_id,
            origin_ph=origin_ph,
            follow_id=follow_id,
            follow_name=follow_name
        ).save()

    if 0 < len(href):
        for i in href:
            # 게시글
            user_url = "https://www.instagram.com" + i
            driver.get(user_url)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.c-Yi7")))

            source2 = driver.page_source
            soup = BeautifulSoup(source2, 'html.parser')

            # 올린 날짜
            post_date = soup.select('div.eo2As > div.k_Q0X.NnvRN > a > time')
            for a in post_date:
                post_date = a['title']

            post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace('오전', 'AM'). \
                replace('오후', 'PM').replace(' ', '')

            try:
                # 장소추가
                post_place = soup.select('div.o-MQd > div.M30cS a')[0].text
            except Exception as e:
                post_place = ''

            try:
                # 본문
                post_text = soup.select('div.KlCQn.EtaWk > ul > li:nth-of-type(1) > div > div > div > span')[0].text
            except Exception as e:
                post_text = ''

            try:
                # 좋아요 or 조회수
                like = int(soup.select('section.EDfFK.ygqzn div.Nm9Fw span')[0].text.replace(',', ''))
                view = 0
            except Exception as e:
                view = int(soup.select('section.EDfFK.ygqzn div.HbPOm > span > span')[0].text.replace(',', ''))
                like = 0

            # django db insert
            InstagramPost(
                user_id=user_id,
                origin_ph=origin_ph,
                post_text=post_text,
                post_place=post_place,
                post_like=like,
                post_view=view,
                post_date=post_date
            ).save()

    else:
        print('게시물 없음')
    driver.close()

    return insta_dict, following_list, profile_img


def auto_scroll2(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    for cyc in range(0, 2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
    auto_scroll_data = driver.page_source
    auto_scroll_data_soup_html = BeautifulSoup(auto_scroll_data, 'html.parser')

    return auto_scroll_data_soup_html

# if __name__ == '__main__':
#
#     insta_user_id = 'hj.vw'
#     insta_user_pw = '4109121z#!'
#     start(1,insta_user_id,insta_user_pw)