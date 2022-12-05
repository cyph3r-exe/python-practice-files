#learning classes in python
class Employee: 
    def __init__(self, first, last, pay):
        self.fname = first 
        self.lname = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
    
    def fullname(self): #creating a method which returns the full name.
        return '{} {}'.format(self.fname, self.lname)

#setting variables
bro = Employee('Debangshu', 'Roy', 300000)

print(bro.email)
print(bro.fullname())