import sys

class fb:
	@classmethod
	def init(cls):
		f = open(sys.argv[1])

	@classmethod
	def line(cls,type=str):
		return type(str(f.readline().strip()))
		
	@classmethod
	def lis(cls,type=str):
		return [ type(x) for x in f.readline().strip()]


def go():
	fb.init()
	z = fb.line(int)
	for x in xrange(1,z+1):
		if x %3 == 0:
			if x % 5 == 0: print "Hop" 
			else: print "Hoppity"
		elif x % 5 == 0:print "Hophop"
f = open(sys.argv[1])
go()