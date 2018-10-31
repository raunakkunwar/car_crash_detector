import serial
import os
import sys
import smtplib
import datetime
import subprocess

from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders

msg = MIMEMultipart()
fromaddr = "pusparajthapaliya8147@gmail.com"
toaddr = "sujan.pandey6@gmail.com"
toaddr1 = "alvinpoudels@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Cc'] = toaddr1
msg['Subject'] = "Emergency Service:ALLSTATE Insurance"
body = "There is something wrong with your car at "


print('Running the program')
device = '/dev/ttyACM0' #this will have to be changed to the serial port you are using
arduino = serial.Serial(device, 9600) 
i=1
while i==1:
    data = arduino.readline()  #read the data from the arduino
    x = data.decode()
    q =len(x)
    if q== 17:
        os.system("sh camera.sh")
        RT = datetime.datetime.now()
        Tx_string = RT.strftime("%I:%M%p on %B %d %Y")
        body = body + Tx_string
        body = body + ". We are sending emergency services immediately to help you. \n \n Sincerely,\n AllState Insurance."
        msg.attach(MIMEText(body, 'plain'))
        im = "image.jpg"
        img_data = open(im, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(im))
        msg.attach(image)
        f_vid = "output.mp4"
        part = MIMEBase('application',"octet-stream")
        vid_data =open(f_vid,"rb")
        part.set_payload(vid_data.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f_vid))
        msg.attach(part)

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.connect("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, "Nepal9845@")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.sendmail(fromaddr, toaddr1, text)
        server.quit()
        break
        
    
        


