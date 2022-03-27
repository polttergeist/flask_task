from flask import Flask, render_template, url_for, make_response, request
from base64 import b64encode, b64decode
import xml.etree.ElementTree as ET
from lxml import etree

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.cookies.get('data') == None:
        pass
    else:
        data = b64decode(request.cookies.get('data'))
        tree = etree.fromstring(data)
        return other_render(tree[0].text, tree[1].text, data)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        gxml = f'<?xml version="1.0" encoding="UTF-8"?><form><email>{email}</email><password>{password}</password></form>'
        bgxml = bytes(gxml, 'utf-8')
        return other_render(email, password, bgxml)

    return render_template("index.html")


def other_render(a, b, c):
    res = make_response(render_template("other.html", email=a, password=b))
    coo = b64encode(c)
    res.set_cookie('data', coo.decode('utf-8'))
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


