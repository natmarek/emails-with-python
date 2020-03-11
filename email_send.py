import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']= 'madeupemail1@outlook.com'
email['to'] = 'madeupemail2@outlook.com'
email['subject'] = 'Hey you!'

email.set_content('Have a good day!')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()             #this is an encryption method
    smtp.login('madeupemail1@outlook.com', 'Madeuppassword123')
    smtp.send_message(email)
    print('all good boss!')