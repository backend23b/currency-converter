from flask import Flask, request, jsonify
import currencyapicom
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.environ.get('API_KEY')
client = currencyapicom.Client(API_KEY)


app = Flask(__name__)


@app.route('/api/v1/convert/', methods=['GET'])
def to_usd():

    # get params
    params = request.args

    amount = float(params.get('amount'))   # 100 usd
    base = params.get('base')

    # convert
    result = client.latest(base, currencies=['UZS','EUR', 'USD', 'RUB'])
    
    data = result.get('data')
   
    ans = [
        {
            'currency': 'UZS',
            'value': data['UZS']['value'] * amount
        },
        {
            'currency': 'EUR',
            'value': data['EUR']['value'] * amount
        },
        {
            'currency': 'USD',
            'value': data['USD']['value'] * amount
        },
        {
            'currency': 'RUB',
            'value': data['RUB']['value'] * amount
        },
    ]

    return jsonify(ans)

if __name__ == '__main__':
    app.run(debug=True)    