class MyClass:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

m = MyClass("mostafa" , "saleh")
print(m.__first) 		   #Make Error
m._MyClass__first = "sasa" #Mutate
print(m._MyClass__first)  #Print

