#program 1
def test(n):
	global count
	count = 0
	for i in range(n+1): 
		#count += 1  #write at any time 
		a = add(i)
		print("a = ",a)
	print("called",count)
    
def add(x):
	global count 
	count += 1		 #write at any time
	return x+x

test(5)
print(count)

#program 2

def mul(x):
	global count #declration
	count += 1	
	return x*x

count = 0
mul(5)
mul(5)
mul(5)
mul(5)
mul(5)
print(count)

