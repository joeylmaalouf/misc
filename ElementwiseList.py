import operator


class ElemList(list):
	def _operate(self, opfunc, other = None, right = False):
		return [((opfunc(value, other) if not right else opfunc(other, value)) if other is not None else opfunc(value)) for value in self]

	def __add__(self, other): return self._operate(operator.__add__, other)
	def __sub__(self, other): return self._operate(operator.__sub__, other)
	def __mul__(self, other): return self._operate(operator.__mul__, other)
	def __div__(self, other): return self._operate(operator.__div__, other)
	def __mod__(self, other): return self._operate(operator.__mod__, other)
	def __pow__(self, other): return self._operate(operator.__pow__, other)

	def __radd__(self, other): return self._operate(operator.__add__, other, True)
	def __rsub__(self, other): return self._operate(operator.__sub__, other, True)
	def __rmul__(self, other): return self._operate(operator.__mul__, other, True)
	def __rdiv__(self, other): return self._operate(operator.__div__, other, True)
	def __rmod__(self, other): return self._operate(operator.__mod__, other, True)
	def __rpow__(self, other): return self._operate(operator.__pow__, other, True)

	def __pos__(self): return self._operate(operator.__pos__)
	def __neg__(self): return self._operate(operator.__neg__)
	def __abs__(self): return self._operate(operator.__abs__)


if __name__ == "__main__":
	el = ElemList([-4, -1, 1, 4])
	tests = [
	"el",
	"el + 5",
	"el - 2",
	"el * 3",
	"el / 2",
	"el % 2",
	"el ** 2",
	"5 + el",
	"2 - el",
	"3 * el",
	"2 / el",
	"2 % el",
	"2 ** el",
	"+el",
	"-el",
	"abs(el)"
	]
	for test in tests:
		print "{0}:\n\t{1}\n".format(test, eval(test))
