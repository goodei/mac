def calc(bot,update):
	result = None
	message = update.message.text
	message = message.replace("/calc"," ").strip()
	print(message)
	clean_mes = message.replace("=","").strip()
	if message[-1] == '=':
		if "-" in message:
			a,b = clean_mes.split("-")
			result = int(a)- int(b)
		elif '+' in message:
			a,b = clean_mes.split("+")
			result = int(a) + int(b)
		elif '*' in message:
			a,b = clean_mes.split("*")
			result = int(a)* int(b)
		try:
			if "/" in message:
				a,b = clean_mes.split("/")
				result = int(a) / int(b)
		except ZeroDivisionError:
			result = ('Деление на ноль')
	bot_result = bot.sendMessage(update.message.chat_id, 'Результат : %s' % result)



