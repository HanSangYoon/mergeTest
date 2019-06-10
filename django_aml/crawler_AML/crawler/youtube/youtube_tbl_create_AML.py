import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    db='AML',
    charset='utf8mb4')
print(db)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchall()
print(version)

sql = '''CREATE TABLE `youtube_info` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `username` VARCHAR(255) NULL DEFAULT NULL,
        `subscribe_cnt` INT(11) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql2 = '''CREATE TABLE `youtube_subscribe` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `channel_name` VARCHAR(5000) NULL DEFAULT NULL,
        `channel_info` VARCHAR(255) NULL DEFAULT NULL,
        `channel_sub_cnt` INT(11) NULL DEFAULT NULL,
        `channel_video_cnt` INT(11) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql3 = '''CREATE TABLE `youtube_recent_video` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `video_channel_name` VARCHAR(255) NULL DEFAULT NULL,
        `video_name` VARCHAR(255) NULL DEFAULT NULL,
        `video_info` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql4 = '''CREATE TABLE `youtube_comment_history` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `video_name` VARCHAR(255) NULL DEFAULT NULL,
        `video_comment` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
