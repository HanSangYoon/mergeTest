# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AML.models import FacebookInfo, FacebookPost, FacebookFriends
import logging.handlers
import time
import json
import re


hereWork = str('Facebook')
now = datetime.now()
currentTime = '%s_%s_%s' % (now.year, now.month, now.day)

# logger 인스턴스를 생성 및 로그 레벨 설정
logger = logging.getLogger(hereWork + '_logging')
logger.setLevel(logging.DEBUG)

# formatter 생성
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

# fileHandler 와 StreamHandler 를 생성
file_max_bytes = 10 * 1024 * 1024  # log file size : 10MB

fileHandler = logging.handlers.RotatingFileHandler(
    'C://Users/micro/DevelopCode_1905/django_aml/crawler_AML/crawler/log/' + hereWork + '_log_'
    + currentTime, maxBytes=file_max_bytes, backupCount=10)

streamHandler = logging.StreamHandler()

# handler 에 formatter 세팅
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# Handler 를 logging 에 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# logging
logging.debug(hereWork + '_crawler_bot_debugging on' + currentTime)
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')


def start(origin_ph, user_id, user_pw):
    start_time_all = time.time()

    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    mobile_emulation = {"deviceName": "iPhone 8 Plus"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    url = 'https://m.facebook.com'
    path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    drivers = webdriver.Chrome(options=options, executable_path=path)
    drivers.get(url)
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.other-links")))
    try:
        drivers.find_element_by_name('email').send_keys(user_id)
        time.sleep(1)
        drivers.find_element_by_name('pass').send_keys(user_pw)
        drivers.find_element_by_name('login').click()
        WebDriverWait(drivers, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#rootcontainer")))
    except Exception as e:
        WebDriverWait(drivers, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._5yd0")))
        error = drivers.find_element_by_css_selector('div._5yd0').text
        if error != '':
            print('비밀번호 또는 아이디 오류')
            drivers.close()
            return error,
        else:
            print('로그인 창 변경')
            try:
                WebDriverWait(drivers, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._2pie")))
                drivers.find_element_by_css_selector('div._2pie > div:nth-of-type(1) > button').click()
                time.sleep(2)
                drivers.find_element_by_name('pass').send_keys(user_pw)
                drivers.find_element_by_css_selector('div._2pie > div:nth-of-type(2) > button').click()
                WebDriverWait(drivers, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#rootcontainer")))
            except Exception as e:
                WebDriverWait(drivers, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._5yd0")))
                error = drivers.find_element_by_css_selector('div._5yd0').text
                return error,
    result_dict = facebook_crawler_start(drivers, user_id, origin_ph)
    print('데이터 기반 크롤링 총 구동 시간 :', time.time() - start_time_all)
    print()
    return result_dict


def facebook_crawler_start(drivers, user, origin_ph):
    result_dict = dict()
    result_dict['이름'] = ''
    result_dict['성별'] = ''
    result_dict['휴대폰'] = ''
    result_dict['생일'] = ''
    result_dict['거주했던장소1'] = ''
    result_dict['거주했던장소2'] = ''
    result_dict['거주했던장소3'] = ''
    result_dict['거주했던장소4'] = ''
    result_dict['직장1'] = ''
    result_dict['직장2'] = ''
    result_dict['직장3'] = ''
    result_dict['직장4'] = ''
    result_dict['학력1'] = ''
    result_dict['학력2'] = ''
    result_dict['학력3'] = ''
    result_dict['학력4'] = ''
    result_dict['학력5'] = ''
    result_dict['Instagram'] = ''
    result_dict['YouTube'] = ''
    result_dict['Twitter'] = ''
    result_dict['웹사이트'] = ''
    result_dict['친구수'] = '0'
    result_dict['profile_img'] = ''
    result_dict['page_id'] = ''

    friends_list = list()
    ############################################################################################################

    # 자기 타임라인
    drivers.get('https://m.facebook.com/')
    WebDriverWait(drivers, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

    drivers.find_element_by_css_selector('div#mJewelNav > div:nth-of-type(6)').click()
    WebDriverWait(drivers, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul > li:nth-of-type(1)")))

    drivers.find_element_by_css_selector('ul > li:nth-of-type(1)').click()
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

    # page_id 가져오기
    info = drivers.find_element_by_css_selector('._55st:nth-of-type(1)').get_attribute('data-store')
    page_id = str(json.loads(info)['hq-profile-logging']['profile_id'])

    # 프로필 정보
    drivers.get('https://m.facebook.com/profile.php?v=info&id=' + page_id)

    WebDriverWait(drivers, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#static_templates")))
    html_soup = auto_scroll2(drivers)

    # 이름
    try:
        name = html_soup.select('title')[0].text
        result_dict['이름'] = name
    except Exception as e:
        pass

    # 직장
    try:
        work_list = html_soup.select('#work > div > div')
        for i in range(len(work_list)):
            work = html_soup.select('#work > div > div:nth-of-type(' + str(i+1) + ')')[0].text
            result_dict['직장'+str(i+1)] = work
    except Exception as e:
        pass

    # 학력
    try:
        edu_list = html_soup.select('#education > div > div')
        for i in range(len(edu_list)):
            edu = html_soup.select('#education > div > div:nth-of-type(' + str(i+1) + ')')[0].text
            result_dict['학력' + str(i + 1)] = edu
    except Exception as e:
        pass

    # 거주했던 장소
    try:
        living_list = html_soup.select('#living > div > div')
        for i in range(len(living_list)):
            living = html_soup.select('#living > div > div:nth-of-type(' + str(i+1) + ')')[0].text
            result_dict['거주했던장소' + str(i + 1)] = living
    except Exception as e:
        pass

    # 연락처 정보 (웹사이트, instagram)
    try:
        contact_info_list = html_soup.select('#contact-info > div > div')
        for i in range(len(contact_info_list)):
            contact_info = html_soup.select('#contact-info > div > div:nth-of-type('
                                            + str(i+1) + ') > div > div:nth-of-type(1)')[0].text
            contact_info_title = html_soup.select('#contact-info > div > div:nth-of-type('
                                                  + str(i + 1) + ') > div > div:nth-of-type(2)')[0].text
            result_dict[contact_info_title] = contact_info
    except Exception as e:
        pass

    # 기본 정보 (생일, 성별)
    try:
        basic_info_list = html_soup.select('#basic-info > div > div')
        for i in range(len(basic_info_list)):
            basic_info = html_soup.select('#basic-info > div > div:nth-of-type('
                                          + str(i+1) + ') > div > div:nth-of-type(1)')[0].text
            basic_info_title = html_soup.select('#basic-info > div > div:nth-of-type('
                                                + str(i + 1) + ') > div > div:nth-of-type(2)')[0].text
            result_dict[basic_info_title] = basic_info
    except Exception as e:
        pass



    # if 친구리스트 ~ 타임라인
    if '콘텐츠를 찾을 수 없음' != result_dict['이름']:
        drivers.get('https://m.facebook.com/profile.php?v=friends&id=' + page_id)

        WebDriverWait(drivers, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#static_templates")))
        html_soup = auto_scroll2(drivers)


        friends_ = html_soup.select('#root > div > div > div > div')[0].text
        if friends_ != '친구 없음':
            result_dict['친구수'] = html_soup.select(
                '#root > div > div.item._cs2.acw > a > div > div._4mo.c > div._4mp > span'
            )[0].text.replace('친구 ', '').replace('명', '')
            print('[ 친구수 ]')
            print(result_dict['친구수'])
            friends = html_soup.findAll('div', {'class': '_5pxa'})
            for i in range(len(friends)):
                friends_dict = dict()
                friends_dict['name'] = ''
                friends_dict['page_id'] = ''
                try:
                    friend_name = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                        'h3', {'class': '_5pxc'}).text
                except Exception as e:
                    friend_name = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                        'h1', {'class': '_5pxc'}).text

                try:
                    friend_info = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                        'div', {'class': 'ellipsis'}).text
                except Exception as e:
                    friend_info = ''

                try:
                    friend_href = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                        'h3', {'class': '_5pxc'}).find('a')['href']
                except Exception as e:
                    try:
                        friend_href = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                            'h1', {'class': '_5pxc'}).find('a')['href']
                    except Exception as e:
                        friend_href = ''

                friends_dict['name'] = friend_name
                friends_dict['page_id'] = 'https://www.facebook.com'+friend_href
                friends_list.append(friends_dict)
                # django db insert
                FacebookFriends(
                    user_id=user,
                    origin_ph=origin_ph,
                    friends_name=friend_name,
                    friends_info=friend_info,
                    friends_id='https://www.facebook.com'+friend_href
                ).save()

        else:
            pass

        ############################################################################################################
        # 타임라인
        drivers.get('https://m.facebook.com/' + page_id)
        html_soup = auto_scroll2(drivers)

        profile_img = html_soup.select('i.profpic')[0]['style']
        p_re = re.compile('\'[^)]*')
        result_dict['profile_img'] = p_re.findall(profile_img)[0].replace(r'\3a ', ':').replace(r'\3d ', '=').replace(r'\26 ', '&').replace("'", '')
        result_dict['page_id'] = 'https://www.facebook.com/' + page_id

        section = html_soup.select('section.storyStream')
        for i in section:
            article_list = html_soup.select('section#' + i['id'] + ' > article')
            for j in range(len(article_list)):
                try:
                    post_text = ''

                    # 날짜
                    post_date = html_soup.select('section#' + i['id'] + ' > article:nth-of-type('
                                                 + str(j+1) + ') > div > header > div:nth-of-type(2) > div > div > '
                                                              'div:nth-of-type(1) > div > a > abbr')[0].text
                    if '시간' in post_date or '분' in post_date:
                        post_date = '%s-%s-%s' % (now.year, now.month, now.day)
                    elif '어제' in post_date:
                        post_date = '%s-%s-%s' % (now.year, now.month, (now.day-1))
                    elif '오후' not in post_date and '오전' not in post_date:
                        post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace(' ', '')
                        post_date = datetime.strptime(post_date, '%Y-%m-%d')
                    elif '년' in post_date:
                        post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace('오전', 'AM').\
                            replace('오후', 'PM').replace(' ', '')
                        post_date = datetime.strptime(post_date, '%Y-%m-%d%p%I:%M')
                        post_date = post_date.strftime('%Y-%m-%d')
                    else:
                        post_date = str(now.year) + '년 ' + post_date
                        post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace('오전', 'AM').\
                            replace('오후', 'PM').replace(' ', '')
                        post_date = datetime.strptime(post_date, '%Y-%m-%d%p%I:%M')
                        post_date = post_date.strftime('%Y-%m-%d')
                    # 텍스트
                    try:
                        post_text = html_soup.select('section#' + i['id'] + ' > article:nth-of-type('
                                                     + str(j+1) + ') > div > div')[0].text
                    except Exception as e:
                        pass

                    # 장소추가
                    try:
                        post_info = html_soup.select('section#' + i['id'] + ' > article:nth-of-type('
                                                     + str(j+1) + ') > div > header > div:nth-of-type(2) > div > '
                                                                  'div > div:nth-of-type(1) > h3')[0].text
                    except Exception as e:
                        post_info = ''

                    # django db insert
                    FacebookPost(
                        user_id=user,
                        origin_ph=origin_ph,
                        post_text=post_text,
                        post_info=post_info,
                        post_date=post_date
                    ).save()

                except Exception as e:
                    pass
    else:
        pass
    ajax_dict = dict()
    if result_dict['이름'] != '':
        ajax_dict['name'] = result_dict['이름']
    if result_dict['생일'] != '':
        ajax_dict['birthday'] = result_dict['생일']
    if result_dict['거주했던장소2'] != '':
        ajax_dict['address'] = result_dict['거주했던장소2']
    if result_dict['학력3'] != '':
        ajax_dict['school'] = result_dict['학력3']
    if result_dict['직장2'] != '':
        ajax_dict['office'] = result_dict['직장2']
    if result_dict['친구수'] != '':
        ajax_dict['friends'] = result_dict['친구수']
    if result_dict['page_id'] != '':
        ajax_dict['facebook-url'] = result_dict['page_id']
    print(result_dict)
    # django db insert
    try:
        FacebookInfo(
            user_id=user,
            origin_ph=origin_ph,
            page_id=str(result_dict['page_id']),
            username=str(result_dict['이름']),
            gender=str(result_dict['성별']),
            phone_number=str(result_dict['휴대폰']),
            birthday=str(result_dict['생일']),
            company1=str(result_dict['직장2']),
            company2=str(result_dict['직장3']),
            company3=str(result_dict['직장4']),
            university1=str(result_dict['학력3']),
            university2=str(result_dict['학력4']),
            university3=str(result_dict['학력5']),
            address1=str(result_dict['거주했던장소2']),
            address2=str(result_dict['거주했던장소3']),
            address3=str(result_dict['거주했던장소4']),
            contact1=str(result_dict['Instagram']),
            contact2=str(result_dict['YouTube']),
            contact3=str(result_dict['Twitter']),
            contact4=str(result_dict['웹사이트']),
            friends_cnt=int(result_dict['친구수']),
        ).save()
    except Exception as e_maria:
        logger.error('[ Error ] MariaDB About information Insertion => {}'.format(e_maria))
    drivers.close()
    return ajax_dict, friends_list, result_dict['profile_img']


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
