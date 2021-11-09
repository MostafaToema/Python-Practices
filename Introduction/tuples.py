#how to create tuples and access the elements

t1 = (1,"saleh",45)
t2 = (t1 ,"sasa")

print(t1)
print(t2)
#concatenation
print (t1 + t2)
#indexing
print(t1[1])
print((t1 + t2)[3])
#slicing
print((t1 + t2)[2:5])
#singletons
t3 = ("three",)
print(t3)
print(t1 + t2 + t3)
