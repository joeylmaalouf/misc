import operator


class ElemList(list):
	def _operate(self, opfunc, other = None):
		return [opfunc(value, other) if other is not None else opfunc(value) for value in list(self)]
	def __add__(self, other): return self._operate(operator.__add__, other)
	def __sub__(self, other): return self._operate(operator.__sub__, other)
	def __mul__(self, other): return self._operate(operator.__mul__, other)
	def __div__(self, other): return self._operate(operator.__div__, other)
	def __mod__(self, other): return self._operate(operator.__mod__, other)
	def __pow__(self, other): return self._operate(operator.__pow__, other)
	def __pos__(self): return self._operate(operator.__pos__)
	def __neg__(self): return self._operate(operator.__neg__)
	def __abs__(self): return self._operate(operator.__abs__)
	def __radd__(self, other): return self.__add__(other)
	def __rmul__(self, other): return self.__mul__(other)


if __name__ == "__main__":
	el = ElemList(range(-1, 4))
	print el
	print el + 5
	print 5 + el
	print el - 2
	print el * 3
	print 3 * el
	print el / 2
	print el % 2
	print el ** 2
	print +el
	print -el
	print abs(el)

