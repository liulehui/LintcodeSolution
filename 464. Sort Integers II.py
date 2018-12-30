# coding : utf-8

# merge sort

def sort(A):
	left = 0
	right = len(A) - 1 
	mergesort(A,left,right)
	return 

def mergesort(A, left,right):
	if left >= right:
		return
	mid = (left + right) // 2

	mergesort(A,left,mid)
	mergesort(A,mid+1,right)
	merge(A,left,right,mid)
	return
def merge(A,left,right,mid):
	p = left # this is the start of the inplace list
	L = A[left:mid+1]
	R = A[mid+1:right+1]
	l = 0
	r = 0
	while l < len(L) and r < len(R):
		if L[l] <= R[r]:
			A[p] = L[l]
			p += 1
			l += 1
		else:
			A[p] = R[r]
			p += 1
			r += 1
	while l< len(L):
		A[p] = L[l]
		p += 1
		l += 1 
	while r < len(R):
		A[p] =  R[r]
		p += 1
		r += 1

	return

# quick sort
def sort2(A):
	if A is None or len(A) == 0:
		return 
	if len(A) == 1:
		return 
	left = 0
	right = len(A) - 1
	quicksort(A,left,right)
	return 

def quicksort(A,left,right):
	if left >= right:
		return 
	l,r = partition(A,left,right)
	quicksort(A,left,r)
	quicksort(A,l,right)
	return 

def partition(A,left,right):

	pivot_index = (left + right) // 2
	pivot = A[pivot_index]

	l = left
	r = right

	while l <= r:
		while l<=r and A[l] < pivot:
			l += 1
		while l<= r and A[r] > pivot:
			r -= 1
		if l <= r:
			A[l],A[r] = A[r],A[l]
			l += 1
			r -= 1 

	return l,r
	

A = [1,3,5,4,2]
sort2(A)

print(A)