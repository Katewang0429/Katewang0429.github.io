from flask import Flask,render_template
from flask import request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template('signin.html')

@app.route("/auth", methods=['POST'])
def auth():
    acctName = request.values['acctName']
    pwd = request.values['pwd']

    if str.upper(acctName) == "TEST" and str.upper(pwd) == "TEST":
        return render_template('member.html',**locals())
    else:
        return render_template('error.html',**locals())

if __name__ == '__main__':
	app.run(host='127.0.0.1',port='3000',debug=True)