import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

port = 465
paswrd = 'nrtqsyfjkoncjbem'
login_email = 'pythontestemailshtrikuldmitry'
recipient = 'dmitriyshtrikul@gmail.com'

message_text = """\
Subject:hello there
Hi
How are you?"""

message_html = """\
<html>
  <body>
    <p>Hi,<br>
       <b>How are you?</b><br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

message = MIMEMultipart('alt')
message['Subject'] = 'Test HTML'
message['From'] = login_email
message['To'] = recipient
message.attach(MIMEText(message_html, "html"))
attachment = 'UML Classroom.pdf'

with open(attachment, 'rb') as att:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(att.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {attachment}")
    message.attach(part)

ctx = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', port, context=ctx) as server:
    server.login(login_email, paswrd)
    server.sendmail(login_email, recipient, message.as_string())


print('Sent')