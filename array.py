courses=["Mit","Cybersecurity","Data science"]
print(courses)

#accesing an element
print(courses[2])

#looping through an array
for a in courses:
    print("course is",a)

    #adding a new element into an array

courses.append("Laravel")
print(courses)

#deleting
courses.remove("Cybersecurity")
print(courses)