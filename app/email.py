from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(Subject, template, to,**kwargs ):
    sender ='brianmuchera4@gmail.com'

    email = Message(Subject,sender = sender, recipients=[to])
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.txt', **kwargs)
    mail.send(email)