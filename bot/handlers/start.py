from telebot import types


def startHandler(bot, message: types.Message):
    try:
        bot.send_message(message.chat.id, f'''Привет{' ' + message.chat.username + '!' or '!'} Я умею быстро ковертировать валюты, список доступных валют выдаю по команде /values а для осуществления конвертации отправьте мне сообщение в виде:

<b>&lt;валюта, цену которой хотите узнать&gt; &lt;валюта в которой надо вывести цену первой валюты&gt; &lt;количество первой валюты&gt;</b>

<b>Пример:</b> <i>USD RUB 100</i>''')
    except Exception as error:
        bot.reply_to(message, f'Ошибка обработки команды /start\n {error}')
