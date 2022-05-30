import environ

from bot.handlers.start import startHandler
from bot.handlers.convert import convertHandler
from bot.handlers.currencyValues import valuesHandler
from bot.middlewares.checkChat import checkChatType
from bot.bot import Bot

env = environ.Env()
environ.Env.read_env()

bot = Bot(env('BOT_TOKEN'), parse_mode='HTML')
bot.addMessageHandler(startHandler, commands=['start', 'help'])
bot.addMessageHandler(valuesHandler, commands=['values'])
bot.addMessageHandler(convertHandler, content_types=['text'])
bot.addMiddleWare(checkChatType, update_types=['message'])
bot.run()
