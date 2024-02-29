import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "kyleh777programming@gmail.com"
password = "fuudiqfrnpwurkbj"

receiver = "kyleh777programming@gmail.com"
context = ssl.create_default_context()

message = '''\
subject:Hey
you sent it
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
