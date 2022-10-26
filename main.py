import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

YOUR_EMAIL = " -- YOUR EMAIL ID -- "
PASSWORD = " -- YOUR PASSWORD -- "  # In case of gmail, you need to enable 2 factor authentication and then get an app password which will unique for this script

receiver = " -- RECEIVERS EMAIL ID -- "

msg = MIMEMultipart()
msg['Subject'] = ' -- SUBJECT OF THE EMAIL -- '
msg['From'] = ' -- THE NAME WHICH YOU WANT THE EMAIL TO GO WITH -- '
msg['To'] = receiver

body = " -- BODY OF THE EMAIL -- "

msgText = MIMEText('<b>%s</b>' % (body), 'html')
msg.attach(msgText)

with open(' -- PATH OF THE IMAGE FILE YOU WANT TO ATTACH -- ', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename=" -- NAME OF THE ATTACHMENT -- ")
    msg.attach(img)

try:
    with smtplib.SMTP(' -- EMAIL PROVIDERS SMTP SERVER -- ' , 587) as smtp:  # In case of gmail, it is - smtp.gmail.com
        smtp.ehlo()
        smtp.starttls()
        smtp.login(YOUR_EMAIL, PASSWORD)
        smtp.sendmail(YOUR_EMAIL, receiver, msg.as_string())
except Exception as e:
  print(e)
