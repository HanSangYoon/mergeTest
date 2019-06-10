#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from crawler_AML.crawler.AML_foreign_RM_Institutions.AML_dbConnection import AML_dbConnection

from crawler_AML.crawler.googleSearcher.dbConnection import dbConnection

class FBI_wantedList_cralwer:

    def search(self):
        pageList = ['https://www.fbi.gov/wanted',
                    'https://www.fbi.gov/wanted/fugitives',
                    'https://www.fbi.gov/wanted/terrorism',
                    'https://www.fbi.gov/wanted/kidnap',
                    'https://www.fbi.gov/wanted/seeking-information',
                    # 'https://www.fbi.gov/wanted/parental-kidnappings',
                    'https://www.fbi.gov/wanted/bank-robbers',
                    'https://www.fbi.gov/wanted/ecap',
                    'https://www.fbi.gov/wanted/vicap']

        #pageList = ['https://www.fbi.gov/wanted']

        import os
        import platform
        #print("Os: ", os, ", ", platform.system())
        operationSystem = platform.system()

        if 'Windows' == operationSystem:
            print('Your Operation System is', operationSystem, '-', platform.release())

            suspectName = ''
            suspectCategories = ''
            suspectValues={}


            # 데이터 업데이트 할 때 기존 데이터와의 중복을 피하기 위함. 먼저 데이터를 읽어오는 단계 또는 데이터 insert 시 중복 insert 방지 둘 중 하나 택일하여
            # 구현할 필요성이 있음.
            # reading data part

            # dbcon1 = AML_dbConnection()
            # returnSelectResult = dbcon1.dataSelect_AML_FBI_wantedList()
            #
            # print(returnSelectResult)

            for l in pageList:

                html = requests.get(l).text
                soup = BeautifulSoup(html, 'html.parser')

                totalCnt = soup.find_all('p', {'class':'read-more text-center bottom-total visualClear'})

                for c in totalCnt:
                    print("Count of list: ", int(c.text.split('of ')[1].split(' Results')[0].strip()))
                    suspCnt = int(c.text.split('of ')[1].split(' Results')[0].strip())

                    suspectListCategories = soup.find_all('h3', {'class': 'title'})
                    suspectNameList = soup.find_all('p', {'class': 'name'})
                    suspectTitle = soup.find('h1', {'class': 'documentFirstHeading'})

                    print('suspectNameList:', suspectNameList)

                    for a in suspectNameList:
                        suspectName = a.text.strip()
                        suspectCategories = suspectTitle.text

                        suspectValues[suspectName] = suspectCategories
                        print(suspectName, '-', suspectTitle.text)
                        dbcon2 = AML_dbConnection()
                        dbcon2.dataInsert_AML_FBI_wantedList(suspectName, suspectCategories)

            # dictionary 타입 으로 insert 하는 방법을 생각하고 있었음. 미완성. 퍼포먼스가 증가할 것으로 생각됨.
            # print(suspectName, '-', suspectTitle.text)
            # dbcon2 = AML_dbConnection()
            # dbcon2.dataInsert_AML_FBI_wantedList(suspectName, suspectValues[suspectName])

        elif 'Linux' == operationSystem:

            #curses 라이브러리를 사용해 scroller를 만들 계획임. 미완성. scroll 관련 소스는 scrollTest.py에 있음. 윈도우즈에서는 라이브러리 사용 불가함. 리눅스에서만 사용가능.
            print('Your Operation System is', operationSystem, '-', platform.release())
            for l in pageList:
                html = requests.get(l).text
                soup = BeautifulSoup(html, 'html.parser')

                totalCnt = soup.find_all('p', {'class': 'read-more text-center bottom-total visualClear'})

                for c in totalCnt:
                    print("Count of list: ", int(c.text.split('of ')[1].split(' Results')[0].strip()))
                    suspCnt = int(c.text.split('of ')[1].split(' Results')[0].strip())

                    suspectNameList = soup.find_all('h3', {'class': 'title'})
                    suspectTitle = soup.find('h1', {'class': 'documentFirstHeading'})

                    cnt = 0
                    for a in suspectNameList:
                        suspectName = a.text.strip()

                        cnt += 1
                        print(cnt, '. ', suspectName, '-', suspectTitle.text)


fbiList = FBI_wantedList_cralwer()
fbiList.search()
