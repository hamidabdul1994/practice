# Author Hamid Raza Noori(noorihamid1994@gmail.com) 
# Desc Sample OOPS program
# Date 07 Nov 2020

class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def fullName(self):
        return self.firstName + " " + self.lastName

emp = Employee('Aroh','yadav') #memory allocation
print(emp.fullName())


emp1 = Employee('Ahad','siddiqui')
print(emp1.fullName())

# 10001 : emp {aroh , yada}
# 10002 : emp2 {ahad si...} 