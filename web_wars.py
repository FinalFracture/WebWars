import pygame
import spawning
import splitter
import hud
import target

from ship import Ship



class Webwars:
	"""class  to manage assets for the game """
	
	def __init__(self):
		#initialize and
		pygame.init()
		self.log = open('event_log.txt', 'w')
		self.screen = pygame.display.set_mode((1080, 2175))
		self.hud = hud.Hud(self)
		self.spawn = spawning.Spawn_points(self)
		self.ships = pygame.sprite.Group()
		self.splitter = splitter.Splitter(self)
		self.target = target.Target(self)
		self.spawned_ships = 0
		
		

	def run(self):
		"""Main function"""
		while True:
			self._check_events()
			self._update_screen()
					
			
			
	def _check_events(self):
		#pygame events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.log.write(f'\n{self.spawned_ships} spawned (main 40)\n')
				self.log.close()
				pygame.quit()
			elif event.type == pygame.FINGERDOWN:
				pos = pygame.mouse.get_pos()
				if self.hud.spawn_rect.collidepoint(pos):
					self._spawn_ship(pos)
				if self.hud.auto_rect.collidepoint(pos):
					if self.spawn.auto is True:
						self.spawn.auto = False
					elif self.spawn.auto is False:
						self._auto_spawn()
		#non pygame events
		if self.spawn.auto is True:
			self._auto_spawn()
			
#  _-_-_-_-_function zone _-_-_-_-_-_-_
					
	def _spawn_ship(self, pos):
		self.spawn.tap_spawn(pos)
		new_ship = Ship(self)
		self.ships.add(new_ship)
		self.spawned_ships += 1
		
	def _auto_spawn(self):
		self.spawn.auto_spawn()
		new_ship = Ship(self)
		self.ships.add(new_ship)
		self.spawned_ships += 1
					
	def _update_screen(self):
		self.screen.fill((150,150,150))
		self.hud.draw()
		for ship in self.ships.sprites():
			ship.draw_ship()
		self.ships.update()
		self.target.update()
		
		pygame.display.flip()
			
			
game = Webwars()
game.run()
