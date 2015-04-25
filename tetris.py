import pygame
from sys import argv
from time import sleep


def initialize(grid, n_rows, n_cols):
	for i in range(n_rows):
		row = []
		for j in range(n_cols):
			row.append(False)
		grid.append(row)


def main(argv):
	pygame.init()
	grid = []
	dimensions = (24, 8)
	size = (24, 32)
	colors = ((200, 200, 200), (100, 100, 100))
	initialize(grid, dimensions[0], dimensions[1])
	screen = pygame.display.set_mode((size[1]*dimensions[1], size[0]*dimensions[0]))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				pygame.draw.rect(screen, colors[int(grid[i][j])], pygame.Rect(size[1]*j, size[0]*i, size[1]-1, size[0]-1))

		pygame.display.flip()
		sleep(0.25)


if __name__ == "__main__":
	main(argv)
