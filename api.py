'''
API for pep8 validator
'''


from flask import Flask, render_template, request
import json
from redis import StrictRedis
import app as myapp


app = Flask(__name__)


redis_config = {
    'host': '146.185.172.28',
    'password': 'asorGYGAhJ1ybSCrWc2l5h8mKYk',
    'port': 6379
}
redis = StrictRedis(**redis_config)


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/check_pep8', methods=['POST', 'GET'])
def check():
    if request.method == 'POST':
        code = request.form.get('code', '')
        # print(myapp.check_pep8(code))
        results = myapp.check_pep8(code)

        # REDIS
        # redis_data = redis.get(code)
        # print(redis_data)
        # if redis_data:
        #     # from redis
        #     print('from redis')
        #     results = json.loads(redis_data.decode('utf-8'))
        # else:
        #     # from app
        #     print('from app')
        #     results = myapp.check_pep8(code)
        #     redis.set(code, json.dumps(results))

        # JSON OUT
        # results = json.dumps(results)

        print(results)

        return render_template('index.html', title='Results', results=results, code=code)

    elif request.method == 'GET':
        return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run()
