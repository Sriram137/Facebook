class test:
	def __init__(self,a,b,I=1,D=1,R=1):
		self.a = a
		self.b = b
		self.mem = dict()
		self.la = len(a)
		self.lb = len(b)
		self.I = I
		self.D = D
		self.R = R

	def diff(self,i=0,j=0):
		T = self.diff
		memo = self.mem
		if j == self.lb: return self.D * i
		if i == self.la: return self.D * j
		if (i,j) in memo: return memo[i,j]
		if self.a[i] == self.b[j]:
			memo[i,j] = T( i+1,j+1 )
			return memo[i,j]
		memo[i,j] = min(self.R + T(i+1,j+1), self.D + T(i+1,j), self.I + T(i,j+1) ,
		 self.D + T(i,j+1) , self.I + T(i+1,j) )
		# print "##"
		# print i,j
		# print self.R + T(i+1,j[1:])
		# print self.D + T(i[1:0],j)
		# print self.I + T(i,j[1:0])
		# print "##"
		return memo[(i,j)]