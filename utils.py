import os 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from importlib_metadata import email

class User():
    __slots__ = ['name', 'email_id', 'password']
    
    def __init__(self):
        self.name = "" 
        self.email_id = "" 
        self.password = "" 
    
    def print_acc(self):
        print("\n-----------------------\n")
        print("Account Details for: ", self.name)
        print("Email: ", self.email_id)
        print("\n-----------------------\n")
        print("\n")
    

def login():
    print("Welcome to User Config")
    print("Enter your Email ID (my@example.com)")
    sender_id = input()
    print("Enter your password")
    password = input()
    return sender_id, password


def intro():
    print("Welcome to Email Client")
    print("Enter your name")
    name = input()
    return name 

def recv_email():
    print("Enter the email for receiver")
    recv_id = input()
    return recv_id

def config_server():
    def_server, def_port = "smtp@gmail.com", 587
    print("Welcome to Server Cofigurations")
    print("Do you want to use default setting or Custom? (D/C)")
    setting = input()

    if setting == 'D':
        return def_server, def_port
    else:
        print("Enter Server you want to you use")
        server = input()
        print("Enter port you want to use")
        port = input()
        return server, port

def set_message(sender_address, receiver_address, subject, mail_content):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject 
    message.attach(MIMEText(mail_content, 'plain'))


def write_sub():
    print("Enter Subject (One Line)")
    sub = input()

    if sub is None:
        print("Are you sure you want empty subject? (Y/N)")
        choice = input()
        if choice == 'Y':
            return ""
        else:
            sub = input("Enter Subject (One Line)")
            return sub
    return  sub

def write_mail():
    print("Write your email in the terminal below")
    content = []

    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)




