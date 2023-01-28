import smtplib

mailFrom =  "BITCOin_Wins.com"
passowrd = "napsujhjscxmazjf"
user = "marekp806@gmail.com"
mailTo = ["marszcz806@gmail.com"]
mailSubject = "FREEE BITCOIN!!"

mailBody = """Hello

Your computer have a virus!!

Do not answer.

Have a nice day!"""
message = """From:{}
Subject:{}

{}
""".format(mailFrom,mailSubject,mailBody)

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.ehlo()
    server.login(user, passowrd)
    for i in range(0,2):
        server.sendmail(user,mailTo,message)
    server.close()
    print("Success")
except:
    print("fail")