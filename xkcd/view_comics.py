import pygtk
pygtk.require("2.0")
import gtk


class Viewer(object):
	def __init__(self):
		self.current_id = 1
		self.main = gtk.main
		self.quit = gtk.main_quit
		self.image = gtk.Image()
		self.window = gtk.Window()
		self.window.connect("destroy", gtk.main_quit)
		self.window.connect("key_press_event", self.key_press)
		self.window.add(self.image)
		self.res = [self.window.get_screen().get_width(), self.window.get_screen().get_height()]
		self.update_image()
		self.window.show_all()

	def key_press(self, widget, event):
		if gtk.gdk.keyval_name(event.keyval) == "Left":
			self.current_id -= 1
			self.update_image()
		elif gtk.gdk.keyval_name(event.keyval) == "Right":
			self.current_id += 1
			self.update_image()

	def update_image(self):
		self.window.set_title("XKCD Comic #{0:04d}".format(self.current_id))
		self.image.set_from_file("xkcd_comic_{0:04d}.jpg".format(self.current_id))
		self.window.resize(self.res[0], self.res[1])


if __name__ == "__main__":
	v = Viewer()
	v.main()
