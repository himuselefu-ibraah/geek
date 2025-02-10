temp=45
if temp >25 :
    print("It is cold")
else:
    print("it is too cold")


#a program tht returns the smallest number


first=67
second=90
third=13

if first <second and first <third:
    print(first,"is the smallest number")
elif second < first and second < third:
    print(second,"is the smallest number")
else:
    print(third,"is the smallest number")

num=0,1,2,3,4,5,6,7,8,9,10,11
for num in range (0,11):


    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

