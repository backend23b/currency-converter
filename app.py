from flask import Flask, request, render_template

app = Flask(__name__)

usd = 11380.7 # 1 USD = 11380.7 UZS


@app.route('/')
def home():
    return  '<h1>Home</h1>'



@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    params = request.args
    amount = params.get('amount')
    converted = float(amount) / usd
    data = {
        'amount': float(amount),
        'currency': 'UZS',
        'converted': round(converted, 2),
        'convertedCurrency': 'USD'
    }
    return render_template('index.html', data=data)

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    params = request.args
    amount = params.get('amount')
    converted = float(amount) * usd
    data = {
        'amount': float(amount),
        'currency': 'USD',
        'converted': round(converted, 2),
        'convertedCurrency': 'UZS'
    }
    return render_template('index.html', data=data)
    

if __name__ == '__main__':
    app.run(debug=True)    