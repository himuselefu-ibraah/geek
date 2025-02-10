#parent/super/base class
class Animal:
    def speak(self):
        print("Animal is speaking")


#chid/sub/derived class
class Dog(Animal):   #how to inherit (NAME OF CLASS YOU WANT TO INHERIT)
    def Bark(self):
        print("Dog is barking")



class Cat:
    def Meow(self):
        print("Cat is meowing")

a = Animal()
d = Dog()
c = Cat()

