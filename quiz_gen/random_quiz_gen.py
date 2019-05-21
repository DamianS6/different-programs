# random_quiz_gen.py - Create geography quizzes with questions and answers
# in random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
	'Albania': 'Tirana',
	'Andorra': 'Andorra la Vella',
	'Austria': 'Vienna',
	'Belarus': 'Minsk',
	'Belgium': 'Brussels',
	'Bosnia And Herzegovina': 'Sarajevo',
	'Bulgaria':	'Sofia',
	'Croatia':	'Zagreb',
	'Cyprus':	'Nicosia',
	'Czech Republic':	'Prague',
	'Denmark':	'Copenhagen',
	'Estonia':	'Tallinn',
	'Faroe Islands':	'Tórshavn',
	'Finland':	'Helsinki',
	'France':	'Paris',
	'Germany':	'Berlin',
	'Gibraltar':	'Gibraltar',
	'Greece':   'Athens',
	'Guernsey':	'St. Peter Port',
	'Hungary':  'Budapest',
	'Iceland':	'Reykjavik',
	'Ireland':	'Dublin',
	'Isle Of Man':	'Douglas',
	'Italy':	'Rome',
	'Jersey':	'Saint Helier',
	'Kosovo':	'Pristina',
	'Latvia':   'Riga',
	'Liechtenstein':    'Vaduz',
	'Lithuania': 'Vilnius',
	'Luxembourg': 'Luxembourg',
	'Macedonia': 'Skopje',
	'Malta':	'Valletta',
	'Moldova':	'Chișinău',
	'Monaco':	'Monaco',
	'Montenegro':	'Podgorica',
	'Netherlands':	'Amsterdam',
	'Norway':   'Oslo',
	'Poland':	'Warsaw',
	'Portugal':	'Lisbon',
	'Romania':	'Bucharest',
	'Russia':	'Moscow',
	'San Marino':	'City of San Marino',
	'Serbia':	'Belgrade',
	'Slovakia':	'Bratislava',
	'Slovenia':	'Ljubljana',
	'Spain':	'Madrid',
	'Sweden':	'Stockholm',
	'Switzerland':	'Bern',
	'Ukraine':	'Kiev',
	'United Kingdom':	'London',
	'Vatican City':	'Vatican City',
}

# Generate 35 quiz files.
for quiz in range(35):
	# Create the quiz and answer key files.
	quizfile = open(f'capitalsquiz{quiz + 1}.txt', 'w')
	answerkeyfile = open(f'capitalsquiz_answers%s.txt' % (quiz + 1), 'w')

	# Write out hte header for the quiz.
	quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizfile.write((' ' * 20) + 'European Capitals Quiz (Form %s)\n\n' % (quiz + 1))

	# Shuffle the order of the states.
	countries = list(capitals.keys())
	random.shuffle(countries)

	# Loop through all 50 states, making a question for each.
	for question_num in range(50):

		# Get right and wrong answers.
		correct = capitals[countries[question_num]]
		wrongs = list(capitals.values())
		del wrongs[wrongs.index(correct)]
		wrongs = random.sample(wrongs, 3)
		answer_options = wrongs + [correct]
		random.shuffle(answer_options)

		# Write the question and answer options to the quiz file.
		quizfile.write(f'{question_num + 1}. What is the capital '
		               f'of {countries[question_num]}?\n')
		for i in range(4):
			quizfile.write(f'   {"ABCD"[i]}. {answer_options[i]}\n')
		quizfile.write('\n')

		# Write the answer key to a file.
		answerkeyfile.write('%s. %s\n' % (question_num + 1, 'ABCD'[
			answer_options.index(correct)]))
	quizfile.close()
	answerkeyfile.close()
