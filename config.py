import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andrew:12345@localhost/pitpa'
    SECRET_KEY='DJYJGSJHDH'
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}