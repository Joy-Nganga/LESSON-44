#write a program to creat a class with name Student and perform the following tasks
#  Create a class variable grade and name Create a function to print a sentence
#  Create a function to print class variables grade and name
#  Create an object of class Student
#  Call the two functions to execute them

class student:
    #class variables
    grade=10
    name="Tabassum"

def display(self):
    print("hi ia a student")
def intro(self):
    print("i am {} studying in grade {}".format(self.name,self.grade))

stud1=student()
stud1.display()
stud1.intro()       