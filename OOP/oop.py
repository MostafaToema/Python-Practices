class Cs_student:
    stream = "cs"
    def __init__(self , roll):
        self.roll  = roll
    def set_adderss(self , adderss):
        self.adderss = adderss
    def get_adderss(self):
        return self.adderss

s1 = Cs_student(100)
s1.set_adderss("cairo")
adderss = s1.get_adderss()
print(adderss)
print(Cs_student.stream)
print(s1.stream)

