#!/usr/bin/python
import requests
import json
import pprint
from bs4 import BeautifulSoup
from crawler_AML.crawler.AML_foreign_RM_Institutions.AML_dbConnection import AML_dbConnection

class Interpol_redList_cralwer:

    def search(self):

        #getPageNumber
        htmlInit = requests.get("https://ws-public.interpol.int/notices/v1/red?resultPerPage=20&page=1").text
        soupInit = BeautifulSoup(htmlInit, 'html.parser')

        dicData = json.loads(str(soupInit))

        '''
        data sample
        [
            {
            'forename': 'WILLIAM BRADFORD JR', 
            'date_of_birth': '1936/08/01', 
            'entity_id': '1976/371', 
            'nationalities': ['US'], 
            'name': 'BISHOP', 
            '_links': {
                        'self': {'href': 'https://ws-public.interpol.int/notices/v1/red/1976-371'}, 
                        'images': {'href': 'https://ws-public.interpol.int/notices/v1/red/1976-371/images'}, 
                        'thumbnail': {'href': 'https://ws-public.interpol.int/notices/v1/red/1976-371/images/59479919'}
                      }
            },
        '''

        totalPageCnt = dicData['total']

        print('totalPageCnt:', int(totalPageCnt/20))
        #for a in range(int(int(totalPageCnt)/20)+1): # 전체 페이지 수
        for a in range(318,348):# 전체 페이지 수
            a += 1  # page1부터 다시
            print('1st Cycle:', a)
            html = requests.get("https://ws-public.interpol.int/notices/v1/red?resultPerPage=20&page=" + str(a)).text
            soup = BeautifulSoup(html, 'html.parser')
            print('cycling 1 to 348: ', a)
            dicData = json.loads(str(soup))

            for b in range(20): #한 페이지당 출력되는 사람의 수 20명
                print('2nd Cycle:', b)
                forename = dicData['_embedded']['notices'][b]['forename']
                name = dicData['_embedded']['notices'][b]['name']
                nationalities = dicData['_embedded']['notices'][b]['nationalities']
                date_of_birth = dicData['_embedded']['notices'][b]['date_of_birth']
                entity_id = dicData['_embedded']['notices'][b]['entity_id']

                if nationalities is None:
                    nationalities = ''
                else:
                    nationalities = ''.join(nationalities)

                for c in range(3):
                    print('3rd Cycle:', c)
                    image_href = dicData['_embedded']['notices'][b]['_links']['images']['href']
                    print('test:', forename, name, nationalities, date_of_birth, entity_id, image_href)

                    # dbinsert
                    dbcon2 = AML_dbConnection()
                    dbcon2.dataInsert_AML_Interpol_wantedList(forename, name, nationalities, date_of_birth, entity_id, image_href)

                    continue

                continue

            continue








interpolList = Interpol_redList_cralwer()
interpolList.search()

