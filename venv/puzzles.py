from random import shuffle

class MultipleChoice(object):
	def __init__(self, question, correctAnswer, WrongAnswer1, WrongAnswer2, WrongAnswer3):
		self.question = question
		self.correctAnswer = correctAnswer
		self.WrongAnswer1 = WrongAnswer1
		self.WrongAnswer2 = WrongAnswer2
		self.WrongAnswer3 = WrongAnswer3

		self.answers = [self.correctAnswer, self.WrongAnswer1, self.WrongAnswer2, self.WrongAnswer3]
		shuffle(self.answers)


	def trivia(self):
		counter = 0
		for answers in self.answers:
			if self.correctAnswer == answers:
				break
			else:
				counter +=1
		print(self.question)
		print('a)'+ self.answers[0] + '		b)' + self.answers[1] + '	c)' + self.answers[2] + '	d)' + self.answers[3])
		choice = input('Selection:')
		if choice.lower() == 'a':
			choice = 0
		elif choice.lower() == 'b':
			choice = 1
		elif choice.lower() == 'c':
			choice = 2
		elif choice.lower() == 'd':
			choice = 3
		else:
			print("False!")
			return

		if choice == counter:
			print("Fact!")
		else:
			print("False!")




puzzle1 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle2 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle3 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle4 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle5 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle6 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle7 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle8 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle9 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")
puzzle10 = MultipleChoice("Question: What kind of bear is best", "False: Black Bear", "That's a ridiculous question", "Polar bear", "Mama bear")


'''Question: What kind of bear is best?
How many toes do you have? 10, 9, 0
What is Merideths son's name? Jake'
Who is the last person to steal from you? William Charles Schnider
What element is the most important in the growth of paper, phosphours right?
Boboddy. What does the first "b" stand for?
Where does Phyllis' husband work'''

puzzle = {
	1:puzzle1,
	2:puzzle2,
	3:puzzle3,
	4:puzzle4,
	5:puzzle5,
	6:puzzle6,
	7:puzzle7,
	8:puzzle8,
	9:puzzle9,
	10:puzzle10
}
'''
	11:
	12:
	13:
	14:
	15:
	16:
	17:
	18:
	19:
	20:
	21:
	22:
	23:
	24:
	25:
	26:
	27:
	28:
	29:
	30:
	31:
	32:
	33:
	34:
	35:
	36:
	37:
	38:
	39:
	40:
	41:
	42:
	43:
	44:
	45:
	46:
	47:
	48:
	49:
	50:
 	}
'''
