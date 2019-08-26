import smtplib
import imaplib
import time
import email


class Mail:
    def __init__(self,email,password):
        self.server=''
        self.smtpPort = 993
        self.email = email
        self.password = password

    def readMail(self):
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            print(self.email,self.password)
            mail.login(self.email, self.password)
            mail.select('inbox')

            mtype, data = mail.search(None, 'FROM','ff21-RRS@ff21.com')
            print("Mail types = ",mtype)
            print("Mail data = ",data)
        except Exception as e:
            print("Error = ",e)

if __name__ == "__main__":
    mail = Mail("adhikaribipul00@gmail.com","bibishaisted")
    mail.readMail()
