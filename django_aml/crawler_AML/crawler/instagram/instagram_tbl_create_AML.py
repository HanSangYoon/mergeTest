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

sql = '''CREATE TABLE `instagram_info` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `page_id` VARCHAR(255) NULL DEFAULT NULL,
        `username` VARCHAR(255) NULL DEFAULT NULL,
        `intro` VARCHAR(255) NULL DEFAULT NULL,
        `homepage` VARCHAR(255) NULL DEFAULT NULL,
        `post_cnt` INT(11) NULL DEFAULT NULL,
        `follower_cnt` INT(11) NULL DEFAULT NULL,
        `follow_cnt` INT(11) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql2 = '''CREATE TABLE `instagram_post` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `post_text`  VARCHAR(5000) DEFAULT NULL,
        `post_place` VARCHAR(255) NULL DEFAULT NULL,
        `post_like` INT(11) NULL DEFAULT NULL,
        `post_view` INT(11) NULL DEFAULT NULL,
        `post_date` DATE NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql3 = '''CREATE TABLE `instagram_follower` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `follower_id` VARCHAR(255) NULL DEFAULT NULL,
        `follower_name` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql4 = '''CREATE TABLE `instagram_follow` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `follow_id` VARCHAR(255) NULL DEFAULT NULL,
        `follow_name` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''
cursor.execute(sql)
# cursor.execute(sql2)
# cursor.execute(sql3)
# cursor.execute(sql4)
