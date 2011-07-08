import sys

class fb:
	f = open(sys.argv[1])
	@classmethod
	def line(cls,type=str):
		return type(str(cls.f.readline().strip()))

	@classmethod
	def lis(cls,type=str):
		return [ type(x) for x in cls.f.readline().strip().split()]

def comp(x):
	return not x

def go():
	s = fb.line(int)
	color = dict()
	for i in xrange(0,s):
		t= fb.lis()
		x,y,temp,retcol = t[0],int(t[1]),[],False
		for j in xrange(y):
			z = fb.line()
			temp.append(z)
			if z in color:
                            retcol = comp(color[z])
                            print "###########"
                try:
		    color[x] = color[x]
                    retcol = comp(color[x])
                except Exception:
                    color[x] = retcol
                    print "$$$$$$$$$$"
                    retcol = comp(retcol)
		for z in temp:
			color[z] = retcol
                print color
	t,f = (0,0)
	for i in color.values():
		if i: t+=1
		else: f+=1
	print "%d %d"%(max(t,f),min(t,f))
        print color
go()
