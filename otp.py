import smtplib
import math
import random

mail=input("Enter your email address: ")
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sbaijal55@gmail.com','gckqxyohsacbrynf') #add your own email and password

digits="0123456789"
OTP=""
for i in range(6):
  OTP+=digits[math.floor(random.random()*10)]

message = f"""\
Subject: Your OTP is {OTP}

Do not share it with anyone"""
server.sendmail('sbaijal55@gmail.com',mail,message)
print("mail sent")

a= input("Enter your OTP: ")

if a == OTP:
  print("Verified")
else:
  print("Wrong OTP entered")
