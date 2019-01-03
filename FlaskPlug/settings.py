import redis


class DevConfig(object):
    DEBUG = True
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='localhost', port=6379)






