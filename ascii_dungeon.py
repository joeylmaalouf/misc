import curses
from random import randint


def box(rows, cols):
  s = u"\u250C" + (u"\u2500" * cols) + u"\u2510" + "\n"
  for _ in range(rows):
    s += u"\u2502" + (" " * cols) + u"\u2502" + "\n"
  s += u"\u2514" + (u"\u2500" * cols) + u"\u2518"
  return s.encode("utf-8")


class Entity(object):
  def __init__(self, pos = (0, 0), char = "@"):
    super(Entity, self).__init__()
    self.y, self.x = pos
    self.char = char

  def move(self, movement = [0, 0], bounds = [[0, 0], [9, 9]]):
    self.y = max(bounds[0][0], min(bounds[0][1], self.y + movement[0]))
    self.x = max(bounds[1][0], min(bounds[1][1], self.x + movement[1]))
    return self

  def draw(self, screen, color_id = 0, clear = False):
    screen.addch(self.y, self.x, " " if clear else self.char, curses.color_pair(color_id))
    return self


class AsciiDungeon(object):
  def __init__(self):
    super(AsciiDungeon, self).__init__()
    self.screen = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    self.screen.keypad(1)

    self.screen.nodelay(1)
    self.screen.border(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    self.game_over = False
    self.screen_limits = [[1, i - 2] for i in self.screen.getmaxyx()]
    self.player = Entity((1, 1), "@")
    self.enemies = [Entity((randint(*self.screen_limits[0]), randint(*self.screen_limits[1])), "#") for _ in range(3)]

  def close(self):
    self.screen.keypad(0)
    curses.curs_set(1)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    return self

  def run(self):
    while not self.game_over:
      self.step()
    self.close()
    return self

  def step(self):    
    key = self.screen.getch()
    if   key == 27:               self.game_over = True # Esc quits the game
    elif key == curses.KEY_UP:    movement = [-1,  0]
    elif key == curses.KEY_DOWN:  movement = [ 1,  0]
    elif key == curses.KEY_LEFT:  movement = [ 0, -1]
    elif key == curses.KEY_RIGHT: movement = [ 0,  1]
    else:                         movement = [ 0,  0]

    self.player.draw(self.screen, color_id = 0, clear = True)
    self.player.move(movement, self.screen_limits)
    self.player.draw(self.screen, color_id = 0)

    for e in self.enemies:
      e.draw(self.screen, color_id = 1, clear = True)
      e.move([randint(-1, 1), randint(-1, 1)], self.screen_limits)
      e.draw(self.screen, color_id = 1)
      if e.y == self.player.y and e.x == self.player.x:
        self.game_over = True

    self.screen.refresh()
    curses.napms(17)
    return self


if __name__ == "__main__":
  AsciiDungeon().run()
