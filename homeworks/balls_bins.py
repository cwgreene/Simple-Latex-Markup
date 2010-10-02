def fac(n):
	prod = 1
	for x in range(n):
		prod *= (x+1)
	return prod

def choose(m,n):
	return fac(n)/(fac(m)*fac(n-m))

mde = {}
def distribute_exact(balls,bins):
	if bins == 1:
		return 1
	if (balls,bins) in mde:
		return mde[(balls,bins)]
	result = bins**balls
	for i in range(1,bins):
		result -= choose(bins-i,bins)*distribute_exact(balls,i)
	mde[(balls,bins)] = result
	return result

def probability_exact(balls,bins):
	return distribute_exact(balls,bins)*1.0/(bins**balls)
