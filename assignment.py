# A program to check whether a year is leap or not

# A program to check whether a letter is a consonant or vowel

num = 2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011
for num in range(2000,2011):
    if num % 4==0:
        print(f"{num} is leap")
    else:
        print(f"{num} is not leap")

letters= "a,b,c,d,e,f,g,h,k,l,m,n,o,p,s,t,u,q,r,z,x,w,j,y,z"
letters_list = letters.split(",") #splits the string into a list of letters
vowels ="aeiou"
for letter in letters_list: #goes thru each letter and checks if its in the vowels string.
    if letter in vowels:
        print(letter,"is a vowel")
    else:
        print(letter,"is a consonant")