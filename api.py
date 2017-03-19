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


def check_ip(ip):
    '''
    '''
    if redis.exists('p'+ip):
        redis.incrby('p'+ip,1)
        redis.expire('p'+ip,10)
    else:
        redis.setex('p'+ip, 10, 1)

    if int(redis.get('p'+request.remote_addr)) < 10:
        return 1
    else:
        return 0


@app.route('/')
def index():
    '''
    '''
    # redis.delete('p'+request.remote_addr)


    # if redis.exists('p'+request.remote_addr):
    #     # count = int(redis.get('p'+request.remote_addr))
    #     # count += 1
    #     # redis.set('p'+request.remote_addr, count)
    #     redis.incrby('p'+request.remote_addr,1)
    #     redis.expire('p'+request.remote_addr,10)
    # else:
    #     # count = 1
    #     # redis.set('p'+request.remote_addr, 1)
    #     # redis.expire('p'+request.remote_addr,10)
    #     redis.setex('p'+request.remote_addr, 10, 1)

    # print_attacker()

    # if int(redis.get('p'+request.remote_addr)) < 10:
    if check_ip(request.remote_addr):
        return render_template('index.html', title='Home')
    else:
        return render_template('sorry.html', title='sorryjako'), 400


@app.route('/check_pep8', methods=['POST', 'GET'])
def check():
    '''
    '''
    if request.method == 'POST':
        # print_attacker()
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
        if check_ip(request.remote_addr):
            return render_template('index.html', title='Results', results=results, code=code)
        else:
            return render_template('sorry.html', title='sorryjako'), 400

    elif request.method == 'GET':
        # print_attacker()
        if check_ip(request.remote_addr):
            return render_template('index.html', title='Home')
        else:
            return render_template('sorry.html', title='sorryjako'), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
