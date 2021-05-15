from flask import Flask, render_template, url_for,request,redirect
from flask import Response
import mysql.connector

app=Flask(__name__)

conn=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="registration",auth_plugin='mysql_native_password')

cursor=conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register",methods=['POST','GET'])
def register():
    fname=request.form.get("fname")
    lname=request.form.get("lname")
    country=request.form.get("country")
    city=request.form.get("city")
    zip=request.form.get("zip")
    cursor.execute("""INSERT INTO `details` (`id`,`FIRST_NAME`,`LAST_NAME`,`COUNTRY`,`CITY`,`ZIP`) 
    VALUES (NULL,'{}','{}','{}','{}','{}')""".format(fname,lname,country,city,zip,cursor))
    conn.commit()
    return redirect('/success')


@app.route("/success")
def success():
    return render_template("submit.html")

@app.route("/failed")
def failed():
    return render_template("duplicate.html")

@app.route('/submit',methods=['POST'])
def submit():
    return redirect('/success')

if __name__=="__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)     