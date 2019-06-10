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

sql = '''CREATE TABLE `gmail_info` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `mail_cnt` INT(11) NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

sql2 = '''CREATE TABLE `gmail_list` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_id` VARCHAR(255) NULL DEFAULT NULL,
        `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
        `gmail_sender` VARCHAR(255) NULL DEFAULT NULL,
        `gmail_sender_email` VARCHAR(255) NULL DEFAULT NULL,
        `gmail_title` VARCHAR(255) NULL DEFAULT NULL,
        `gmail_contents` VARCHAR(5000) NULL DEFAULT NULL,
        `gmail_date` DATE NULL DEFAULT NULL,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''

# sql3 = '''CREATE TABLE `gamil_sender` (
#         `no_index` INT(11) NOT NULL AUTO_INCREMENT,
#         `user_id` VARCHAR(255) NULL DEFAULT NULL,
#         `origin_ph` VARCHAR(255) NULL DEFAULT NULL,
#         `gamil_sender` VARCHAR(255) NULL DEFAULT NULL,
#         `send_cnt` INT(11) NULL DEFAULT NULL,
#         PRIMARY KEY (`no_index`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
#     ;'''


cursor.execute(sql)
cursor.execute(sql2)
# cursor.execute(sql3)
