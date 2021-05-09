from flask import Flask, render_template, url_for,request,redirect
from flask import Response
import mysql.connector

app=Flask(__name__)




cursor=conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)     