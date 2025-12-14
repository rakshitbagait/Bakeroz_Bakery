from flask import Flask , render_template, request, url_for ,redirect,session
from flask_mail import Mail,Message
import os 
from dotenv import load_dotenv
import markdown
from smtplib import SMTP
from DbConnect import *
from verify import verification_code
from flask_login import current_user
# Returns the user ID as a string   
connection_db()
load_dotenv()


app = Flask(__name__)
app.secret_key =os.getenv("SECRET_KEY")
@app.route("/",methods =["POST","GET"])
def home():
    if request.method == "POST":
        return render_template ("login.html")
    return render_template("index.html")
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("Email")
        password = request.form.get("Password")
        user = get_user_by_mail(user_email=email)
        if user and user["password_hash"]==password:
            user_id = user["id"]
            print(user_id)
            session["user_id"] = user["id"]
            return render_template("home.html")
        if user and user["password_hash"] != password:
            return render_template("login.html", error ="Invalid password or email")
    return render_template("login.html")
@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "POST" :
        name = request.form.get("Name")
        email = request.form.get("Email")
        create_password = request.form.get("Create-password")
        confirm_password  = request.form.get("Confirm-password")
        user =  get_user_by_mail(email)
        if user and user["email"]== email:
            return render_template("signup.html", error= "User Exist. Login!")
        if create_password != confirm_password:
            return render_template("signup.html", error= "Password doesn't match!!")
        else:
            code = verification_code(user_mail=email)
            session["temp_name"] = name
            session["temp_email"] = email
            session["temp_password"] = str(create_password)
            session["verification_code"] = code
            return redirect(url_for("verify"))
    return render_template("signup.html")
@app.route("/verify", methods = ["GET","POST"])
def verify():
    if request.method == 'POST':
        user_input_code = request.form.get("code-for-verification")
        if user_input_code == session.get("verification_code"):
            user_name =session.get("temp_name")
            password =session.get("temp_password")
            verification_code =session.get("verification_code")
            user_email = session.get("temp_email")
            add_to_db(user_name=user_name,
                email=user_email,password_hash=password,user_role="customer",is_verified=True,verification_code=verification_code)
            return render_template("home.html")
    return render_template("verify.html")
@app.route("/homepage")
def homepage():
    return render_template("home.html")
@app.route("/search",methods=["GET","POST"])
def search():
    if request.method =="POST":
        search_item = request.form.get("search-box").lower()
        search_items_from_db(search_query=search_item)
    return render_template("home.html")
@app.route("/account",methods = ["POST","GET"])
def account():
    delete = False
    user_id = int(session.get("user_id"))
    print("This is user id ",user_id)
    user = get_user_by_id(user_id=user_id)
    # print(user)
    user_name = user["user_name"]
    user_email = user["email"]
    if request.method == "POST":
        delete = True
        if request.form.get("cancel") is not None:
                 delete = False
                 return render_template("account.html", Name = user_name, Email = user_email ,delete = delete)
        if request.form.get("confirm") is not None:
                session.clear()
                delete_account(user_id=user_id)       
                return  redirect(url_for("logout"))
    return render_template("account.html", Name = user_name, Email = user_email ,delete = delete)
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug = True,use_reloader = False)