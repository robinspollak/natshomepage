def collatz(n,our_dict):
	original = n
	counter = 0
	while True:
		if n==1: 
			our_dict[original]=counter
			return n,our_dict
		elif n in our_dict:
			return our_dict[n]+counter,our_dict
		elif n%2 = 0:
			n = n/2
		else:
			n=3n+1

max_length = 0
memoization = {}
for number in range(1000000):
	length,memoization = collatz(number)
	print "number %d has series length %d"%(number,length)
	if length>max_length: max_length=length
print max_length



