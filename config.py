import os

class Config:
    '''
    General configurations parent
    '''
    QUOTES_API_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY= os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST= 'app/static/photos'
    
     #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    class ProdConfig(Config):
     '''
    Production configuration child class
    
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False

class TestConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'Test':TestConfig
}