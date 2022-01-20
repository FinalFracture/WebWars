import pygame
import random

class Spawn_points:
	""" a class to manage ship spawning"""
	def __init__(self, game):
		self.game = game
		self.spawn_point = pygame.Rect(0,0,1,1)
		self.spawn_zone_rect = self.game.hud.spawn_rect
		self.auto = False
		
		
	def auto_spawn(self):
		self.auto = True
		self.spawn_point.x = random.randint(self.spawn_zone_rect.x, self.spawn_zone_rect.x+450)
		self.spawn_point.y = random.randint(self.spawn_zone_rect.y, self.spawn_zone_rect.y+400)
			
	def tap_spawn(self, pos):
		self.auto = False
		self.spawn_point.x = pos[0]
		self.spawn_point.y = pos[1]
				
				
		