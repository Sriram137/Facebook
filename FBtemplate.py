import sys

class fb:
	f = open(sys.argv[1])
	@classmethod
	def line(cls,type=str):
		return type(str(cls.f.readline().strip()))
		
	@classmethod
	def lis(cls,type=str):
		return [ type(x) for x in cls.f.readline().strip()]

def go():
	pass