#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

from crawler_AML.crawler.googleSearcher.dbConnection import dbConnection

def search(prekeyword):
    print(prekeyword)
    html = requests.get('https://www.google.co.kr/search?q={}&num=100&sourceid=chrome&ie=utf-8'.format(prekeyword)).text
    soup = BeautifulSoup(html, 'html.parser')

    print("=============================================================================================")

    for b in soup.find_all('div', {'class':'g'})[:10]:  #검색 결과 최근 10개만 추출(시간 순서는 검색 결과 출력 순서를 따름.)

        searchedURL = b.find('a', href=True)['href'][7:]
        searchedText1 = b.find('h3').text   #검색 제목만 추출
        searchedText1 = searchedText1.replace(" ...", "").replace("...", "").replace(" ... ", ".").replace(" '", " ").replace("'", "").replace(",", ".")
        #

        if(b.find('span', {'class':'st'}) is not None):
            searchedText2 = b.find('span', {'class':'st'}).text
            searchedText2 = searchedText2.replace(" ...", "").replace("...", "").replace(" ... ", ".").replace(" '", " ").replace("'", "").replace(",", ".")
            print(prekeyword, ', ', searchedURL,  ', ', searchedText1,  ', ', searchedText2)
            dbcon2 = dbConnection()
            dbcon2.dataInsert(prekeyword, searchedURL, searchedText1, searchedText2)

def readWordList(userName):
    dbCon1 = dbConnection()
    hazardWordOfList = dbCon1.dataSelect()

    for lp in range(len(hazardWordOfList)):
        search(userName + ' AND ' + hazardWordOfList[lp])


#readWordList('정원훈')