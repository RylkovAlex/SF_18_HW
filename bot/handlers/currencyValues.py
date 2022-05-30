from telebot import types
from config import CURRENCIES


def valuesHandler(bot, message: types.Message):
  try:
        text = 'Доступные для ковертации валюты:\n\n'
        if len(CURRENCIES.keys()) == 0:
          text = 'Нет валют, доступных для конвертации'
        else:
          for cur in CURRENCIES:
            text += f'{cur} (<b>{CURRENCIES[cur]}</b>)\n'

  except Exception as error:
    bot.reply_to(message, f'Не удалось обработать команду!\n {error}')
  else:
    bot.reply_to(message, text)
