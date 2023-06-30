import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = "miguel.carcamo@tegraglobal.com"
password = "Naruto04.."
mail_from = "miguel.carcamo@tegraglobal.com"
mail_to = ["miguel.carcamo@tegraglobal.com","osman.mendez@tegraglobal.com", "ludin.castro@tegraglobal.com"]
mail_subject = "Test send mail"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to[0]
mimemsg['To']=mail_to[1]
mimemsg['To']=mail_to[2]
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()

