import currencyapicom
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.environ.get('API_KEY')
client = currencyapicom.Client(API_KEY)


result = client.latest('USD',currencies=['EUR','AUD'])
