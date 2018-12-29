"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 5
"""

# part A

lst = eval(input("write your list here:"))
val = eval(input("write what you want to delete from your list:"))

# Redefine lst, delete val and repeat until there is no val in lst
while val in lst:
    lst.remove(val)
print(lst)


#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW5.py
# write your list here:['to', 'be', 'or', 'not', 'to', 'be']
# write what you want to delete from your list:'to'
# ['be', 'or', 'not', 'be']
#
# Process finished with exit code 0


#part B

#the user will enter the numbers here:
a=int(input("enter the first number here:"))
b=int(input("enter the second number here:"))
c=int(input("enter the third number here:"))


#python will check if the numbers the user entered are
#fit to the conditions for the length of a triangle.
if (a+b)>c and (b+c)>a and (c+a)>b:
    #cheacking if the triangle is equilateral triangle- if it is print a note
    if a == b == c:
        print("the three numbers represent the lengths of an equilateral triangle")
    #checking if the triangle is isosceles trianle- if it is print a note
    elif a == c or c == b or a == b:
        print("the three numbers represent the lengths of an isosceles triangle")
    #if the triangle is not a equilateral or isosceles triangle- will print a note
    else:
        print("the three numbers represent the lengths of an scalene triangle")
#will print a note if the numbers can't be length of a triangle
else:
    print("the three numbers can not represent the lengths of a triangle")

# #C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter the first number here:1
# enter the second number here:1
# enter the third number here:1
# the three numbers represent the lengths of an equilateral triangle
#
# Process finished with exit code 0


#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter the first number here:5
# enter the second number here:5
# enter the third number here:8
# the three numbers represent the lengths of an isosceles triangle
#
# Process finished with exit code 0

# #C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter the first number here:3
# enter the second number here:4
# enter the third number here:5
# the three numbers represent the lengths of an scalene triangle
#
# Process finished with exit code 0

# #C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter the first number here:1
# enter the second number here:2
# enter the third number here:3
# the three numbers can not represent the lengths of a triangle
#
# Process finished with exit code 0


# create a list
lst = []

# looping 4 times over the input to append 4 numbers inside the list
for i in range(4):
    lst.append(float(input("enter a number:")))

# sorting the list from the smallest number to the biggest
lst.sort()

# printing the 2 middle values
print(lst[1:3])

# #C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter a number:101.35
# enter a number:4000
# enter a number:11
# enter a number:-41
# [11.0, 101.35]
#
# Process finished with exit code 0



