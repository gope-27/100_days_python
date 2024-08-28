import smtplib
import random
import pandas as pd
import random
import datetime

my_email = ""
password = ""


now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt")as data_file:
        all_quotes = data_file.readlines()
        df1 = random.choice(all_quotes)

        # Set up the SMTP server connection with port 587
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()  # Start TLS encryption
        connection.login(user=my_email, password=password)

        # # Properly format the message with subject and body
        # subject = "Test Email"
        # body = "Hello"
        # msg = f"Subject: {subject}\n\n{body}"

        # Send the email
        connection.sendmail(from_addr=my_email, to_addrs="gopenath.27@gmail.com", msg=f"Subject:Wednesday Motivation\n\n{df1}")
        connection.close()

        print("Email sent successfully!")