from flask import Flask, render_template, url_for,request,redirect
from flask import Response
import mysql.connector

app=Flask(__name__)

conn=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="",auth_plugin='mysql_native_password')

cursor=conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")

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