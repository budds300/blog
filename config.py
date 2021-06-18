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
    
    