import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "Sender's name"
email['to'] = 'insert receiver email'
email['subject'] = 'You won 999,999,999 euro!'

email.set_content(html.substitute({'name': 'DenDon'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender email', 'sender password')
    smtp.send_message(email)
    print('all good boss!') 