class Student:
    def __init__(self,name,roll):
        self.name=name 
        self.roll=roll
def display(self):
    print(f"Name:{self.name},Roll Number:{self.roll}")
student_list=[]
n=int(input("Enter details of students you want to add:"))
for i in range(n):
    print(f"\n enter details of student{i+1}")
    Name=input("enter name")
    roll=input("enter roll no")

obj = Student(name ,roll)
Student_list.append(obj)

