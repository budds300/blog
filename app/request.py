import requests
from .models import Quote

#Getting the Quote base url
base_url = None

def configure_request(app):
    global base_url
    base_url= app.config['QUOTES_API_URL']
    
def get_quotes():
    ''' 
    function gets the json response to our url
    '''
    get_quotes_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    print(get_quotes_response)
    
    return get_quotes_response