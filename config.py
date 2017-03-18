'''
Script for redis configuration
'''

from redis import StrictRedis

redis_config = {
    'host': '146.185.172.28',
    'password': 'asorGYGAhJ1ybSCrWc2l5h8mKYk',
    'port': 6379
}
redis = StrictRedis(**redis_config)





def main():



if __name__ == '__main__':
    main()
