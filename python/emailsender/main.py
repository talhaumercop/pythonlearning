# import smtplib
#
# email = "talhaumar097@gmail.com"
# password = "yyxb ktmu hayr qopk"  # Not your Gmail password
#
# # Correct: use port 587
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(email, password)
# connection.sendmail(email, "yourzlove56@gmail.com", "Subject: Test\n\nHello from Python!")
# connection.close()

import datetime as dt

now=dt.datetime.now()
weekday=now.weekday()

birthdays=[]

if weekday==