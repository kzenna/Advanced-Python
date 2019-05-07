# Домашнее задание к лекции 1.5
# «PEP8 и PEP»
#
# Кокурникова Лилия Фаритовна, 22.04.19
#

import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"
PORT_SMTP = 587


class EmailSendReceive:
    def __init__(self, login_mail, password):
        self.login_mail = login_mail
        self.password = password

    def send_email(self, adress_to, subject, message):
        msg = MIMEMultipart()
        msg['From'] = login_mail
        msg['To'] = adress_to
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(GMAIL_SMTP, PORT_SMTP)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(login_mail, password)
        ms.sendmail(login_mail, ms, msg.as_string())
        ms.quit()

    def receive_email(self):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(login_mail, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert (data[0]), "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        _ = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    login_mail = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    EmailSendReceive(login_mail, password)