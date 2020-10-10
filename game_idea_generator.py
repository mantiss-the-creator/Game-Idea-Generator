import random

keywords = ['spaceships', 'cars', 'planes', 'sports', 'tanks', 'space', 'city',
			'guns', 'future', 'catapults', 'medieval', 'ancient', 'aliens',
			'computers', 'lasers', 'insects', 'reptiles', 'fish', 'frogs',
			'cats', 'dogs', 'knights', 'swords', 'cannons', 'war', 'planets',
			'nature', 'building', 'blocks', 'adventure', 'retro', 'platformer',
			'shooter', 'fighting', 'racing', 'hacking', 'lava', 'love',
			'school', 'virus', 'zombie', 'plants', 'science', 'galaxy',
			'knives', 'jungle', 'survival', 'tropical', 'arctic', 'snow',
			'winter', 'caves', 'crystals', 'gold', 'pirates', 'ocean', 'beach',
			'crabs', 'sharks', 'whales', 'shopping', 'money', 'animals',
			'monsters', 'creatures', 'ships', 'warships', 'bombs', 'explosions',
			'nations', 'food', 'sky', 'clouds', 'birds', 'drones', 'combat']

print('\nWelcome to the Game Idea Generator!\n')
print('It will pick random keywords for you to base game ideas on!\n')

while True:
	while True:
		num = input('Number of keywords: ')
		try:
			num = int(num)
		except:
			print(f"'{num}' is not a number!")
			continue
		if num <= 1:
			print('The number has to be bigger than 1!')
			continue
		break

	print('\nThe keywords are:')
	chosen_keywords = ''
	for i in range(num - 1):
		chosen_keywords +=	random.choice(keywords) + ', '
	chosen_keywords += random.choice(keywords)
	print(chosen_keywords + '\n')

	while True:
		another = input('Generete another idea? [y/n]: ')
		if another == 'y':
			break
		elif another == 'n':
			quit()
		else:
			print(f"'{another}' is not an option!")
