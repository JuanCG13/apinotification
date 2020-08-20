# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def MailNotification(message):
    # create message object instance
    msg = MIMEMultipart()
    
    # setup the parameters of the message
    password = "zwkyzdgmypfpyhqm"
    msg['From'] = "linkstartv2.0@gmail.com"
    destino = ['jjlocoxdlol@gmail.com','marcelomellone2@gmail.com','willi1997.1@gmail.com']
    # msg['To'] = "jjlocoxdlol@gmail.com"
    msg['Subject'] = "Subscription"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], destino, msg.as_string())
    
    server.quit()
    
    print("successfully sent email to %s:" % (destino))