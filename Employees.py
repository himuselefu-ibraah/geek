class Employee:
    def __init__(self,name,position,salary):
        self.name =name
        self.position =position
        self.salary =salary

    def details(self):
        print(self.name,"is the", self.position)


employee1 = Employee("John","manager","250000")
print(employee1.name,employee1.salary,employee1.position)
employee2 = Employee("mary","nmanager","50000")
print(employee2.name,employee2.salary,employee2.position)
employee3 = Employee("jane","hr","350000")
print(employee3.name,employee3.salary,employee3.position)
employee4 = Employee("Joseph","hr","450000")
print(employee4.name,employee4.salary,employee4.position)
employee5 = Employee("Jude","ceo","250000")
print(employee5.name,employee5.salary,employee5.position)



