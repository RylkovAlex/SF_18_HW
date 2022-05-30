import requests
import json


class APIException(Exception):
    pass


class CurrencyConverter():
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise APIException(
                f'Не возможно осуществить конвертацию одинаковых валют')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(
                f'Не удалось распознать количество валюты: {amount}')

        response = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        if response.status_code != 200:
            raise Exception(
                f'Проблемы при конвертации через min-api.cryptocompare.com')
        return round(float(json.loads(response.content)[quote]) * float(amount), 2)

    def __init__(self, currencies):
        self.currencies = currencies

    def getTicker(self, currencyName):
        currencyName = currencyName.upper()
        ticker = self.currencies[currencyName] if currencyName in self.currencies.keys(
        ) else currencyName if currencyName in self.currencies.values() else None
        if ticker:
            return ticker
        raise APIException(f"Ошибка в имени валюты: {currencyName}")
