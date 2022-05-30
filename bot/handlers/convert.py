from telebot import types
from extensions import APIException
from extensions import CurrencyConverter
from config import CURRENCIES

converter = CurrencyConverter(CURRENCIES)


def convertHandler(bot, message: types.Message):
    try:
        args = list(map(lambda s: s.strip().upper(), message.text.split(' ')))
        if len(args) != 3:
            raise APIException(f'Не достаточно аргументов для выполнения ковертации')
        to, from_, amount = args
        tickerFrom = converter.getTicker(from_)
        tickerTo = converter.getTicker(to)
        price = converter.get_price(tickerFrom, tickerTo, amount)
    except APIException as error:
        bot.reply_to(message, f'Ошибка ввода:\n{error}')
    except Exception as error:
        bot.reply_to(message, f'Ошибка обработки команды\n{error}')
    else:
        bot.reply_to(message, f'{amount} {tickerTo} = {price} {tickerFrom}')
