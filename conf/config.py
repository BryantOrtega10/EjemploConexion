class Config(object):
    DEBUG = False
    TESTING = False
    DBHOST = ''
    DBPORT = ''
    DBUSER = ''
    DBPASS = ''

class ProductionConfig(Config):
    DBHOST = ''
    DBPORT = ''
    DBUSER = ''
    DBPASS = ''


class DevelpmentConfig(Config):
    DEBUG = True
    DBHOST = ''
    DBPORT = ''
    DBUSER = ''
    DBPASS = ''
