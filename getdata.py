import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="user_db")
cur = conn.cursor()


def get_data():
    try:
        sql = "SELECT * FROM account"
        cur.execute(sql)
        rs = cur.fetchall()
        if not rs:
            print("Data empty!\n")
        else:
            print("=== Account info ===")
            print("ID\tUsername\tPassword\tFullname")
            for row in rs:
                print("%s\t%s\t\t%s\t\t%s" % (row[0], row[1], row[2], row[3]))
            print("====================")
    except:
        conn.rollback()


def get_by_acc(acc, pwd):
    try:
        sql = "SELECT  balance, name FROM account WHERE user =%s AND pass =%s"
        cur.execute(sql, (acc, pwd))
        rs = cur.fetchone()
        if not rs:
            return None
        else:
            return rs
    except:
        conn.rollback()


def update_data(value):
    try:
        sql = "UPDATE `account` SET `balance`=%s WHERE `acc`=%s"
        # adr = tuple()  # ("accB", )
        cur.execute(sql, value)
        conn.commit()
        print("Update success!\n")
    except:
        conn.rollback()
