import math
import pygame
import sys
import time


class Game(object):
	def __init__(self):
		super(Game, self).__init__()
		info_obj = pygame.display.Info()
		self.screen = pygame.display.set_mode((info_obj.current_w, info_obj.current_h), pygame.FULLSCREEN)
		pygame.display.set_caption("Python Game")
		self.player = Player()

	def run(self):
		while True:
			self.process_inputs()
			self.player.move()
			self.draw_player()

	def process_inputs(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.player.dest = list(pygame.mouse.get_pos())

	def draw_player(self):
		self.screen.fill((0, 0, 0))
		pygame.draw.circle(self.screen, (0, 200, 0), self.player.pos, self.player.radius)
		pygame.display.flip()
		time.sleep(float(1/30))


class Player(object):
	def __init__(self):
		self.radius = 8
		self.pos = [100, 100]
		self.speed = 8
		self.dest = self.pos

	def move(self):
		dx = self.dest[0]-self.pos[0]
		dy = self.dest[1]-self.pos[1]
		mag = math.sqrt(dx**2 + dy**2)
		if abs(dx) < self.speed and abs(dy) < self.speed:
			self.pos = self.dest
		else:
			self.pos[0] += int(self.speed*dx/mag)
			self.pos[1] += int(self.speed*dy/mag)


def main(argv):
	pygame.init()
	game = Game()
	game.run()


if __name__ == "__main__":
	main(sys.argv)
