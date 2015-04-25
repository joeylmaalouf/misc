from pymouse import PyMouse
import math
import time
m = PyMouse()
pos = m.position()
for i in range(100):
	n = i/4.0
	m.move(pos[0]+50*math.cos(n), pos[1]+50*math.sin(n))
	time.sleep(0.01)
m.move(pos[0], pos[1])
