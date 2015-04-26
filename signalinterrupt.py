import signal
import sys
import time


def signal_handler(signal, frame):
		print("\nYou pressed Ctrl+C!")
		sys.exit(0)


def main(argv):
	signal.signal(signal.SIGINT, signal_handler)
	i = 0
	while True:
		print(i)
		i += 1
		time.sleep(0.1)


if __name__ == "__main__":
	main(sys.argv)
