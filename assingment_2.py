#question 1
a="Python is a case sensitive language"                     #defining the given string
print("length of string is:",len(a))
rev_a=a[::-1]                                                #reversing the order by using slicing of string       
print("reversed string is ",rev_a)
new_str=a[10:26]                                             #slicing the required substring 
print("substring is\n",new_str)
b=a.replace("a case sensitive","object oriented")            #replacing the given sustring
print("string with replaced words is",b)
print("index of a is",a.index("a"))                          #finding index of a in string a
print("string with removed spaces is",a.replace(" ",""))     #removing all the spaces


#question 2
SID=21103042                                 #defining SID
name="Akshit Saini"                          #defining name
department="Computer Science"                #defining department
CGPA=9.8                                     #defining CGPA
str="""Hey,{0} Here!
My SID is {1}
I am from {2} department and my CGPA is {3}""" #defining string to be formatted
          #formatting string
print(str.format(name,SID,department,CGPA))


#question 3
a=56
b=10
print("a is",a,"b is",b)
# part a 
print("a&b is",a&b)
# part b
print("a|b is",a|b)
# part c 
print("a^b is",a^b)
# part d left shift of a and b with 2 bits
print("left shift of a and b with 2 bits is")
print(a>>2)
print(b>>2)
# part e right shift of a and b with 2 bits
print("right shift of a and b with 2 bits is")
print(a<<2)
print(b<<2)


#question 4
a=[]                              #defining a list
for i in range(3):
  print("enter number",i+1)        #entering elements in list using loop
  a.append(int(input()))
a.sort()                          #sorting the numbers in list so that they are in increasing order  
print(a[-1],"is the maximum number")  #maximum number is number with last index in list



#question 5
str=input("input a string\n")   #entering a string
print("Is \"name\" in string ?")
if "name" in str: 
  print("Yes")                #checking if name is in the string
else:
  print("No")


#question 6
print("enter three sides of triangle")  #taking three sides of triangles from user
a=int(input())
b=int(input())
c=int(input())
print("Is the triangle possible?")
if (a<(b+c))and(b<(c+a))and(c<(b+a)):
 print("Yes")                           #checking the condition if side is less than sum of other two
else:
 print("No")

