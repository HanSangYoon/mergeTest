import pymysql


def select():
    db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='1234',
        db='AML',
        charset='utf8mb4')
    print(db)
    cursor = db.cursor()

    sql = 'SELECT * FROM `user_info`;'

    cursor.execute(sql)
    return cursor.fetchall()
