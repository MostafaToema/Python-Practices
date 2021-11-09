#calculate cube root of cube

cube = int(input("enter an integer "))

for ans in range(0,abs(cube)+1):
	if (ans**3 >= abs(cube)):
		break
if(ans**3 != abs(cube)):
	print (str(cube) + " is not aperfect cube")
else:
	if (cube < 0):
		ans = -ans
	print("cube root of " + str(cube) + " is " + str(ans))
print("done")
