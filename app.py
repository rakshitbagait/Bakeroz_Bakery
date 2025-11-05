from flask import Flask , render_template, request
from flask_mail import Mail,Message
import os 
from dotenv import load_dotenv
import mysql.connector
import markdown
from smtplib import SMTP

app = Flask(__name__)
def connection_db():
    bakery_db = mysql.connector.connect(
        host = "localhost",
        user= "root",
        password = "password",
        database = "Bakery_db",
        use_pure = True,
        port = 3306
    )

    return bakery_db
@app.route("/")
def login():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug = True)
    