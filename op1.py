class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def speak(self):
        print(self.name,"is speaking")

Person1 = Person("Mark","46","Teacher")
print(Person1.name)
Person1.speak()

Person2 = Person("Martha","36","Accountant")
print(Person2.name)
Person2.speak()