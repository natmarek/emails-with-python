import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path         #similar to os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from']='madeupemail1@outlook.com'
email['to'] ='madeupemail2@outlook.com'
email['subject'] = 'Hey you!'

email.set_content(html.substitute(name= 'Pingu'), 'html')   # email.set_content(html.substitute({'name'= 'Pingu'})) if that html file has mltpl variables

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()             #this is an encryption method
    smtp.login('madeupemail1@outlook.com', 'Madeuppassword123')
    smtp.send_message(email)
    print('all good boss!')