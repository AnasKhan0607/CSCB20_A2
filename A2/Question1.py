from distutils.log import debug
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/<name>")
def user(name):
    if not name.isalpha():
        only_letters = ""
        for c in name:
            if c.isalpha():
                only_letters += c
        return f'<h1>Welcome, {only_letters.strip()}, to my CSCB20 website!<h1>'
    elif name.islower():
        return f'<h1>Welcome, {name.upper().strip()}, to my CSCB20 website!<h1>'
    elif name.isupper():
        return f'<h1>Welcome, {name.lower().strip()}, to my CSCB20 website!<h1>'
    else:
        return f'<h1>Welcome, {name.strip().capitalize()}, to my CSCB20 website!<h1>'


if __name__ == '__main__':
    app.run(debug=True)
