import requests
import pandas


class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query?'

    def fetch_quote(self, symbol):
        url = f'{self.base_url}function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data['Global Quote']

    def fetch_currency_exchange_rates(self, currencies):
        exchange_rates = []

        for currency in currencies:
            params = {
                'function': 'CURRENCY_EXCHANGE_RATE',
                'from_currency': 'USD',
                'to_currency': currency,
                'apikey': self.api_key
            }

            response = requests.get(self.base_url, params=params)
            data = response.json()

            try:
                exchange_rate_data = data['Realtime Currency Exchange Rate']
                exchange_rates.append({
                    'Currency': currency,
                    'Exchange Rate': exchange_rate_data['5. Exchange Rate'],
                    'Last Refreshed': exchange_rate_data['6. Last Refreshed']
                })
            except KeyError:
                print(data)
        return pandas.DataFrame(exchange_rates)
