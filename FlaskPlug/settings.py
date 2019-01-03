import redis


class DevConfig(object):
    DEBUG = True
    # flask-session配置
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.Redis(host='localhost', port=6379)

    # flask-SQLAlchemy配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123abc@127.0.0.1:3306/sqlalchemy?charset=utf8'
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 2
    SQLALCHEMY_TRACK_MODIFICATIONS = False





