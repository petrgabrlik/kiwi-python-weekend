'''
API for pep8 validator
'''


from flask import Flask, render_template, request
import json
import redis
import app as myapp


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/check_pep8', methods=['POST', 'GET'])
def check():
    if request.method == 'POST':
        code = request.form.get('code', '')
        results = myapp.check_pep8(code)

        json_out = json.dumps(results)
        # json_out = request.form.get('json_output', False)
        print(json_out)

        return render_template('index.html', title='Results', results=results, code=code)
    else:
        return render_template('index.html', title='Results', results=results, code=code)


if __name__ == '__main__':
    app.run()
