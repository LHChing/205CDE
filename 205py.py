from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

app.secret_key="000000"

db=mysql.connector.connect(
    host='localhost',
    user="LHC",
    password="000000",
    database="myshop"
)


@app.route("/")
def homepage():
	return render_template("Home.html")

@app.route("/newarrival")
def newarrival():
	return render_template("Newarrival.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
	if request.method == 'POST' and 'comment' in request.form:
	    comment = request.form['comment']
	    time = datetime.now()
	    cursor = db.cursor(dictionary=True)
	    cursor.execute('INSERT INTO comment VALUES (%s, %s)', (time, comment))
	    db.commit()
	return render_template("contact.html")

@app.route("/product")
def product():
	return render_template("product.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/preorder", methods=['GET','POST'])
def preorder():
	if request.method == 'POST' and 'name' in request.form:
	    name = request.form['name']
	    phone = request.form['phone']
	    email = request.form['email']
	    amt = request.form['amt']
	    cursor = db.cursor(dictionary=True)
	    cursor.execute('INSERT INTO preorder VALUES (%s, %s, %s, %s)', (name, phone, email, amt))
	    db.commit()
	    return redirect (url_for('ordered'))
	return render_template("preorder.html")


@app.route("/ordered")
def ordered():
	return render_template("ordered.html")

@app.route("/test")
def test():
	if request.method == 'POST' and 'comment' in request.form:
	    cursor = mysql.cursor(dictionary=True)
	    records=cursor.execute('SELECT * FROM comment')
	    mysql.commit()
	return render_template("test.html")





if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0",port=8000)
