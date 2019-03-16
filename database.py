from flask import Flask, render_template
import sqlite3

class DataBase():
    def __init__(self):
        conn = sqlite3.connect('splite3.db')

    def create(self, conn):
        query = """
            CREATE TABLE IF NOT EXISTS MEMBER(
                USERID VARCHAR(10) PRIMARY KEY,
                PASSWORD VARCHAR(10),
                PHONE VARCHAR(10),
        REGDATE DATE DEFAULT CURRENT_TIMESTAMP
        );
        """
        print('쿼리체크')
        print(query)
        conn.execute(query)
        conn.commit()

    def insertMany(self, conn):
        data = [
            ('lee', '1', '010-1234'),
            ('kim', '1', '010-2345'),
            ('park', '1', '010-4567')
        ]
        # stmt = "INSERT INTO MEMBER(USERID, PASSWORD, PHONE) VALUES(?, ?, ?)"
        # conn.executemany(stmt, data)
        # conn.commit()

    def fetchone(self, conn):
        cursor = conn.execute("SELECT * FROM MEMBER WHERE USERID LIKE 'lee'")
        row = cursor.fetchone()
        print('이씨')
        print(row)

    def fetchall(self, conn):
        cursor = conn.execute("SELECT * FROM MEMBER")
        rows = cursor.fetchall()
        count = 0;
        for i in rows:
            count += 1

        print(count)
