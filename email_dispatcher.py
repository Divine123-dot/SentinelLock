#smtplib makes python connect to an email server to send alrt messages

import smtplib

#MIME is module that allow the system to build emails with text, headers, and file attachments

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os


#send_security_alert function when the an authorized person try to access the phone the system send an email to the user. where they can get even from aother device

def send_security_alert(subject: str, body_text: str, attachment_path: str = None):

    #the system grab credentials from environment variables

    send_email = os.getenv("ALERT_SENDER_EMAIL")
    send_password = os.getenv("ALERT_SENDER_PASSWORD")
    recipient_email = os.getenv("ALERT_RECIPIENT_EMAIL")

    #in case the credentials are not set up yet, don't crash just return false

    if not send_email or not send_password or not recipient_email:
        print("Email credentials missing in environment variables")

        return False

    try:

        #MIMEMultipart() keeps the email details like a full message like text, location and encrypted photo

        msg = MIMEMultipart()

        #setting email headers

        msg["From"] = send_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        #MIMEText is the pain text that are wrapped in the email is like a package that email server accept instead sending plain text
        #msg.attach is used to put the text inside the msg envelope

        msg.attach(MIMEText(body_text, "plain"))

        #checking if the attachment_path was given and exists on the device

        if attachment_path and os.path.exists(attachment_path):

        #openning the file in the rb mode and load it into MIMEBase
            with open(attachment_path, "rb") as attachment_file:

                #application and octet-scream create a binary file download container and set_payload loads the raw encrypted bytes into it
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment_file.read())

            #in this section, we encode the file for email transit label its filename and attach it to msg because the email server can only transmit text characters across internet not binary

            encoders.encode_base64(part)
            filename = os.path.basename(attachment_path)

            part.add_header("Content-Disposition", f"attachment; filename={filename}")

            msg.attach(part)   
    

        #smtplib.SMTP open connection to email server. the 587 is the standart secure submission port

        server = smtplib.SMTP("smtp.gmail.com", 587)

        #starttls is critical for network security because you do not want your password to travel across wifi in plain text. using starttls hide the connection in transport layer security

        server.starttls()

        #log in to the email account while using the sender email and password; send the mail and close the connection, it converts our msg into formatted email string and dispatches it from the sender email to reciept email

        server.login(send_email, send_password)
        server.sendmail(send_email, recipient_email, msg.as_string())

        #quit() clean ou the logs and disconnect network

        server.quit()
        return True

    #in case, the thief turn off the connection or switch to the airplane mode the try block will jump down to except Execption as e and return false instead of crashing the app

    except Exception as e:
        print(f"Failed to send email alert: {e}")

        return False


#we are testing the email alert dispatcher

if __name__ == "__main__":

    #testing the email alert call

    result = send_security_alert("SentinelOCK Test Alert", "Intruder detected on device!")

    print(f"Email dispatch test result: {result}")



