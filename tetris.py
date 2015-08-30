import pygame
from sys import argv, exit
from time import sleep


class Game(object):
	def __init__(self, dimensions = (28, 8), block_size = (24, 32)):
		super(Game, self).__init__()
		pygame.init()
		self.dimensions = dimensions
		self.block_size = block_size
		self.colors = ((200, 200, 200), (100, 100, 100))
		self.grid = [[False]*dimensions[1] for _ in range(dimensions[0])]
		self.screen = pygame.display.set_mode((block_size[1]*dimensions[1], block_size[0]*dimensions[0]))

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						exit()

			for i in range(len(self.grid)):
				for j in range(len(self.grid[0])):
					pygame.draw.rect(
						self.screen,
						self.colors[int(self.grid[i][j])],
						pygame.Rect(self.block_size[1] * j, self.block_size[0] * i, self.block_size[1] - 1, self.block_size[0] - 1) # -1 to show border lines
					)

			pygame.display.flip()
			sleep(0.25)


if __name__ == "__main__":
	tetris = Game()
	tetris.run()
