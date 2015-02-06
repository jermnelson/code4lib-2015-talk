"""
Created:     2015/02/03
Copyright:   (c) Jeremy Nelson 2015
Licence:     GPLv3
"""
__author__ = "Jeremy Nelson"
__license__ = "GPLv3"

import smtplib
import sys
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.config.from_pyfile('config.py')

def send_contact(form):
    FROM = request.form['email']
    TO = ["jermnelson@gmail.com"]
    if 'signup' in request.form:
        SUBJECT = "SIGNUP For Catalog Pull Platform Newsletter"
    else:
        SUBJECT = "FEEDBACK from Code4Lib Lightning Talk"
    TEXT = "Comment from {}, email is {}:\n\n{}".format(
        request.form['name'],
        request.form['email'],
        request.form['comment'])
    message = """\From: {}\nTo: {}\nSubject: {}\n\n{}""".format(
        FROM,
        ",".join(TO),
        SUBJECT,
        TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(app.config.get("GMAIL_USER"), app.config.get("GMAIL_PWD"))
        server.sendmail(FROM, TO, message)
        server.close()
    except:
        print("ERROR {}".format(sys.exc_info()))
        return False
    return True



@app.route("/contact", methods=['POST'])
def contact():
    name = request.form['name']
    msg = "Thank-you {} for your interest and comments.".format(name)
    email = request.form['email']
    comment = request.form['comment']
    if 'signup' in request.form:
        signup = request.form['signup']
        msg += """You have signed up for the Catalog Pull Platform newsletter.
        You will be receiving periodic newsletter emailed to {}""".format(email)
    send_contact(request.form)
    flash(msg)
    return redirect(url_for('index'))

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

def main():
    app.run(host='0.0.0.0', port=20150, debug=True)

if __name__ == '__main__':
    main()
