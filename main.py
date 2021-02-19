import telebot
from bd import hello_variants

bot = telebot.TeleBot('1616118789:AAFGPYYK8zeXKMf8_04bB2RfGvklAVpvkPI')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	if message.from_user.first_name == 'Joanna💫':
		bot.reply_to(message, 'Цунаде це ти?!')
	else:
		bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	msg = message.text.lower()

	if message.from_user.first_name == 'Joanna💫':
		if msg in hello_variants:
			bot.reply_to(message, hello_variants.get(msg))
		else:
			bot.reply_to(message, 'Нихуя не понял, но очень интересно!')
	else:
		if msg == 'привет':
			bot.reply_to(message, 'Ну типа здравстуй')
		else:
			bot.reply_to(message, 'Команда не распознана...')


bot.polling()
