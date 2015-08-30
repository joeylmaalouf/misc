import pygame
import random
import sys
import time


class Game(object):
	def __init__(self):
		super(Game, self).__init__()
		self.resolution = (pygame.display.Info().current_w, pygame.display.Info().current_h)
		self.screen = pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)
		pygame.display.set_caption("Dota Demake")
		self.world = World((64, 64), (32, 32))
		self.cam_pos = [0, 0]

	def run(self):
		while True:
			self.check_quit()
			self.move_camera()
			self.draw()

	def check_quit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()

	def move_camera(self):
		mposx, mposy = pygame.mouse.get_pos()
		if mposx < 0.05 * self.resolution[0]:
			self.cam_pos[0] = max(0, self.cam_pos[0] - 8)
		elif mposx > 0.95 * self.resolution[0]:
			self.cam_pos[0] = min(self.world.size[0] - self.resolution[0], self.cam_pos[0] + 8)
		if mposy < 0.05 * self.resolution[1]:
			self.cam_pos[1] = max(0, self.cam_pos[1] - 8)
		elif mposy > 0.95 * self.resolution[1]:
			self.cam_pos[1] = min(self.world.size[1] - self.resolution[1], self.cam_pos[1] + 8)

	def draw(self):
		self.screen.fill((0, 0, 0))
		for row in self.world:
			for item in row:
				pygame.draw.rect(self.screen, item.color, item.rect(self.cam_pos))
		pygame.display.flip()
		time.sleep(float(1 / 60))


class World(object):
	def __init__(self, dim, bsize):
		super(World, self).__init__()
		self.size = [dim[0] * bsize[0], dim[1] * bsize[1]]
		self.grid = [[Block((w, h), bsize) for w in range(dim[0])] for h in range(dim[1])]

	def __getitem__(self, index):
		return self.grid[index]


class Block(object):
	def __init__(self, pos, size):
		self.grid_pos = pos
		self.pixel_pos = (pos[0] * size[0], pos[1] * size[1])
		self.size = size
		self.color = (random.randint(0, 32), random.randint(0, 32), random.randint(0, 32))

	def rect(self, cam_pos):
		return pygame.Rect((self.pixel_pos[0] - cam_pos[0], self.pixel_pos[1] - cam_pos[1]), self.size)


if __name__ == "__main__":
	pygame.init()
	game = Game()
	game.run()
