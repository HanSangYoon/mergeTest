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


sql = '''CREATE TABLE `user_info` (
        `no_index` INT(11) NOT NULL AUTO_INCREMENT,
        `user_name` VARCHAR(255) NULL DEFAULT NULL,
        `user_ph` VARCHAR(255) NULL DEFAULT NULL,
        `facebook_id` VARCHAR(255) NULL DEFAULT NULL,
        `facebook_pw` VARCHAR(255) NULL DEFAULT NULL,
        `google_id` VARCHAR(255) NULL DEFAULT NULL,
        `google_pw` VARCHAR(255) NULL DEFAULT NULL,
        `instagram_id` VARCHAR(255) NULL DEFAULT NULL,
        `instagram_pw` VARCHAR(255) NULL DEFAULT NULL,
        `twitter_id` VARCHAR(255) NULL DEFAULT NULL,
        `twitter_pw` VARCHAR(255) NULL DEFAULT NULL,
        `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`no_index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ;'''


cursor.execute(sql)
