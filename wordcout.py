
def word_count(bot,update):
	#import re
	check = "[\"'!@#$%^&*()_+]"
	message = ''
	for i in update.message.text:
		if i not in check:
			message += i
			print(message)
	"""while message.find("  ") > -1:
		message.replace("  "," ")"""

	message = len(message.strip().split()) - 1
	our_message = "Колличество слов в сообщении : %s" % message
	"""if re.search(check , message):
		check.replace()"""
	bot.sendMessage(update.message.chat_id , our_message)


