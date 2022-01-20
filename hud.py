import pygame

class Hud:
	def __init__(self, game):
		self.game = game
		
		#word side bars
		self.left_rect = pygame.Rect(0,1500, 300, 675)
		self.right_rect = pygame.Rect(780, 1500, 300, 675)
		self.bar_color = (100,140,100)
		
		# black side bar background
		self.left_bg = pygame.Rect(0, 1485, 315, 725)
		self.right_bg = pygame.Rect(765, 1485, 315, 725)
		self.bg_color = (0,0,0)
		
		#spawn zone
		self.spawn_rect = pygame.Rect(315, 1780,450, 400)
		self.spawn_color = (140, 85, 85,)
		
		#auto spawn
		self.auto_rect = pygame.Rect(800, 1450, 250, 30)
		self.auto_color = (120, 60 , 200)
		
		
	def draw(self):
		self.get_color_change()
		pygame.draw.rect(self.game.screen, self.spawn_color, self.spawn_rect)
		pygame.draw.rect(self.game.screen, self.bg_color, self.right_bg)
		pygame.draw.rect(self.game.screen, self.bg_color, self.left_bg)
		pygame.draw.rect(self.game.screen, self.bar_color, self.left_rect)
		pygame.draw.rect(self.game.screen, self.bar_color, self.right_rect)
		pygame.draw.rect(self.game.screen, self.auto_color, self.auto_rect)
		
	def get_color_change(self):
		if self.game.spawn.auto == True:
			self.auto_color = (30, 200, 50)
		else:
			self.auto_color = (120, 60 , 200)