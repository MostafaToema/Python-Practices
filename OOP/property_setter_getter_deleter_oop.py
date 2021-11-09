class Employee:
    def __init__(self , first , last):
        self.first = first
        self.last  =last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first , self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first , self.last)

    @fullname.setter
    def fullname(self , name):
        self.first , self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last  = None
        print ("Delete Done!")

emp1 = Employee("mostafa" , "saleh")
#getter
print(emp1.email)
print(emp1.fullname)
#setter
emp1.fullname = "mohamed afifi"
print(emp1.email)
print(emp1.fullname)
#deleter
del emp1.fullname
print(emp1.email)
print(emp1.fullname)
#delete all instance(object)
del emp1
print(emp1.email) #Error because emp1 is not defined
print(emp1.fullname) #Error because emp1 is not defined
