import random
import smtplib
otp=''.join([str(random.randint(0,9)) for i in range(4)])
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('munukutlavranusha@gmail.com','xbaj tjfl wbjg gydi')
msg='your otp is'+str(otp)
server.sendmail('munukutlavranusha@gmail.com','edusolutions22@gmail.com',msg)
server.quit()
