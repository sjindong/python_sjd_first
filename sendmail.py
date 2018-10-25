#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header

import config
 
mail_host = config.mail_host      
mail_user = config.mail_user      
mail_pass = config.mail_pass      
 
sender = config.mail_sender            
receivers = config.mail_receivers      

def sendEmail(title,content):
    message = MIMEText(content, 'plain', 'utf-8')  
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
 
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
        smtpObj.login(mail_user, mail_pass) 
        smtpObj.sendmail(sender, receivers, message.as_string()) 
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
    pass

def sendEmailDef(title,content,filepath,filename):
    send_emailFile(config.mail_host,
        config.mail_user,
        config.mail_pass,
        config.mail_receivers,
        title,content,filepath,filename)
    pass
 
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
 
    email_client.quit()
    pass

def send_emailFile(SMTP_host, from_account, from_passwd, to_account, subject, content,filepath,filename):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    message.attach(MIMEText(content, 'plain', 'utf-8'))
 
    att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')  
    att["Content-Type"] = 'application/octet-stream'  
    att["Content-Disposition"] = 'attachment; filename="'+filename+'"'  
    msg.attach(att)
    email_client.sendmail(from_account, to_account, msg.as_string())
 
    email_client.quit()
    pass


if __name__ == '__main__':  
    test_content = '我用Python'    
    test_title = '人生苦短'         
    sendEmail(test_title,test_content)

    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
    pass