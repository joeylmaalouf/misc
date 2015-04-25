import pyglet
from pyglet.gl import *
from pyglet.window import key


def main():
	win = pyglet.window.Window(resizable=True)
	vertices = []
	vertices.append((150, 150, 0))
	vertices.append((200, 200, 0))
	vertices.append((250, 250, 0))
	vertices.append((300, 300, 0))

	@win.event
	def on_key_press(symbol, modifiers):
		print("The " + key.symbol_string(symbol) + " key was pressed.")

	@win.event
	def on_draw():
		# Clear buffers
		glClear(GL_COLOR_BUFFER_BIT)
		# Draw outlines only
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
		# Draw some stuff
		glBegin(GL_LINES)
		for v in vertices:
			glVertex3i(v[0], v[1], v[2])
		glEnd()

	pyglet.app.run()


if __name__ == "__main__":
	main()
