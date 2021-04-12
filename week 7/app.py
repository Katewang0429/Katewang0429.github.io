from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_restful import Resource, Api, reqparse
import os
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.secret_key = os.urandom(24)

api = Api(app)

connection = pymysql.connect(host="127.0.0.1",
                             user="root",
                             password="@@shine0429",
                             db="website",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@ app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass

    if session.get('username'):
        user = session['username']
        return redirect(url_for('member', user=user))
    return redirect(url_for('signin'))

# 透過python 建立api


@ app.route("/api/users", methods=['GET', 'POST'])
def users():
    user = []  # []list
    if request.method == 'POST':
        pass

    if 'username' in request.args:
        username = request.args['username']  # 從URL拿到Username
    else:
        return "錯誤: API-URL沒有提供{0}，請指定一個{0}".format("username")

    cursor = connection.cursor()
    sql = "SELECT * FROM user WHERE username = '{0}';".format(username)
    cursor.execute(sql)
    users = cursor.fetchone()  # users為資料庫users
    cursor.close()
    # 將資料庫資料組合成json 格式
    if users:
        user.append({
            "id": users["id"],
            "name": users["name"],
            "username": users["username"]
        })
        result = dict(data=user)
    else:
        result = dict(data=None)

    return jsonify(result)  # result 值為字典，再轉為json 格式


@ app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        acct = request.values['acct']
        pwd = request.values['pwd']

        if acct == "" or pwd == "":
            return redirect(url_for('error', message="您未輸入帳號或密碼"))

        try:
            cursor = connection.cursor()

            sql = "SELECT * FROM user WHERE username = '{0}' AND password = '{1}';".format(
                acct, pwd)
            cursor.execute(sql)
            user = cursor.fetchone()
            cursor.close()
            if user:
                session['username'] = user['name']
                return redirect(url_for('member'))
            return redirect(url_for('error', message="未註冊帳號 或 帳號或密碼輸入錯誤"))
        except Exception as e:
            print("Problem select from db: " + str(e))

    return render_template('signin.html')


@ app.route("/signup", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        reg_name = request.values['reg_name']
        reg_acct = request.values['reg_acct']
        reg_pwd = request.values['reg_pwd']

        if reg_name == "" or reg_acct == "" or reg_pwd == "":
            return redirect(url_for('error', message="您未輸入姓名或帳號或密碼"))

        try:
            cursor = connection.cursor()
            sql = "SELECT * FROM user WHERE username = '{0}';".format(
                reg_acct)

            cursor.execute(sql)
            reg = cursor.fetchone()

            if reg:
                return redirect(url_for('error', message="帳號已經被註冊"))

            sql = "INSERT INTO user(id, name, username, password) VALUES (0, \"{0}\", \"{1}\", \"{2}\");".format(
                reg_name, reg_acct, reg_pwd)
            cursor.execute(sql)
            connection.commit()
            cursor.close()

        except Exception as e:
            print("Problem inserting into db: " + str(e))

        return redirect(url_for('index'))

    return render_template('signup.html')


@ app.route("/member", methods=['GET', 'POST'])
def member():
    if request.method == 'POST':
        pass

    if session.get('username'):
        username = session['username']
        cursor = connection.cursor()
        sql = "SELECT * FROM user WHERE username = '{0}';".format(username)

        cursor.execute(sql)
        user = cursor.fetchone()

        return render_template('member.html', user=user['name'])
    return redirect(url_for('signin'))


@ app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        pass

    session.pop('username', None)
    message = request.values['message']
    return render_template('error.html', message=message)


@ app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
