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

sql = '''CREATE TABLE `twitter_info` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `username` VARCHAR(255) NULL DEFAULT NULL,
        `page_id` VARCHAR(255) NULL DEFAULT NULL,
        `tweet_cnt` INT(11) NULL DEFAULT NULL,
        `following_cnt` INT(11) NULL DEFAULT NULL,
        `follower_cnt` INT(11) NULL DEFAULT NULL,
        `joined_date` DATE NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql2 = '''CREATE TABLE `twitter_tweet` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `tweet_name` VARCHAR(255) NULL DEFAULT NULL,
        `tweet_page_id` VARCHAR(255) NULL DEFAULT NULL,
        `tweet_text` VARCHAR(255) NULL DEFAULT NULL,
        `tweet_date` DATE NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql3 = '''CREATE TABLE `twitter_trends` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `trends_name` VARCHAR(255) NULL DEFAULT NULL,
        `trends_tweet_cnt` INT(11) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql4 = '''CREATE TABLE `twitter_following` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `following_name` VARCHAR(255) NULL DEFAULT NULL,
        `following_page_id` VARCHAR(255) NULL DEFAULT NULL,
        `following_info` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql5 = '''CREATE TABLE `twitter_follower` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `follower_name` VARCHAR(255) NULL DEFAULT NULL,
        `follower_page_id` VARCHAR(255) NULL DEFAULT NULL,
        `follower_info` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

# cursor.execute(sql)
# cursor.execute(sql2)
# cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
