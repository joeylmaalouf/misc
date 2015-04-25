import random
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

size = m.screen_size()
print("size: %s" % (str(size)))
pos = (random.randint(100, size[0]-100), random.randint(100, size[1]-100))
print("Position: %s" % (str(pos)))

for i in range(2):
	k.press_key(k.alt_key)
	k.tap_key(k.tab_key)
	k.release_key(k.alt_key)
	time.sleep(1)

m.move(pos[0], pos[1])
for i in range(100):
	m.move(pos[0]+2*i, pos[1]+i)
	time.sleep(0.025)
pos = m.position()
time.sleep(1)
m.click(pos[0], pos[1], 1)
time.sleep(1)
m.click(pos[0], pos[1], 2)
time.sleep(1)
m.click(pos[0], pos[1], 3)
