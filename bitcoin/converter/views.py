# converter/views.py

from django.shortcuts import render
import requests

def bitcoin_converter(request):
    if request.method == 'POST':
        # Get the number from the form
        btc_amount = request.POST.get('btc_amount')

        # Fetch data from the API
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        bitcoin_data = response.json()

        # Extract relevant data
        usd_rate = bitcoin_data['bpi']['USD']['rate_float']
        inr_rate = usd_rate * 74.67  
        rub_rate = usd_rate * 74.93  

        # Convert Bitcoin amount to USD, INR, and RUB
        usd_value = float(btc_amount) * usd_rate
        inr_value = float(btc_amount) * inr_rate
        rub_value = float(btc_amount) * rub_rate

        # Set session expiry time to 1 second
        request.session.set_expiry(2)

        # Render template with data
        return render(request, 'converter/bitcoin_converter.html', {
            'usd_value': usd_value,
            'inr_value': inr_value,
            'rub_value': rub_value
        })
    else:
        return render(request, 'converter/bitcoin_converter.html')

