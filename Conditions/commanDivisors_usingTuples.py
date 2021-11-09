#start
def find_divisors(num1 , num2):
	divisors = ()
	for i in range(1 , min(num1 , num2) + 1):
		if ((num1 % i == 0)and(num2 % i == 0 )):
			divisors += (i,) 
	return divisors
#end

number1 = int (input("enter an number1: "))
number2 = int (input("enter an number2: "))
divs = find_divisors(number1 , number2)
print(divs)

total = 0
#summation of divisors
for div in divs:
	total += div
print(total)
