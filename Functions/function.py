#function to calculate power

def power(n , p):
	result = 1
	for iteration in range(p):
		result *= n
	return result
#end 

base_num = float(input("enter an number "))
power_num = int (input("enter an power number "))

ret_val = power(base_num,power_num)
print(ret_val)
