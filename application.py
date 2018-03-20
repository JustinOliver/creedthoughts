#!python3
# CreedThoughts.py - A text based adventure puzzle game based on the life of Creed

import random
import sys
from time import sleep
from characters import *
from quotes import *
from puzzles import *
from scenes import *


# Define variables to be used during game.

puzzlesSolved = 0

'''
def chooseCharacter():
	while True:
		try:
			choice = int(input("1. Warrior\n2. Wizard\n3. Archer\nEnter the number of your choice now!:"))
			if choice == 1:
				character = warrior

			elif choice == 2:
				character = wizard

			elif choice == 3:
				character = archer
			else:
				continue

		except ValueError:
			continue
		else:
			break
	sleep(.2)
	print("Good choice my friend, you are a ", character.name)
	return character



def inventoryShow():
	if len(inventory) == 0:
		sleep(.2)
		print("Your inventory is empty")
		return
	else:
		sleep(.2)
		print("You have the following in your inventory..." + str(inventory))
		return


def lootCheck(loot):
	if loot in inventory:
		sleep(.2)
		print("You already have this item, so you leave it for another adventurer!")
		return
	else:
		inventory.append(loot)
		return

def useItem():
	y = rarity0.health
	sleep(.2)
	x = input("Are you sure you want to use " + y + "? Enter yes or no:\n")
	sleep(.2)
	if x.lower() == "yes":
		if y in inventory:
			print("You have increased your " + y + " by " + str(rarity0.score) + " points!")
			character.health += rarity0.score
			inventory.remove(y)
		else:
			print("You don't have " + y + "in your inventory silly pants!")
			return

	elif x.lower() == "no":
		print("Okay, we won't use that.")
		return
	else:
		print("I didn't understand your input, so we are going  to put that item away. Carry on my wayward son!")
		return



def loot(enemy):
	x= random.randint(1, 4)
	#if x == 0:
	loot = rarity0.health
	#elif x == 1:
	#	loot = rarity + str(enemy.rarity) + '.defense'
	#elif x == 2:
	#	loot = rarity + str(enemy.rarity) + '.attack'
	#elif x == 3:
	#	loot = 'rarity' + str(enemy.rarity) + '.ranged'
	#else:
	#	print("no loot for you, something happened")
	#	return
	#loot1 = loot
	sleep(.2)
	print("The enemy has dropped a...", loot)
	lootCheck(loot)
'''
def decision(ver, a, b, c):
	while True:
		try:
			decision = input("a)" + a +	"	b)" + b + "		c)" + c + "\nSelection: ")
			if decision.lower() == 'a':
				print(quote[ver])
			elif decision.lower() == 'b':
				#print(puzzle1.question)
				x = puzzle[ver].trivia
				if callable(x):
					x()
				else:
					print('I\'m headed back to my desk to eat some mungbeans')
			elif decision.lower() == 'c':
				print(3)#scenes(ver)
			else:
				sleep(.2)
				print("I didn't get that, lets try again. Push ctrl+c to exit the game at anytime")
				continue
		except ValueError:
			continue
		else:
			break


def feeling():
	while True:
		try:
			feeling = input("a) Groovy	b) Where am I? 	c) I pay for this privilege\nSelection: ")
			if feeling.lower() == 'a':
				print('Yea baby')
			elif feeling.lower() == 'b':
				print('Dunder Mifflin')
			elif feeling.lower() == 'c':
				print('What does that even mean?')
			else:
				sleep(1)
				print("Don't be a dummy Creed, enter either \'a\' \'b\' or \'c\'")
				continue
		except ValueError:
			continue
		else:
			break
