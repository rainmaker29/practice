#Hackerrank Interview Set : Arrays #4

#Given an array , find how many times a number has bribed to move it's poition behind
# Example : 1 2 3 5 4 here 4 has bribed to get behind 5.
# If a number has moved more than two positions (>2) , print 'Too chaotic'

def bribe(q):
	ans=0
	#Start from the last element
	for i in range(len(q),-1,-1):
		if q[i]-(i+1)>2:
			print("Too chaotic")
			return
			# Since if q[i] - (i+1) > 2 => the element has moved forward by more than 2 positions
		for j in range(max(0,q[i]-2),i):
			if q[j]>q[i]:
				ans+=1
	print(ans)
