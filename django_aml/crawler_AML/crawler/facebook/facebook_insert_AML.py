import pymysql


class DatabaseConnection:
    def __init__(self):

        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='1234',
                db='AML',
                charset='utf8mb4')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            # print('DB connection completed')

        except Exception as e:
            print('Cannot connect to Database: ', e)

    # INSERT facebook
    def facebook_insert(self, user_id, origin_ph, username, gender, phone_number, birthday, company1, company2, company3,
                        university1, university2, university3, address1, address2, address3, contact1, contact2,
                        contact3, contact4, friends_cnt):
        try:
            insert_command = """INSERT INTO aml_facebookinfo (
                             user_id, origin_ph, username, gender, phone_number, birthday, company1, company2, company3,
                             university1, university2, university3, address1, address2, address3, contact1, contact2, 
                             contact3, contact4, friends_cnt
                             ) VALUES (
                             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
            print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, username, gender, phone_number, birthday,
                                                 company1, company2, company3, university1, university2, university3,
                                                 address1, address2, address3, contact1, contact2, contact3, contact4,
                                                 friends_cnt))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def post_insert(self, user_id, origin_ph, post_text, post_info, post_date):
        try:
            insert_command = """INSERT INTO aml_facebookpost (
                             user_id, origin_ph, post_text, post_info, post_date
                             ) VALUES(
                             %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, post_text, post_info, post_date))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def friends_insert(self, user_id, origin_ph, friends_name, friends_info, friends_id):
        try:
            insert_command = """INSERT INTO aml_facebookfriends (
                             user_id, origin_ph, friends_name, friends_info, friends_id
                             ) VALUES(
                             %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, friends_name, friends_info, friends_id))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)
