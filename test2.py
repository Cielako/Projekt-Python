from urllib import request,urlopen

def raport_mail(target):
    from smtplib import SMTP
    from email.mime.text import MIMEText
    
    msg = MIMEText('tresc_wiadomosci')
    msg['Subject'] = 'tytuł_maila'
    msg['From'] = 'od_kogo'
    msg['To'] = 'do_kogo'
    
    server = SMTP('smtp.gmail.com:587')
    server.starttls()# Podłączenie do serwera SMTP
    server.login('login','hasło')
    server.sendmail('moj_mail',['adres_odbiorcy'],msg.as_string())
    server.quit()
    return 'Mail został wysłany'