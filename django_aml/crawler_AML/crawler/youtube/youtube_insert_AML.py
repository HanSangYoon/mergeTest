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
    def youtube_insert(self, user_id, origin_ph, username, subscribe_cnt):
        try:
            insert_command = """INSERT INTO aml_youtubeinfo (
                             user_id, origin_ph, username, subscribe_cnt
                             ) VALUES (
                             %s, %s, %s, %s)
                            """
            print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, username, subscribe_cnt))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def subscriber_insert(self, user_id, origin_ph, channel_name, channel_info, channel_sub_cnt, channel_video_cnt):
        try:
            insert_command = """INSERT INTO aml_youtubesubscribe (
                             user_id, origin_ph, channel_name, channel_info, channel_sub_cnt, channel_video_cnt
                             ) VALUES(
                             %s, %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, channel_name, channel_info, channel_sub_cnt,
                                                 channel_video_cnt))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def recent_video_insert(self, user_id, origin_ph, video_channel_name, video_name, video_info):
        try:
            insert_command = """INSERT INTO aml_youtuberecentvideo (
                             user_id, origin_ph, video_channel_name, video_name, video_info
                             ) VALUES(
                             %s, %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, video_channel_name, video_name, video_info))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)

    def comment_history_insert(self, user_id, origin_ph, video_name, video_comment):
        try:
            insert_command = """INSERT INTO aml_youtubecommenthistory (
                             user_id, origin_ph, video_name, video_comment
                             ) VALUES(
                             %s, %s, %s, %s)
                            """
            # print('insert ok', insert_command)
            self.cursor.execute(insert_command, (user_id, origin_ph, video_name, video_comment))
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print('db 에러', e)
