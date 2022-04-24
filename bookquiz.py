# Biography Interest Survey

title = '======================================\nWHAT KIND OF BIOGRAPHY SHOULD I READ?\n======================================\n'

def startQuiz():
	print(title + '\nThis quiz will help you choose a biography to read! Respond to each question with your letter choice and then press Enter. Either uppercase or lowercase will work.\n')
	start = input('Are you ready to begin? (yes/no)\n>')
	if start.lower() == 'yes':
		questions()
	else:
		return 'All done!'

def questions():
	responses = []
	
	answer = input('\nQuick! Pick a color:\n\nA. Red\nB. Orange\nC. Purple\nD. Yellow\nE. Green\nF. Blue\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nWhere would you most like to go on a trip\n\nA. Washington D.C.\nB. Wrigley Field\nC. Mt. Everest\nD. The Metropolitan Muesum of Art\nE. Broadway\nF. Kennedy Space Center\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nPick a famous person:\n\nA. Greta Thunberg (activist)\nB. Serena Williams (tennis player)\nC. Simone Biles (gymnast)\nD. Amanda Gorman (poet)\nE. Olivia Rodrigo (singer)\nF. Jane Goodall (scientist)\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nWhat is your favorite kind of shoe?\n\nA. Whatever looks best with what I am wearing\nB. Running shoes\nC. Barefoot\nD. Something different from what others are wearing\nE. Anything as long as it looks cool\nF. Hiking Boots\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nWhat is your goal in middle school?\n\nA. To get all As\nB. To make the A team\nC. To get more involved\nD. To make new friends\nE. To be the class clown\nF. To learn something new\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nPick a type of TikTok account to follow:\n\nA. Awareness\nB. Trick shot\nC. Workout\nD. Aesthetic\nE. Dance\nF. Travel\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nWhich landscape is most inspiring?:\n\nA. Mountains\nB. Open road\nC. Ocean\nD. Flower fields\nE. City streets\nF. Night sky\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nWhat is your favorite subject in school?\n\nA. Science\nB. Math\nC. Social Studies\nD. Language Arts\nE. Music\nF. Tech\n\nYour Answer: ')
	responses.append(answer.lower())

	# pick a book based off its cover 

	answer = input('\nWhat kind of technology is a must-have for you?\n\nA. Social media\nB. Gaming system\nC. Internet\nD. Pencil\nE. Camera\nF. VR Tech\n\nYour Answer: ')
	responses.append(answer.lower())

	answer = input('\nPick an ice cream flavor:\n\nA. Birthday cake\nB. Cookies and cream\nC. Superman\nD. Gelato or sorbet\nE. Cookie dough\nF. Rocky road\n\nYour Answer: ')
	responses.append(answer.lower())

	# print(responses)
	getResults(responses)
	

def getResults(responses):
	letterCounts = {}
	letterCounts['a'] = responses.count('a')
	letterCounts['b'] = responses.count('b')
	letterCounts['c'] = responses.count('c')
	letterCounts['d'] = responses.count('d')
	letterCounts['e'] = responses.count('e')
	letterCounts['f'] = responses.count('f')

	# print(letterCounts)

	# get highest response count
	max = 0
	for key, value in letterCounts.items():
		if value > max:
			max = value

	# get top choice key(s) based on highest value
	topChoice = []
	for key, value in letterCounts.items():
		if value == max:
			topChoice.append(key)

	printResults(topChoice)		
		
	
def printResults(topChoice):
	results_strings = {
		'a': 'people who LEAD',
		'b': 'people who COMPETE',
		'c': 'people who INSPIRE',
		'd': 'people who CREATE',
		'e': 'people who PERFORM',
		'f': 'people who EXPLORE or INNOVATE'
	}

	tie_str = '\nIt was a tie! You should read about '
	for choice in topChoice:
		for key, value in results_strings.items():
			if len(topChoice)==1 and key==choice:
				# no tie
				print(f'\nYou chose mostly {topChoice[0].upper()}s. You should read about {value}!\n')
			elif key==choice:
				# yes tie
				tie_str += value + ' or '
	
	if len(topChoice) > 1:
		# cut off the last 'or' of the tie string
		print(tie_str[0:len(tie_str)-3] + '!\n')

	restart = input('Do you want to retake the quiz? (yes/no)\n>')
	if restart.lower() == 'yes':
		startQuiz()
	else:
		return 'All done!'
						
	
# START THE QUIZ!
startQuiz()