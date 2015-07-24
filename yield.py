from pprint import pprint as pp


def mod(it, div, val):
	for i in it:
		if i%div == val:
			yield i


def loop(it, fn = pp):
	while True:
		try:
			fn(it.next())
		except:
			break


def original(it): return mod(it, div = 1, val = 0)
def even(it): return mod(it, div = 2, val = 0)
def odd(it): return mod(it, div = 2, val = 1)


data = range(20)
for fn in [original, even, odd]:
	print(fn.__name__)
	it = fn(data)
	loop(it)
	print("")
