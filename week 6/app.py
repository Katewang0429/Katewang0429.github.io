from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@@shine1234",
    database="website"
)


@app.route("/")
def index():
    if session.get('username') is not None:
        user = session['username']
        print(user)
        return render_template('member.html', user=user)
    return render_template('signin.html')


@app.route("/signup", methods=['POST'])
def register():
    reg_name = request.values['reg_name']
    reg_acct = request.values['reg_acct']
    reg_pwd = request.values['reg_pwd']

    cursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE username = '" + reg_acct + "';"
    print(sql)
    cursor.execute(sql)
    reg = cursor.fetchone()

    if reg != None:
        return redirect(url_for('error', message="帳號已經被註冊"))

    try:
        sql = "INSERT INTO user(id, name, username, password) VALUES (0, \"" + \
            reg_name + "\", \"" + reg_acct + "\", \"" + reg_pwd + "\");"
        cursor.execute(sql)
        mydb.commit()
        cursor.close()
    except Exception as e:
        print("Problem inserting into db: " + str(e))

    return redirect(url_for('index'))


@app.route("/member", methods=['POST'])
def member():
    acct = request.values['acct']
    pwd = request.values['pwd']

    if acct == "" or pwd == "":
        return redirect(url_for('error', message="您未輸入帳號或密碼"))

    cursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE username = '" + \
        acct + "' AND password = '" + pwd + "';"
    cursor.execute(sql)
    user = cursor.fetchone()

    cursor.close()

    if user != None:
        session['username'] = user[1]
        return render_template('member.html', user=user[1])
    return redirect(url_for('error', message="帳號或密碼輸入錯誤"))


@app.route('/error')
def error():
    session.pop('username', None)
    message = request.values['message']
    return render_template('error.html', message=message)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(host='127.0.0.1', port='3000', debug=True)
