import os

class Config():
    
    SECRET_KEY = '0443'

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'brianmuchera4@gmail.com'
    MAIL_PASSWORD = 'shitakwaaa8*'

    

    @staticmethod   
    def init_app(app):
        pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchera-brian:brian@localhost/blogs'
    DEBUG = True

class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchera-brian:brian@localhost/blogs'

config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}