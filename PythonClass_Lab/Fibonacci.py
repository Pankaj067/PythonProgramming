'''
Fibonnaci using recursion

def fibonnaci(n):
	if n == 1:
	 return 1
	elif (n == 2):
	 	return 1
	else:
	 	return 	fibonnaci(n-1) + fibonnaci(n-2)



for n in range(1,100):
	print(n,":", fibonnaci(n))

'''

#Dynamic Programming

fibonnaci_cache = {}

def fibonnaci(n):
	if n in fibonnaci_cache:
		return fibonnaci_cache[n]

	if n ==1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonnaci(n-1) + fibonnaci(n-2)

	fibonnaci_cache[n] = value
	return value

for n in range(1,1000):
	print(n," -> ",fibonnaci(n))

