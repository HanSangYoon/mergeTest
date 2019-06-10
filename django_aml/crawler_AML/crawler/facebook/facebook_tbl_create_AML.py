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

sql = '''CREATE TABLE `facebook_info` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `username` VARCHAR(255) NULL DEFAULT NULL,
        `gender` VARCHAR(255) NULL DEFAULT NULL,
        `phone_number` VARCHAR(255) NULL DEFAULT NULL,
        `birthday` VARCHAR(255) NULL DEFAULT NULL,
        `company1` VARCHAR(255) NULL DEFAULT NULL,
        `company2` VARCHAR(255) NULL DEFAULT NULL,
        `company3` VARCHAR(255) NULL DEFAULT NULL,
        `university1` VARCHAR(255) NULL DEFAULT NULL,
        `university2` VARCHAR(255) NULL DEFAULT NULL,
        `university3` VARCHAR(255) NULL DEFAULT NULL,
        `address1` VARCHAR(255) NULL DEFAULT NULL,
        `address2` VARCHAR(255) NULL DEFAULT NULL,
        `address3` VARCHAR(255) NULL DEFAULT NULL,
        `contact1` VARCHAR(255) NULL DEFAULT NULL,
        `contact2` VARCHAR(255) NULL DEFAULT NULL,
        `contact3` VARCHAR(255) NULL DEFAULT NULL,
        `contact4` VARCHAR(255) NULL DEFAULT NULL,
        `friends_cnt` INT(11) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql2 = '''CREATE TABLE `facebook_post` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `post_text` VARCHAR(5000) NULL DEFAULT NULL,
        `post_info` VARCHAR(255) NULL DEFAULT NULL,
        `post_date` DATE NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql3 = '''CREATE TABLE `facebook_friends` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `friends_name` VARCHAR(255) NULL DEFAULT NULL,
        `friends_info` VARCHAR(255) NULL DEFAULT NULL,
        `friends_id` VARCHAR(255) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
