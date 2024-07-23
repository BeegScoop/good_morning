import pandas
import random
import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
load_dotenv()
my_email = os.getenv("my_email")
password = os.getenv("password")
send_to = os.getenv("send_to")
send_tester = os.getenv("send_tester")

with open("base_letter.txt") as file:
    letter = file.read()
with open("greetings.txt") as file:
    greetings = file.readlines()
greeting = random.choice(greetings)
greeting = greeting.strip()
with open("quotes.txt") as file:
    quotes = file.readlines()
quote = random.choice(quotes)
quote = quote.strip()

filepath = f"./heart_art/heart_2.txt"
with open(filepath) as file:
    heart = file.read()


letter = letter.replace("[GREETING]",greeting)
letter = letter.replace("[QUOTE]",quote)
letter = letter.replace("[HEART]",heart)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=send_to,
        msg=f"Subject: Good Morning :) \n\n{letter}"
    )