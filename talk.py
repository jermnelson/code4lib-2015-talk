"""
Created:     2015/02/03
Copyright:   (c) Jeremy Nelson 2015
Licence:     GPLv3
"""
__author__ = "Jeremy Nelson"
__license__ = "GPLv3"

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/contact", methods=['POST'])
def contact():
    return "IN Contact"
##    return redirect(url_for('index'))

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

def main():
    app.run(host='0.0.0.0', port=20150, debug=True)

if __name__ == '__main__':
    main()