'''
def attack():
	sleep(.2)
	attackMethod = int(input("1. Sword\n2. Magic\n3. Ranged\n What weapon would you like to attack with?: "))
	if attackMethod == 1:
		sleep(.2)
		print("Lets attack with the sword!")
		return "sword"
	elif attackMethod == 2:
		sleep(.2)
		print("Alright Harry, let's use some magic")
		return "magic"
	elif attackMethod == 3:
		sleep(.2)
		print("Lets use a ranged attack!")
		return "ranged"
	else:
		sleep(.2)
		print("I didn't get that, lets try again. Push ctrl+c to exit the game at anytime")
		attack()





def battlestate():
	global enemyKills
	while True:
		battleState = 1
		enemy = villains[random.randint(0, 3)]
		attackList = [character.attack, character.magic, character.ranged]
		sleep(.2)
		print("You see an enemy coming from a distance...")
		sleep(.2)
		print("It's a ", enemy.name, "!!!")
		sleep(.2)
		print(enemy.intro)
		sleep(.2)
		print("Get ready to fight!!!")
		result = decision()

		if result == "run":
			sleep(.2)
			print("You ran away, nice job!")
			sys.exit()
		if result == "attack":
			sleep(.2)
			print("You have 3 attack options...\n")
			attackMethod = attack()

		while battleState == 1:
			miss = random.randint(0,10)
			if miss > 8:
				sleep(.2)
				print("Your attack missed!")
				sleep(.2)
				print("the enemy attacks!")
				sleep(.2)
				print("The", enemy.name, " takes a swipe")
				sleep(.2)
				damage = round(enemy.attack/character.defense, 2)
				character.health = character.health - damage
				sleep(.2)
				print("The remaining health is...", character.health)
				sleep(.2)
				if character.health < 1:
					sleep(.2)
					print("The hero has died!!!!")
					sys.exit()

			else:
				if attackMethod == "sword":
					damage = round(attackList[0] / enemy.defense, 2)
					sleep(.2)
					print("You swing your sword and do...", damage, "damage")
					enemy.health = enemy.health - damage
					sleep(.2)
					print("Enemy health remaining:", enemy.health)

					if enemy.health <1:
						sleep(.2)
						print("you have defeated the", enemy.name)
						sleep(1)
						enemy.health = 100
						battleState = 0
						loot(enemy)

					else:
						decision()

				elif attackMethod == "magic":
					damage = round(attackList[0] / enemy.defense, 2)
					sleep(.2)
					print("You swing your magic and do...", damage, "damage")
					enemy.health = enemy.health - damage
					sleep(.2)
					print("Enemy health remaining:", enemy.health)


					if enemy.health < 1:
						sleep(.2)
						print("you have defeated the" + enemy.name)
						sleep(1)
						enemy.health = 100
						battleState = 0
						loot(enemy)

					else:
						decision()

				elif attackMethod == "ranged":
					damage = round(attackList[0] / enemy.defense, 2)
					sleep(.2)
					print("You use your ranged and do...", damage, "damage")
					enemy.health = enemy.health - damage
					sleep(.2)
					print("Enemy health remaining:", enemy.health)

					if enemy.health < 1:
						sleep(.2)
						print("you have defeated the", enemy.name)
						sleep(1)
						enemy.health = 100
						battleState = 0
						loot(enemy)

					else:
						decision()
		enemyKills += 1
		if enemyKills == 10:
			sleep(.5)
			print("You win!")
			sys.exit()
		else:
			continue
'''

print('Welcome to Creed thoughts')
sleep(1)
print('Just like Creed, don\'t try to make too much sense of things, just enjoy it and roll with it baby')
sleep(1)
print('Creed Thoughts is an interactive puzzle game with the ability to get sidetracked if you wish')
sleep(1)
print('You will be asked a series if questions, if it\'s multiple choice, enter the coorsponding letter of your choice. If it\'s true or false, enter the world \'true\' or \'false\'')
sleep(1)
print('Press ctrl+c at any time to exit the game')
sleep(1)
print('If you make it to the end, you will be rewarded with a special prize')
sleep(1)
print('Lets zap you into Creed\'s body\n\n')
sleep(1)
print('How are you feeling today Creed?')
sleep(1)
feeling()
sleep(1)
print('Lets get to The Office!')
sleep(1)
print('Damn, WB Jones has their construction crew taking up the whole parking lot, looks like you are supposed to park down the street')
sleep(1)
print("What should we do?")
sleep(1)
decision(1, "Try to outsmart them", "Interact with the nearest person", "Observe what others are doing")






