'''
API for pep8 validator
'''


from flask import Flask
from flask import render_template
import app as myapp


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


# @app.route('/check_pep8', methods='POST')
# def check():
#     pass



if __name__ == '__main__':
    app.run()
