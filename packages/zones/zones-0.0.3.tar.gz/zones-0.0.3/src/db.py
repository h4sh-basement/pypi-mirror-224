import tkinter

from configparser import ConfigParser
from tkinter import Message

import sqlalchemy


class Db(object):
    def __init__(self):
        # Create mysql connection
        self.users: dict = {
            "id": 0,
            "email": "",
            "username": "",
            "password": "",
            "phone": "",
            "first_name": "",
            "last_name": "",
            "created_at": "",
            "updated_at": ""
        }
        self.config = ConfigParser()
        self.config.add_section('mysql')
        self.config.read(filenames="config.ini")
        self.host = self.config.get(section='mysql', option='host')
        self.user = self.config.get(section='mysql', option='user')
        self.password = self.config.get(section='mysql', option='password')
        self.database = self.config.get(section='mysql', option='database')
        self.port = self.config.get(section='mysql', option='port')
        self.engine = sqlalchemy.create_engine(
            "mysql+mysqldb://" + self.user + ":" + self.password + "@localhost:3306/zones?charset=utf8mb4",
            connect_args={"charset": "utf8mb4"}
        )
        self.conn = self.engine.connect()
        self.cur = self.conn.engine.connect()

        if self.conn is None:
            print("Error: unable to connect to MySQL server.")
            tkinter.Message(text="Error: unable to connect to MySQL server.")

            return

        self.cur.exec_driver_sql("CREATE  DATABASE IF NOT EXISTS " + self.database)

        self.cur.exec_driver_sql(
            'CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255)'
            ',username VARCHAR(255), password VARCHAR(255), phone VARCHAR(255),'
            'first_name VARCHAR(255), last_name VARCHAR(255), created_at DATETIME, updated_at DATETIME)')

    def verify(self, username: str = "", password: str = ""):

        self.cur.exec_driver_sql(
            'SELECT * FROM users WHERE username=? AND password=?',
            (username, password)
        )
        user = self.cur.exec_driver_sql('SELECT * FROM users WHERE  username=? ', (username,))
        if user:
            user = self.cur.exec_driver_sql(
                'SELECT * FROM users WHERE username=? AND password=?',
                (username, password)
            )

            if user:
                self.users = user

                return True

            else:

                message = "Wrong password"
                Message(text=message)

        else:

            message = "username or password incorrect"
            Message(text=message)

        return False

    def save(self, _bar_data_data):

        cursor = self.conn
        cursor.exec_driver_sql(
            "CREATE TABLE IF NOT EXISTS candles (id INT AUTO_INCREMENT PRIMARY KEY,"
            "time datetime ,symbol VARCHAR(255) NOT NULL,"
            "open REAL NOT NULL,"
            "high REAL NOT NULL,"
            "low REAL NOT NULL,"
            "close REAL NOT NULL,"
            "volume REAL NOT NULL)" + "")
        self.conn.commit()
        cursor.exec_driver_sql(
            "CREATE TABLE IF NOT EXISTS bars (id INT AUTO_INCREMENT PRIMARY KEY,"
            "time datetime,symbol VARCHAR(255) NOT NULL,"
            "open REAL NOT NULL,"
            "high REAL NOT NULL,"
            "low REAL NOT NULL,"
            "close REAL NOT NULL,"
            "volume REAL NOT NULL)" + "")
        self.conn.commit()

        cursor.exec_driver_sql(
            "INSERT INTO candles (time,symbol,open,high,low,close,volume) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (_bar_data_data['time'], _bar_data_data['symbol'], _bar_data_data['open'],
             _bar_data_data['high'], _bar_data_data['low'], _bar_data_data['close'],
             _bar_data_data['volume']))
        self.conn.commit()
