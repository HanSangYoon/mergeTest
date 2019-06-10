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
    def gmail_insert(self, user_id, origin_ph, mail_cnt):
        try:
            insert_command = """INSERT INTO aml_gmailinfo (
                             user_id, origin_ph, mail_cnt
                             ) VALUES (
                             %s, %s, %s)
                            """
            print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, mail_cnt))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def list_insert(self, user_id, origin_ph, gmail_sender, gmail_sender_email, gmail_title, gmail_contents, gmail_date):
        try:
            insert_command = """INSERT INTO aml_gmaillist (
                             user_id, origin_ph, gmail_sender, gmail_sender_email, gmail_title, gmail_contents, gmail_date
                             ) VALUES(
                             %s, %s, %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, gmail_sender, gmail_sender_email, gmail_title,
                                                 gmail_contents, gmail_date))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    # def sender_insert(self, user_id, origin_ph, gamil_sender, send_cnt):
    #     try:
    #         insert_command = """INSERT INTO gamil_sender (
    #                          user_id, origin_ph, gamil_sender, send_cnt
    #                          ) VALUES(
    #                          %s, %s, %s, %s)
    #                         """
    #         # print('insert ok', insert_command)
    #         self.cursor.execute(insert_command, (user_id, origin_ph, gamil_sender, send_cnt))
    #         self.connection.commit()
    #         self.connection.close()
    #
    #     except Exception as e:
    #         print('db 에러', e)
