"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 6
"""

# plan A
# defining the lists and tuples

lst1=[]
tuple1=()
lst2=[]
tuple2=()

# asking the user to enter the values and insert them to the list -lst0.
lst0=list(eval(input("write you values here:")))

#reaping on the test for all the list-lst0
for item in lst0:
    #sorting the values by their types to 2 different lists (for tuples or srings)
    #and to 2 different tuples (for lists and integers).
    if type(item) == tuple:
        lst1= lst1 + list(item)
    elif type(item) == list:
        tuple1= tuple1 + (tuple(item,))
    elif type(item) == str:
        lst2.append(item)
    elif type(item) == int:
        tuple2= tuple2 + (item,)

#counting the number of integers (n) and stings (s)
n = len(tuple2)
s = len(lst2)

print(n,s)

for item in lst1:
    if type(item) == str:
        s +=1
    elif type(item) == int:
        n +=1

for item in tuple1:
    if type(item) == str:
        s +=1
    elif type(item) == int:
        n +=1

# printing the results - all the lists

print(lst1)
print(tuple1)
print(lst2)
print(tuple2)

print("the total number of strings in the sequence is:", s )
print("the total number of integers in the sequence is:", n)

# #C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW6.py
# write you values here:[1,2,'a',(11,'b'),[22,'c'],(33,),['d'],'e']
# 2 2
# [11, 'b', 33]
# (22, 'c', 'd')
# ['a', 'e']
# (1, 2)
# the total number of strings in the sequence is: 5
# the total number of integers in the sequence is: 5
#
# Process finished with exit code 0


#plan B

# the program is a game of guessing- it will choose 3 random numbers and ask the user to
# guess those numbers- then it will give the user data of his/her try
# if the user will want to end the game- he/she will need to enter the value -1.

import random

# a term for the main loop to run
term = True
odds = [0, 33, 66, 100]
# number of max correct number the user guess from all games
max_correct = 0

# main loop
while True:
    # creating a list for the random numbers the program will choose
    random_n = []
    # creating a list for the numbers the user supply
    guesses_n = []
    # creating a list for numbers the user guess correctly
    correct = []
    # number of correct number the user guess from this specific round of the game
    n_correct = 0
    # choosing 3 random numbers
    for number in range(3):
        random_n.append(random.randint(1, 10))

    for number in range(3):
        x = (int(input("enter a number (from 10-0, include) or -1 to end the game:")))
        if x == (-1):
            term = False  # this variable is used to break the while loop
            break
        else:
            guesses_n.append(x)
            if x in random_n:
                random_n.remove(x)
                correct.append(x)
                n_correct += 1
    if term is False:
        break
    print("this is the correct numbers the user guess:", tuple(correct))
    print("this is the correct numbers the user didn't guess:", random_n)
    print("the percent of correct numbers the user guess:", odds[n_correct])
    if n_correct > max_correct:
        max_correct = n_correct  # updaiting the max score

print("the game is finish! the best percent of correct number in the entire game was:", odds[max_correct])

# #C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/new2.py
# enter a number (from 10-0, include) or -1 to end the game:1
# enter a number (from 10-0, include) or -1 to end the game:2
# enter a number (from 10-0, include) or -1 to end the game:3
# this is the correct numbers the user guess: (3,)
# this is the correct numbers the user didn't guess: [8, 5]
# the percent of correct numbers the user guess: 33
# enter a number (from 10-0, include) or -1 to end the game:1
# enter a number (from 10-0, include) or -1 to end the game:2
# enter a number (from 10-0, include) or -1 to end the game:3
# this is the correct numbers the user guess: ()
# this is the correct numbers the user didn't guess: [7, 10, 10]
# the percent of correct numbers the user guess: 0
# enter a number (from 10-0, include) or -1 to end the game:-1
# the game is finish! the best percent of correct number in the entire game was: 33
#
# Process finished with exit code 0