import sorter
import requests as req

url = 'https://futuretimeline.net/'

""" a mudule to take input and split it into individual words"""


class Splitter:
	def __init__(self, game):
		self.game = game
		self.divider_characters = [' ', '.', '-', '+']
		self.text = req.get(url)
		self.text = self.text.text
		self.sorter = sorter.Sorter(self)
		self.sentence = []
		self.skip_chars = ['<', '(', '[', '{']
		self.return_chars = ['>', ')', ']', '}']
		self.skip = False
		self.generate()
		
	def deconstruct(self):
		for char in self.text:
			if not self.skip:
				if char not in self.skip_chars:
					self.sentence.append(char)
				if char in self.skip_chars:
					self.skip = True
			if self.skip:
				if char in self.return_chars:
					self.skip = False
				
		
	def split(self, doc):
		word = []
		sentence = []
		for line in doc:
			line = line.strip()
			for letter in line.lower():
				if letter in self.sorter.accepted_letters:
					word.append(letter)
				if letter in self.divider_characters:
					if len(word) < 15:
						sentence.append(''.join(word))
					word =[]
		return sentence
		
	def generate(self):
		self.sentence = self.split(self.text)
		self.game.log.write(str(len(self.sentence)))
		return self.sentence
		
	def assign_to_ship(self):
		word = self.sentence[0]
		unit = self.sorter.create_unit(word)
		self.sentence.pop(0)
		return unit
		
		
			