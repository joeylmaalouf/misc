from multiprocessing import Process, Lock
from os.path import exists
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent
from time import strftime


class MouseLogger(PyMouseEvent):

	def __init__(self, lock, path):
		super(MouseLogger, self).__init__()
		self.lock = lock
		self.path = path

	def click(self, x, y, button, press):
		timestamp = strftime("%m/%d/%Y %H:%M:%S")
		status = "pressed " if press else "released"
		logstring = "[{0}] Mouse button {1} was {2} at position ({3:04d}, {4:04d}).\n".format(timestamp, button, status, x, y)
		self.lock.acquire()
		mode = "a" if exists(self.path) else "w"
		fileobj = open(self.path, mode)
		fileobj.write(logstring)
		fileobj.close()
		self.lock.release()


class KeyboardLogger(PyKeyboardEvent):

	def __init__(self, lock, path):
		super(KeyboardLogger, self).__init__()
		self.lock = lock
		self.path = path

	def tap(self, keycode, character, press):
		timestamp = strftime("%m/%d/%Y %H:%M:%S")
		status = "pressed" if press else "released"
		logstring = "[{0}] Keyboard button \"{1}\" was {2}.\n".format(timestamp, character, status)
		self.lock.acquire()
		mode = "a" if exists(self.path) else "w"
		fileobj = open(self.path, mode)
		fileobj.write(logstring)
		fileobj.close()
		self.lock.release()


class DuoLogger(object):

	def __init__(self, outputpath):
		lock = Lock()
		self.ML = MouseLogger(lock, outputpath)
		self.KL = KeyboardLogger(lock, outputpath)
		self.MP = Process(target = self.ML.run)
		self.KP = Process(target = self.KL.run)

	def run(self):
		self.MP.start()
		self.KP.start()
		self.MP.join()
		self.KP.join()


if __name__ == "__main__":
	logger = DuoLogger("./log.txt")
	logger.run()
