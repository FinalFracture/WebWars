import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	"""a class to create shipa basedbon units from sorter module"""
	def __init__(self, game):
		super().__init__()
		self.game = game
		
		#spawning
		self.spawn = self.game.spawn.spawn_point
		self.rect = pygame.Rect(self.spawn.x, self.spawn.y, 40, 40)
		
		#in case of triangle
		self.trigon = ()
		
		#ship metrics
		self.stats = self.game.splitter.assign_to_ship()
		self.name = self.stats[0]
		self.traits = self.stats[2]
		self.stats = self.stats[1]
		self.power = self.stats[0]
		self.durability = self.stats[1]
		self.speed = self.stats[2]
		self.target = self.game.target
		
		
		#color assignment
		self.red = 0
		self.green = 0
		self.blue = 0
		self.color = 0
		self.get_color()
		
	def update(self):
		#this will have the logic for getting the ships next position
		if self.rect.colliderect(self.target.rect):
			self.target.durability -= self.power
		if self.rect.y > self.target.rect.y:
			self.rect.y -= self.speed
		elif self.rect.y < self.target.rect.y:
			self.rect.y += self.speed
		if self.rect.x > self.target.rect.x:
			self.rect.x -= self.speed
		if self.rect.x < self.target.rect.x:
			self.rect.x += self.speed
		
	def draw_ship(self):
		if self.durability < 0:
			self.kill()
		#draws ship when called
		highest_stat = max(self.stats)
		if  self.stats.index(highest_stat) == 0:
			self.get_triangle()
			pygame.draw.polygon(self.game.screen, self.color, self.trigon)
		elif  self.stats.index(highest_stat) == 1:
			pygame.draw.rect(self.game.screen, self.color, self.rect)
		elif  self.stats.index(highest_stat) == 2:
			pygame.draw.circle(self.game.screen, self.color, (self.rect.x, self.rect.y), 20)
			
			
	def get_color(self):
		# determine color of ships
		
		#red
		if self.stats[0]*10 > 255:
			self.red = 255
		else:
			self.red = self.stats[0]*10
			#green
		if self.stats[1]*10 > 255:
			self.green = 255
		else:
			self.red = self.stats[1]*10
			#blue
		if self.stats[2]*10 > 255:
			self.blue = 255
		else:
			self.blue = self.stats[2]*10
			
		self.color = (self.red, self.green, self.blue)
		
		
	def get_triangle(self):
		# define triangle points
		trigon_p1 = (self.rect.x, self.rect.y)
		trigon_p2 = (trigon_p1[0]-20, trigon_p1[1]+40)
		trigon_p3 = (trigon_p2[0]+40, trigon_p2[1] )
		self.trigon = (trigon_p1, trigon_p2, trigon_p3)