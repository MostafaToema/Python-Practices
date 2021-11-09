#squared of number x

x = int(input("enter the number "))

Ans = 0
iteration = x
while (iteration != 0):
	Ans += x
	iteration -= 1

print(str(x) + "*" + str(x)+ "=" + str(Ans))
