# built in functions/starndard library
from types import new_class

y = max(
    67,56,89,95,90,34,38
)
print("The max value is:",y)


x = min(
    67,56,89,95,90,34,38
)
print("The min value is:",x)

#user-defined functions
def name():
    print("ibraah")
name() #calling a function

def multiply():
    x=10
    y=7
    print(x*y)
multiply()

#parameter/variable and arqument/value stored in a variable
def add(a,b):

    print(a+b)
add(60,7)
add(6,5)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)
employee("Musa","Male","CEO","560000",72)
employee("JOHN","Male","Director","560000",49)
employee("Mary","Female","HR","560000",45)
employee("Aisha","Female","Sec","560000",24)

# A PROGRAM THAT DISPLAYS DETAILS OF 5 STUDENT
#USE A USER DEFINED FUNCTION WITH PARAMETERS AND ARQUMENT
#FULLNAME,AGE,COURSE,GENDER

def Students(Fullname,age,gender,course):
    print(Fullname,age,gender,course)
Students("isaac",21,"male","mit")
Students("martin",24,"male","comp science")
Students("braian",22,"male","engineering")
Students("mido",21,"male","mit")
Students("arnest",25,"male","it")
Students("munga",27,"male","data science")
Students("joy",20,"female","hr")
Students("mary",21,"female","cybersecurity")

