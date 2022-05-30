from telebot import apihelper, TeleBot
from functools import partial, update_wrapper

class Bot():
    def __init__(self, *args, **kwargs):
        apihelper.ENABLE_MIDDLEWARE = True
        self.bot = TeleBot(*args, **kwargs)

    def run(self):
        self.bot.polling(non_stop=True)

    def addMessageHandler(self, handler, **filters):
        self.bot.message_handler(**filters)(partial(handler, self.bot))

    def addMiddleWare(self, handler, update_types):
      self.bot.middleware_handler(update_types)(update_wrapper(handler, self.bot))
