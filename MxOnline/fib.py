import random
class Fib(object):
	def __init__(self):
		self.n = 30

	def __iter__(self):
		return self

	# def __next__(self):
	# 	self.n -= 1
     #    if self.n < 0:
     #        raise StopIteration
	# 	return random.randint(1,50)