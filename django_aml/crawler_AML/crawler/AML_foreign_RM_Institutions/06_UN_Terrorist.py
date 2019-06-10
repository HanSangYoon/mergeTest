#!/usr/bin/python
import requests
import json
import pprint
from bs4 import BeautifulSoup
from crawler_AML.crawler.AML_foreign_RM_Institutions.AML_dbConnection import AML_dbConnection

class UN_Terrorist_cralwer:

    def search(self):

        #getPageNumber
        htmlInit = requests.get("https://scsanctions.un.org/en/?keywords=al-qaida#alqaedaind").text
        soupInit = BeautifulSoup(htmlInit, 'html.parser')

        TrList = soupInit.find_all('tr', {'class':'rowtext'})

        for a in TrList:
            print(a.text.strip())
            #print(a.find_all('strong')[1])
            #print(a.find_all('strong')[2])


UN_terror_List = UN_Terrorist_cralwer()
UN_terror_List.search()

