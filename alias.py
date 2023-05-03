import random

words = [
  'home',
  'sun',
  'dog',
  'river',
  'mountain',
  'rose',
  'curtain',
  'chair',
  'chocolate',
  'star',
  'eskimo',
  'coworking',
  'cat',
  'delivery',
  'Thor',
  'crown',
  'axe',
  'banana',
  'happy',
  'blood',
  'bag',
  'smile',
  'stone',
  'goose',
  'beer',
  'got',
  'olive',
  'bass',
  'winter',
  'lake',
  'rainbow'
]

words = sorted(words, key=lambda A: random.random())

class Player:
	guesses = 0
	count = 0
	name = ''
	
playerOne = Player()
playerTwo = Player()

players = [playerOne, playerTwo]
state = 0

players[0].name = str(input('What is the 1-st player name? '))
print('Hello ' + players[state].name + '!')
print('')

players[1].name = str(input('What is the 2-nd player name? '))
print('Hello ' + players[state].name + '!')
print('')
  
while words[0]:
	
	if players[state].guesses == 0:
		print('------------------------')
		print('')
		print('The player: ' + players[state].name)
		print('')
		print('------------------------')
		print('')
	
	print('The word: ' + words[0].upper())
	guess = input('Guessed right? ')
	
	if guess == '1':
		words.remove(words[0])
		players[state].count += 1
		print('Yes')
	else:
		print('No')	
		print('Bad luck...(')
		
		if players[state].count >= 1:
			players[state].count -= 1
			
		words.remove(words[0])
		
	players[state].guesses += 1
	
	print(players[state].name + '\'s count: ' + str(players[state].count))
	print('')
			
	if not words or players[1].count >= 10 and players[state].name != players[0].name and players[state].guesses == 3 or players[0].count >= 10 and players[state].name != players[0].name and players[state].guesses == 3:
		print('------------------------')
		print('')
		print('Game over!')
		print('')
		print('------------------------')
		print('')
		break
		
	if players[state].guesses == 3:
		players[state].guesses = 0
		if state == 0:
			state = 1
		else:
			state = 0
		
print('First player: ' + players[0].name)
print('Count: ' + str(players[0].count))
print('Second player: ' + players[1].name)
print('Count: ' + str(players[1].count))
print('')

print('------------------------')
print('------------------------')
print('')

if players[0].count == players[1].count:
	print('FRENDSHIP WIN!')
elif players[0].count > players[1].count:
	print(players[0].name.upper() + ' WIN!')
else:
	print(players[1].name.upper() + ' WIN!')
print('')
print('------------------------')
print('------------------------')

input('Press ENTER to exit')