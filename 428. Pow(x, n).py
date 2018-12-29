# coding:utf-8

# fast power
# non recursion
def myPow(x, n):
	if n < 0:
		x = 1/x
		n = -n
	ans = 1
	base = x

	while n != 0:
		if n%2 == 1:
			ans *= base
			print('ans = '+ str(ans))
		base *= base
		print('base = '+str(base))
		n = n//2
	return ans

# recursion
def myPow2(x,n):
	if n == 0:
		return 1
	if n%2 == 0:
		temp = myPow2(x,n//2)
		return temp * temp
	if n%2 == 1:
		temp = myPow2(x,n//2)
		return temp * temp * x

x = 3
n = 9
print(myPow(x,n))

print(myPow2(x,n))
