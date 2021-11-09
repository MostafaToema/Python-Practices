#divisible number num by 2 and 3

num = int(input("enter an integer "))

if (num % 2) == 0:
	if (num % 3) == 0:
		print("number divisible by 2 and 3 ")
	else:
		print("number divisible by 2")
elif (num % 3) == 0:
	print("number divisible by 3")
else:
	print("number not divisible by 2 and 3")
print("done")
