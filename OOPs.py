Problem Statement:
Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.
  
Code:
class Student: #class name
  def __init__(self,name,marks): #Constructor
    self.name = name #Attribute
    self.marks = marks #Attribute
  
  def get_avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print("Hi",self.name,"Your average score is",sum/3)
    
s1 = Student("Karan",[87,97,90])
print(s1.name,s1.marks)
s1.get_avg()

Problem Statement 2:
In Python, there is no dedicated inbuilt function to deal with complex numbers. 
In OOP, int has its own class, string has its own class, but complex does not have its own separate class.
That’s why in this code, a custom Complex class has been created, and the concept of dunder (magic) functions has been explained.

class Complex:
  def __init__(self,real,img):
    self.real = real
    self.img = img
  def shownumber(self):
    print(self.real,"i +",self.img,"j")
  def __add__(self, num2): #Dunder function
    newreal = self.real + num2.real
    newimg = self.img + num2.img
    return Complex(newreal,newimg)

num1 = Complex(1,3)
num1.shownumber()
num2 = Complex(4,6)
num2.shownumber()
num3 = num1 + num2
num3.shownumber()

# Dunder function Explanation:
def add(self, num2): # if we write this without slashes
num3 = num1 + num2 # and print num3 like that 
# It will give an error (unsupported operand type(s) for +)
# WHY? Because int,string and list has a defined class for this "+" operand. But complex numbers has no class to define this.
# So here, we can either write it this way
def add(self, num2):
num3 = num1.add(num2)
# or we will have to use a dunder function
def __add__(self, num2):
num3 = num1 + num2
