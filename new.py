"""

# Kareen Sade id: 304924327
# Curse: Python 
H.W 4
"""
# part A

lst = eval(input("write your list here:"))
val = eval(input("write what you want to delete from your list:"))

# now we will find the number of times val is in lst
# so we will know how many times to run remove() later
x = lst.count(val)

# Redefine lst and repeat it x times
for i in range(x):
    lst.remove(val)
print(lst)

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new.py
# write your list here:['to', 'be', 'or', 'not', 'to', 'be']
# write what you want to delete from your list:'to'
# ['be', 'or', 'not', 'be']
#
# Process finished with exit code 0

# part B
# porgram getting a value from user.
#program can't use items that are not Phyton data types
x = eval(input("enter your value here:"))

# define new list- one for pairs and other for odds.
pairs = []
odds = []

#if value=list, it will print 2 list- one of pairs and one of odds
#if value= not list it will print one empty list
if type(x) == list:
    for item in x:
        if type(item) == int:
            if item % 2 == 0:  # use module to check pairs
                pairs.append(item)
            elif item % 2 == 1:  # use module to check odds
                odds.append(item)
    print(pairs)
    print(odds)
else:
    print([])

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new2.py
# enter your value here:'hi'
# []
#
# Process finished with exit code 0

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new2.py
# enter your value here:[1,3,4,8,'hi',9,10]
# [4, 8, 10]
# [1, 3, 9]
#
# Process finished with exit code 0

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new2.py
# enter your value here:[2,'hi',8,'fish',112]
# [2, 8, 112]
# []
#
# Process finished with exit code 0


# part C
#program getting list from user, and a number.
#the program will shift the items in the list as a function
#  of the number. in a circle.
lst = eval(input("enter list:"))
n = eval(input("enter number of steps you want the item to move in the list:"))

if n > 0:
    for i in range(n):
        a = lst[0]
        lst = lst[1:]
        lst.append(a)
elif n < 0:
    for i in range(-n):
        b = lst.pop()
        lst.insert(0, b)
print(lst)

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter list:[1, 2, 3, 4, 5]
# enter number of steps you want the item to move in the list:0
# [1, 2, 3, 4, 5]
#
# Process finished with exit code 0

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter list:[1, 2, 3, 4, 5]
# enter number of steps you want the item to move in the list:1
# [2, 3, 4, 5, 1]
#
# Process finished with exit code 0

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new3.py
# enter list:[1, 2, 3, 4, 5]
# enter number of steps you want the item to move in the list:-1
# [5, 1, 2, 3, 4]
#
# Process finished with exit code 0
