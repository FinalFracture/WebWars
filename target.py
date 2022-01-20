import pygame
import math
class Target:
	def __init__(self, game):
		self.game = game
		self.screen = self.game.screen
		self.rect = pygame.Rect(590, 300, 20,20)
		self.counter = 0
		self.power = 3
		self.durability = 500
		self.color = (0,0,0)
		
		
	def update(self):
		if self.durability:
		#	self.color = (self.durability/2 ,0 , 0)
			self.counter +=1
			for ship in self.game.ships:
				if self.rect.colliderect(ship.rect):
					ship.durability -= self.power
				
			if self.rect.x < 1080:
				self.rect.x += math.sin(self.counter*5)
		
		pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y),self.rect.w)
		