# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from crawler_AML.crawler.gmail import gmail_insert_AML
from AML.models import GmailInfo, GmailList
import logging.handlers
import time


hereWork = str('Gmail')
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
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

    url = 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CwaK9")))

    driver.find_element_by_id('identifierId').send_keys(user_id)
    driver.find_element_by_css_selector('.CwaK9').click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CwaK9")))

    try:
        driver.find_element_by_name('password').send_keys(user_pw)
    except Exception as e:
        error = driver.find_element_by_css_selector('.GQ8Pzc').text
        return error,

    driver.find_element_by_css_selector('.CwaK9').click()

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x7WrMb")))
    except Exception as e:
        error1 = driver.find_element_by_css_selector('.GQ8Pzc').text
        if error1 != '':
            return error1,
        else:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#captchaimg")))
            error2 = driver.find_element_by_css_selector('.T8zd8e').text
            return '보안문제',

    start_time_all = time.time()

    gmail = gmail_crawler_start(driver, user_id, origin_ph)

    print('데이터 기반 크롤링 총 구동 시간 :', time.time() - start_time_all)
    return gmail


def gmail_crawler_start(driver, user, origin_ph):
    # 메일
    driver.get('https://mail.google.com/mail/')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".aeJ")))

    past_date = datetime.now() - timedelta(weeks=13)
    past_date = past_date.strftime('%Y-%m-%d')

    gmail_list = list()
    mail_cnt = 0
    while True:
        html = driver.page_source
        html_soup = BeautifulSoup(html, 'html.parser')
        mail_list = html_soup.select('div.BltHke > div.UI tbody > tr')
        mail_cnt += len(mail_list)
        for i in range(len(mail_list)):
            mail_sender = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                           + str(i+1) + ') > td.yX > div.yW > span.bA4')[0].text
            mail_sender_email = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                           + str(i+1) + ') > td.yX > div.yW > span.bA4 > span')[0]['email']
            try:
                mail_title = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                              + str(i + 1) + ') > td.a4W > div.xS > div.xT > div.y6')[0].text
            except Exception:
                mail_title = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                              + str(i + 1) + ') > td.a4W > div.a4X > div.xS > div.xT > div.y6')[0].text
            try:
                mail_contents = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                                 + str(i + 1) + ') > td.a4W > div.xS > div.xT > span')[0].text
            except Exception:
                mail_contents = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                               + str(i + 1) + ') > td.a4W > div.a4X > div.xS > div.xT > span')[0].text
            mail_date = html_soup.select('div.BltHke > div.UI tbody > tr:nth-of-type('
                                           + str(i + 1) + ') > td.xW > span')[0]['title'].split(' (')[0]

            mail_date = mail_date.replace('년 ', '-').replace('월 ', '-').replace("일", '')
            mail_date = datetime.strptime(mail_date, '%Y-%m-%d')
            mail_date = mail_date.strftime('%Y-%m-%d')

            mail_dict = dict()
            if mail_sender != '':
                mail_dict['sender'] = mail_sender
            if mail_sender_email != '':
                mail_dict['mail_sender_email'] = mail_sender_email
            if mail_title != '':
                mail_dict['mail_title'] = mail_title
            if mail_contents != '':
                mail_dict['mail_contents'] = mail_contents
            if mail_date != '':
                mail_dict['mail_date'] = mail_date
            gmail_list.append(mail_dict)

            # django db insert
            GmailList(
                user_id=user,
                origin_ph=origin_ph,
                gmail_sender=mail_sender,
                gmail_sender_email=mail_sender_email,
                gmail_title=mail_title,
                gmail_contents=mail_contents,
                gmail_date=mail_date
            ).save()

        if mail_date > past_date:
            driver.find_element_by_css_selector('span.Di > div.T-I-Js-Gs').click()
            time.sleep(1.5)
        else:
            break
    # django db insert
    print(gmail_list)
    GmailInfo(
        user_id=user,
        origin_ph=origin_ph,
        mail_cnt=mail_cnt
    ).save()

    gmail_dict = dict()
    gmail_dict['user'] = user
    gmail_dict['mail_cnt'] = mail_cnt

    driver.close()

    return gmail_dict, gmail_list
