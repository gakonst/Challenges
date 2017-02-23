def solve(s,n):
	count = 0 
	for a in s:
		if a =='a':
			count+=1
	#Multiply with full repetitions of string
	count = count*(n/len(s))
	#Up to how many chars
	upto= n%len(s)
	for i in range(0,upto):
		if s[i] =='a':
			count+=1
	return count
if __name__ == '__main__':
    s = raw_input()
    n = int(raw_input().strip())
    print solve(s,n)