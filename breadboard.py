import pygame
import sys


class Breadboard(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((400, 200))
		self.state = 0
		self.states = ["State 0: user needs to click the resistor to begin placement.", "State 1: user needs to click position 1 of the resistor.", "State 2: user needs to click position 2 of the resistor."]
		self.pos1 = (0, 0)
		self.pos2 = (0, 0)

	def run(self):
		while True:
			self.update()
			self.draw()

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mpos = pygame.mouse.get_pos()
				if self.state == 0:
					if mpos[0] < 100 and mpos[1] < 100:
						self.state = 1
				else:
					if mpos[0] > 200:
						if self.state == 1:
							self.pos1 = mpos
							self.pos2 = mpos
							self.state = 2
						elif self.state == 2:
							self.pos2 = mpos
							self.state = 0
				print(self.states[self.state])

	def draw(self):
		pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(0, 0, 100, 100))
		pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(200, 0, 200, 200))
		pygame.draw.line(self.screen, (0, 0, 255), self.pos1, self.pos2, 5)
		pygame.display.flip()


if __name__ == "__main__":
	b = Breadboard()
	b.run()
