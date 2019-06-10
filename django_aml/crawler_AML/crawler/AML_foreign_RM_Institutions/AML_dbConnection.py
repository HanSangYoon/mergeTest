#!/usr/bin/python
import pymysql

class AML_dbConnection():
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


    #FBI
    def dataSelect_AML_FBI_wantedList(self):
        try:
            sql_insert_query = """SELECT word FROM AML_FBI_wantedList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_FBI_wantedList table")

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

    # dataInsert(keyword, searchedURL, searchedText1, searchedText2)
    def dataInsert_AML_FBI_wantedList(self, unit1, unit2):
        try:
            sql_insert_query = """INSERT INTO AML_FBI_wantedList(suspectName, suspectCategories) VALUES ('""" + unit1 +"""', '""" + unit2 + """');"""

            print(sql_insert_query)
            self.cursor.execute(sql_insert_query)

            print("Record inserted successfully into AML_FBI_wantedList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            return "insertion success"

        except Exception as e:
            self.connection.rollback() #rollback if any exception occured
            print("Failed inserting record into AML_FBI_wantedList table.", e)

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            return "insertion fail"


    #Interpol
    def dataSelect_AML_Interpol_wantedList(self):
        try:
            sql_insert_query = """SELECT word FROM AML_Interpol_wantedList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_Interpol_wantedList table")

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

    # dataInsert(keyword, searchedURL, searchedText1, searchedText2)
    def dataInsert_AML_Interpol_wantedList(self, unit1, unit2, unit3, unit4, unit5, unit6):
        try:
            sql_insert_query = """INSERT INTO AML_Interpol_wantedList(
                                        wanted_foreName, wanted_name, wanted_nationalities, wanted_date_of_birth, wanted_entity_id, wanted_image_href) 
                                  VALUES ('""" + unit1 +"""', '""" + unit2 + """', '""" + unit3 + """', '""" + unit4 + """', '""" + unit5 + """', '""" + unit6 + """');"""

            print(sql_insert_query)
            self.cursor.execute(sql_insert_query)

            print("Record inserted successfully into AML_Interpol_wantedList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            return "insertion success"

        except Exception as e:
            self.connection.rollback() #rollback if any exception occured
            print("Failed inserting record into AML_Interpol_wantedList table.", e)

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            return "insertion fail"



# dbcon = AML_dbConnection()
# dbcon.dataInsert()