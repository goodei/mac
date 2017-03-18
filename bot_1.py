

def get_answer(operator):
	operator = str(operator)
	operator = operator.lower()			
	answers = {'hello' : 'Same hi!', 'how are you?' : 'Fine!', 'bye' : 'see u later', }
	word = answers.get(operator,'I dont understand you')
	return word
	question = str(input('Hi,what is your question?:'))
	print(get_answer(question))