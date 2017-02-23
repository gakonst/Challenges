# 0 3 4 2
input = raw_input().split()

def kangaroo():
	x1 = int(input[0])
	v1 = int(input[1])
	x2 = int(input[2])
	v2 = int(input[3])
	if ( x1>x2 and v1>=v2 )or (x1<x2 and v1<=v2):
		print 'NO'
		return 0
	c = abs(float(x1-x2)/float(v1-v2))
	if c.is_integer():
		print 'YES'
	else:
		print 'NO'

kangaroo()