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