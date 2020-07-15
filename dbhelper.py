import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host='localhost', user='root', password='', database='quiz')
            self.mycursor=self.conn.cursor()
            print("Connected to DB")
        except Exception as e:
            print(e)

    def check_login(self,email,password):
        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
        data=self.mycursor.fetchall()
        return data


    def insert_user(self, name, email, password, gender):
        # insert_user===reg_submit
        try:
            # print("INSERT INTO user (user_id,name,email,password) VALUES (NULL,'{}','{}','{}','{}')".format(name,email,password,gender))
            self.mycursor.execute("INSERT INTO users (user_id,name,email,password,gender) VALUES (NULL,'{}','{}','{}','{}')".format(name,email,password,gender))
            self.conn.commit()
            return 1
        except Exception as e:
            print(e)
            return 0


    def fetch_others(self, user_id):
        self.mycursor.execute("SELECT * FROM user WHERE user_id NOT LIKE {}".format(user_id))
        data = self.mycursor.fetchall()
        return data