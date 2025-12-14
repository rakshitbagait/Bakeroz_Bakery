import random
import string
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
def verification_code(user_mail):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    message ="Please enter this code to verify your self"
    verification_code = ""

    for _ in range(2):
        random_lower = random.choice(lowercase_letters)
        random_upper = random.choice(uppercase_letters)
        random_digit = random.choice(digits)

        verification_code += random_lower
        verification_code += random_upper
        verification_code += random_digit
    
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(os.getenv("MY_EMAIL"),os.getenv("MY_PASSWORD"))
        connection.sendmail(from_addr=os.getenv("MY_EMAIL"),
                        to_addrs=user_mail,
                        msg =f"Subject:Verification Code\n\n{verification_code}\n{message}")
        
    return verification_code






