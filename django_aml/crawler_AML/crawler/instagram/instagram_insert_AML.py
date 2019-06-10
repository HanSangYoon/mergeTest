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
    def instagram_insert(self, user_id, origin_ph, page_id, username, intro, homepage, post_cnt,
                         follower_cnt, follow_cnt):
        try:
            insert_command = """INSERT INTO aml_instagraminfo (
                             user_id, origin_ph, page_id, username, intro, homepage, post_cnt, follower_cnt, follow_cnt
                             ) VALUES (
                             %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
            print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, page_id, username, intro, homepage, post_cnt,
                                                 follower_cnt, follow_cnt))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def post_insert(self, user_id, origin_ph, post_text, post_place, post_like, post_view, post_date):
        try:
            insert_command = """INSERT INTO aml_instagrampost (
                             user_id, origin_ph, post_text, post_place, post_like, post_view, post_date
                             ) VALUES(
                             %s, %s, %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, post_text, post_place, post_like, post_view,
                                                 post_date))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def follower_insert(self, user_id, origin_ph, follower_id, follower_name):
        try:
            insert_command = """INSERT INTO aml_instagramfollower (
                             user_id, origin_ph, follower_id, follower_name
                             ) VALUES(
                             %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, follower_id, follower_name))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def follow_insert(self, user_id, origin_ph, follow_id, follow_name):
        try:
            insert_command = """INSERT INTO aml_instagramfollow (
                             user_id, origin_ph, follow_id, follow_name
                             ) VALUES(
                             %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, follow_id, follow_name))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)