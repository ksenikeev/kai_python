from flask import Flask

app = Flask(__name__, static_folder='static')

@app.route('/city', methods=['POST', 'GET'])
@app.route('/city/<name>', methods=['POST', 'GET'])
def city(name='alm'):

    jpg_name = name+'.jpg';

    html= f'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ' \
          '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' \
          '<html><img src="/static/img/%s"></html>' % jpg_name
    return html;


if __name__ == '__main__':
    app.run(host='0.0.0.0')