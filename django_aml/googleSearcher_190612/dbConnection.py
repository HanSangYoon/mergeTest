#!/usr/bin/python
import pymysql

class dbConnection():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='uml.kr', port=3366,
                                              user='aster_dba', password='!aster716811',
                                              db='aster', charset='utf8')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print('DB connection completed')
        except Exception as e:
            print('Cannot connect to Database', e)

    def dataSelect(self):
        try:
            sql_insert_query = """SELECT word FROM googleSearch_hazardWordList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into googleSearch_hazardWordList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultlist = []

            for b in a:
                result = ''.join(b)
                resultlist.append(result.replace('\ufeff', '').replace('\r',''))
                #print(''.join(b) +',' + str(testCnt)) # join 한 값이 찍히지 않음.

            return resultlist

        except BaseException as e:
            print('data selection occured exception', e)
            return None

    #.dataInsert(keyword, searchedURL, searchedText1, searchedText2)
    def dataInsert(self, keyword, url, title, content):
        try:
            sql_insert_query = """INSERT INTO googleSearch_users(keyword, searchedURL, searchedTitle, searchedText) VALUES ('""" + keyword +"""', '""" + url + """', '""" + title + """', '""" + content + """');"""

            print(sql_insert_query)
            self.cursor.execute(sql_insert_query)

            print("Record inserted successfully into googleSearch_users table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

        except Exception as e:
            self.connection.rollback() #rollback if any exception occured
            print("Failed inserting record into googleSearch_users table.", e)

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

# dbcon = dbConnection()
# dbcon.dataInsert()