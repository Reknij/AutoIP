from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import configManager

config = configManager.getConfig()

def SendGmail(subject,content):
    message = MIMEMultipart()
    message['From'] = config.sender
    message['To'] = config.receiver
    message['Subject'] = subject  #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    #Create SMTP session for sending the mail
    session = SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(config.sender, config.senderPass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(config.sender, config.receiver, text)
    session.quit()
