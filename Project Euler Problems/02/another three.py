def fib(n,j,lim):
	if(j>lim):
		if((n%2 == 0)):
			return n
		else:
			print n,j
			return 0
	
	else:
		if((n%2 == 0)):
			return n + fib(j,n+j,lim)
		else:
			return fib(j,n+j,lim)

