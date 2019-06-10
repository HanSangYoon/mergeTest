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
    def twitter_insert(self, user_id, origin_ph, username, page_id, tweet_cnt, following_cnt, follower_cnt, joined_date):
        try:
            insert_command = """INSERT INTO aml_twitterinfo (
                             user_id, origin_ph, username, page_id, tweet_cnt, following_cnt, follower_cnt, joined_date
                             ) VALUES (
                             %s, %s, %s, %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, username, page_id, tweet_cnt, following_cnt,
                                                 follower_cnt, joined_date))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def tweet_insert(self, user_id, origin_ph, tweet_name, tweet_page_id, tweet_text, tweet_date):
        try:
            insert_command = """INSERT INTO aml_twittertweet (
                             user_id, origin_ph, tweet_name, tweet_page_id, tweet_text, tweet_date
                             ) VALUES(
                             %s, %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, tweet_name, tweet_page_id, tweet_text, tweet_date))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def trends_insert(self, user_id, origin_ph, trends_name, trends_tweet_cnt):
        try:
            insert_command = """INSERT INTO aml_twittertrends (
                             user_id, origin_ph, trends_name, trends_tweet_cnt
                             ) VALUES(
                             %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, trends_name, trends_tweet_cnt))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def following_insert(self, user_id, origin_ph, following_name, following_page_id, following_info):
        try:
            insert_command = """INSERT INTO aml_twitterfollowing (
                             user_id, origin_ph, following_name, following_page_id, following_info
                             ) VALUES(
                             %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, following_name, following_page_id, following_info))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def follower_insert(self, user_id, origin_ph, follower_name, follower_page_id, follower_info):
        try:
            insert_command = """INSERT INTO aml_twitterfollower (
                             user_id, origin_ph, follower_name, follower_page_id, follower_info
                             ) VALUES(
                             %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, follower_name, follower_page_id, follower_info))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)
