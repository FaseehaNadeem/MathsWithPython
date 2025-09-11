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
