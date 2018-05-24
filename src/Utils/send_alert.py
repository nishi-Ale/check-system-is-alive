import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import src.Utils.read_inputfile as read_ini


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs,passwd, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(from_addr, passwd)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


def send_email(target_location, target_user):

    alert_settings = read_ini.read_setting_for_alert(target_user)

    to_addr = alert_settings['to']
    subject = alert_settings['subject']
    body = alert_settings['body'] + '\n' + '該当箇所： ' + target_location

    msg = create_message(alert_settings['from'], to_addr, alert_settings['bcc'], subject, body)
    send(alert_settings['from'], to_addr,alert_settings['pass'], msg)


if __name__ == '__main__':
    pass
