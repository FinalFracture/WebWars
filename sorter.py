
""" this module goes through each letter and assigns it a stat value"""


class Sorter:
	"""splits words into individual components and gives each a stat """
	
	def __init__(self,splitter):
		
		self.splitter = splitter
		self.word = ''
		self.letter_count = 0
		self.durability_letters = ['r', 'h', 'g', 'a', 'f', 'u','l']
		self.attack_letters = ['k', 'e', 'i', 'd', 'm', 'b']
		self.speed_letters = ['s', 't', 'c', 'o', 'n', 'y']
		self.special_letters = ['z', 'x', 'w', 'v', 'p', 'q', 'j']
		self.accepted_letters = self.special_letters + self.durability_letters+self.attack_letters+self.speed_letters
		self.unit_stats = []
		self.unit_name = ''
		self.unit = []
		self.unit_traits =[]
		self.special_words = []
		
		
		
	def create_unit(self, word):
		#a function to split the word and generate an object with stats
		self.word = word
		self.assign_stats()
		
		for letter in self.word:
			if letter in self.special_letters:
				self.unit_stats = self.special_letter(letter)
				
		self.unit_name = self.word
		if self.word in self.special_words:
			None
		self.unit = [self.unit_name, self.unit_stats, self.unit_traits]
		
		self.unit_traits = []
		self.letter_count = 0
		return self.unit
		
		
		
		
	def special_letter(self, letter):
		#function to assign traits to words based on special characters
		multiplier = self.letter_count * 0.05

		if letter == 'w':
			self.unit_stats[2] += multiplier
		elif letter == 'x':
			self.unit_stats[0] +=  multiplier
		elif letter == 'q':
			self.unit_stats[1] += multiplier
		elif letter == 'v':
			self.unit_traits.append('v')
		elif letter == 'w':
			self.unit_traits.append('w')
		elif letter == 'j':
			self.unit_traits.append( 'j')
		elif letter == 'p':
			self.unit_traits.append('p')
		return self.unit_stats
		
	def assign_stats(self):
		#brraks the word into stat components
		word_power = 1
		word_durability = 1
		word_speed = 1
		for letter in self.word:
			self.letter_count += 1
			if letter in self.attack_letters:
				word_power +=1
			elif letter in self.speed_letters:
				word_speed +=1
			elif letter in self.durability_letters:
				word_durability += 1
		self.unit_stats = [word_power, word_durability, word_speed]