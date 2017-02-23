test_cases = int(raw_input().strip())
for i in range(0,test_cases):
	data = map(int,raw_input().split())
	n = data[0]
	k = data[1]
	cancelled = True
	ontime = 0
	times = map(int,raw_input().split())
	for i in range(0,n):
		if times[i]<=0:
			ontime+=1
		if ontime>=k:
			cancelled = False
			break
	if cancelled:
		print 'YES'
	else:
		print 'NO'