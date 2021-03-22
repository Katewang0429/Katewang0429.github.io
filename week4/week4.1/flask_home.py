from flask import Flask,render_template
from flask import request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    acctName = request.values['acctName']
    pwd = request.values['pwd']
    return render_template('submit.html',**locals())

if __name__ == '__main__':
	app.run(host='127.0.0.1',port='3000',debug=True)