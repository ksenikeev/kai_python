from flask import Flask
from flask import request

app = Flask(__name__, static_folder='static')

@app.route('/city', methods=['POST'])
def city():
    name = request.form.get('name')
    if (name and name != ''):
        jpg_name = name+'.jpg';
    else:
        jpg_name = 'alm.jpg'
    html= f'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ' \
          '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' \
          '<html><img src="/static/img/%s"></html>' % jpg_name
    return html


@app.route('/city', methods=['GET'])
def get_sity_form():
    html=f'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ' \
          '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' \
          '<html><form action="/city" method="post"><input name="name">	<input type="submit"></form></html>'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')