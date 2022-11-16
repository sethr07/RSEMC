#!env/bin/python
import this
from utils import *
import smtplib
import ssl

""" 
try:
    session = smtplib.SMTP(server, port) #use gmail with port
except Exception as e:
    print("Failed to establish Session : ", str(e))

try:
    session.starttls()
except Exception as e:
    print("Failed to establish TLS Layer : ", str(e))

try:
    session.login(sender_address, sender_pass) #login with mail_id and password
except Exception as e:
    print("Failed to login into Sender Account : ", str(e))

text = message.as_string()

try:
    session.sendmail(sender_address, receiver_address, text)
except Exception as e:
    print("Failed to Send Mail : ", str(e))

session.quit()
print('Mail sent and ended Sesion')
"""

def main():
    myname = intro()
    thisuser = User()
    thisuser.name = myname
    sender, login_pass = login()
    thisuser.email_id = sender
    thisuser.password = login_pass
    
    receiver = recv_email()
    server, port = config_server()


if __name__ == "__main__":
    main()




