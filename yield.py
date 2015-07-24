def mod(it, div, val):
	for i in it:
		if i%div == val:
			yield i
# alternative to [i for i in it if i%div == val]


def original(it): return mod(it, div = 1, val = 0)
def even(it): return mod(it, div = 2, val = 0)
def odd(it): return mod(it, div = 2, val = 1)


data = range(20)
for fn in [original, even, odd]:
	print(fn.__name__)
	it = fn(data)
	print list(it)
	print("")
