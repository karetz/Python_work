"""

# Kareen Sade id: 304924327
# Curse: Python
#HW 7

"""
#part 1
import string

# the program is asking the user to enter his data and explain him/her how to do it.
user_string=eval(input("please enter a string of 3 seprate words (example: 'first second third'):"))

# creating a list from the string input of the user, for checking use.
wordList = user_string.split()
# creating a set of all english vowles
vow = set('aeiouAEIOU')

# first and last 13 english letters, in both uppercase and lowercase
first13l = set(string.ascii_letters[:13] + string.ascii_letters[27:40])
letters_n_forward = set(string.ascii_letters[13:26] + string.ascii_letters[39:])

# taking vowles out of the first and last 13 letters of the abc
consonants = first13l - vow
consonants_selected = letters_n_forward - vow


# Checking if the input is valid. if not- sending an error massage and finish the program.
if isinstance(user_string, str):
    if len(wordList) == 3:
        tupleList = []
        for word in wordList:
            tupleList.append((vow & set(word), consonants & set(word), consonants_selected & set(word)))

        print(tupleList)
        print(tupleList[0])
        print(tupleList[1])
        print(tupleList[2])
    else:
        print("error- the squense you entered is incorrect")

#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW7.py
#please enter a string of 3 seprate words (example: 'first second third'):"people enjoy programming"
#[({'e', 'o'}, {'l'}, {'p'}), ({'e', 'o'}, {'j'}, {'n', 'y'}), ({'a', 'i', 'o'}, {'m', 'g'}, {'p', 'n', 'r'})]
#({'e', 'o'}, {'l'}, {'p'})
#({'e', 'o'}, {'j'}, {'n', 'y'})
#({'a', 'i', 'o'}, {'m', 'g'}, {'p', 'n', 'r'})

#Process finished with exit code 0


#part 2

# asking the user to enter the name list and turing it into a list
names=list(eval(input("write the name list here:")))
#creating a list of people that got in the hotel
names_2=[]

#looping all the entrence of guests and decide what will be the greeting of the guard of the hotel toword them
for name in names:
    if name in names_2:
        print('Good to see you again', name)
    elif name not in names_2:
        print("Welcome", name)
        names_2.append(name)

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/targil2.py
# write the name list here:["David", "Orly", "Neta", "Peleg", "Carol", "Ezra", "Irina", "Orly", "Shir", "Neta", "Sheli", "Neta", "Ezra", "Yosi"]
# Welcome David
# Welcome Orly
# Welcome Neta
# Welcome Peleg
# Welcome Carol
# Welcome Ezra
# Welcome Irina
# Good to see you again Orly
# Welcome Shir
# Good to see you again Neta
# Welcome Sheli
# Good to see you again Neta
# Good to see you again Ezra
# Welcome Yosi

# Process finished with exit code 0


#part 3
import random
#creating a set for the random numbers
set_random=set()

#program will loop until it will add 10 diffrent random numbers to the set
while len(set_random)<10:
    x=random.randint(1,50)
    set_random.add(x)

print(set_random)

# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/targil2.py
# {32, 34, 4, 41, 45, 14, 17, 18, 21, 31}

# Process finished with exit code 0

