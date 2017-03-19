'''
API for pep8 validator
'''


from flask import Flask, render_template, request
import json
from redis import StrictRedis
import app as myapp
import time

app = Flask(__name__)


redis_config = {
    'host': '146.185.172.28',
    'password': 'asorGYGAhJ1ybSCrWc2l5h8mKYk',
    'port': 6379
}
redis = StrictRedis(**redis_config)


def print_attacker():
    '''
    '''
    # print(request.headers)
    print('>', request.remote_addr, int(redis.get('p'+request.remote_addr)), request.headers.get('User-Agent'), sep='  ')


@app.route('/')
def index():
    '''
    '''
    # redis.delete('p'+request.remote_addr)
    # print(time.localtime)
    redis_data = redis.get('p'+request.remote_addr)
    if redis_data:
        count = int(redis_data)
        count += 1
        redis.set('p'+request.remote_addr, count)
    else:
        count = 1
        redis.set('p'+request.remote_addr, count)

    print_attacker()

    if count < 10:
        return render_template('index.html', title='Home')
    else:
        return render_template('sorry.html', title='sorryjako')


@app.route('/check_pep8', methods=['POST', 'GET'])
def check():
    '''
    '''
    if request.method == 'POST':
        print_attacker()
        code = request.form.get('code', '')
        warnings = request.form.get('warnings', '')
        # print(myapp.check_pep8(code))
        results = myapp.check_pep8(code, warnings)

        # REDIS
        redis_data = redis.get(code)
        # print(redis_data)
        if redis_data:
            # from redis
            print('from redis')
            results = json.loads(redis_data.decode('utf-8'))
        else:
            # from app
            print('from app')
            results = myapp.check_pep8(code, warnings)
            redis.set(code, json.dumps(results))

        # JSON OUT
        # results = json.dumps(results)

        # print(results)
        return render_template('index.html', title='Results', results=results, code=code)

    elif request.method == 'GET':
        print_attacker()
        return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
