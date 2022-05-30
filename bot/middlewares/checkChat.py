from telebot.handler_backends import SkipHandler

# TODO: Я не понял почему не работает SkipHandler в function_based middleware? Как это реализовать не используя class_based middleware?


def checkChatType(bot, message):
    if message.chat.type != 'private':
        bot.reply_to(
            message, 'Данный бот работает только в личных чатах, используйте команду /help для получения информации')
        return SkipHandler()
