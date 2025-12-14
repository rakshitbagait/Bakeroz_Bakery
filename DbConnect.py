import mysql.connector

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

def add_to_db(user_name,
    email,password_hash,user_role,is_verified,verification_code) :
    db =connection_db()
    cursor = db.cursor()
    query = """INSERT INTO user(user_name,
    email,password_hash,user_role,is_verified,verification_code) 
    values (%s,%s,%s,%s,%s,%s)"""

    values = (user_name,
    email,password_hash,user_role,is_verified,verification_code) 
    cursor.execute(query,values)
    db.commit()
    cursor.close()
    db.close()
    return 0

def get_user_by_mail(user_email):
    db = connection_db()
    cursor = db.cursor(dictionary=True)
    query  = """SELECT * FROM user WHERE email = %s"""
    cursor.execute(query,(user_email,))
    user= cursor.fetchone()
    return user
def search_items_from_db(search_query):
    db = connection_db()
    cursor = db.cursor()
    db_query = "SELECT * FROM products WHERE name LIKE %s "
    cursor.execute(db_query,("%"+search_query+"%",))
    return cursor.fetchall()
def get_user_by_id(user_id):
    db = connection_db()
    cursor = db.cursor(dictionary=True)
    query = """ SELECT * FROM user WHERE id = %s """
    cursor.execute(query,(user_id,))
    return cursor.fetchone()
def delete_account(user_id):
    db = connection_db()
    cursor = db.cursor()
    query = """ Delete from user where id = %s"""
    cursor.execute(query,(user_id,))
    db.commit()
    cursor.close()
    db.close()
    return 0