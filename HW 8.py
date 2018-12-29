"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 8
"""

#part 1
lst1 = [1, 2, 'a', 'b']
lst2 = [(22, 'aa'), ['x'], ('3',), ('s',3)]
#creating a dictionary
d={}

#looping for all items in lst1 and creating a dictionary when all the keys are items from lst1 and all values are
#from lst2 (mathcing by the same index numbers).
for i in range(0,len(lst1)):
    d[lst1[i]] = lst2[i]
print("this is the dictionary from mission 1:", d)

#C:\ProgramData\Anaconda3\python.exe "C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW 8.py"
#{1: (22, 'aa'), 2: ['x'], 'a': ('3',), 'b': ('s', 3)}
#Process finished with exit code 0

#part2

from collections import Hashable

lst = [1,2,[22],'a','b',[33],[44],[55]]
#creating a list for the ahshable items and a list for the nonhushable items
hashable=[]
nonhashable=[]
#creating a dicionary
dict={}

#looping a test to see if item from lst is hushable- if it is- adding the item to hushable list, if not- adding
#item to nonhushable list
for item in lst:
    if isinstance(item, Hashable):
        hashable.append(item)
    else:
        nonhashable.append(item)
#looping on all items of hushable list and making them keys to new dictionary: d2. for each key, pairing a value from
#nonhushable list, when matching the two by index number.
for b in range(0, len(hashable)):
    dict[hashable[b]] = [nonhashable[b]]
print("this is the dictionary from mission 2:", dict)

#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/targil2.py
#this is the dictionary from mission 2: {1: [[22]], 2: [[33]], 'a': [[44]], 'b': [[55]]}
#Process finished with exit code 0

#part 3

dictionary = {'a':[44], 1:[22], 2:[33], 'b':[55], (22,23): 4}
#creating 3 diffrent dictionaries
d1={}
d2={}
d3={}
#creating a list of the dictionary keys
d_keys=dictionary.keys()

#cheacking for all keys in the keys list if it a int, string or other and put it in his dictionary, with his
#value from the list- dictionary. int- in d1, string in d2, tuples in d3 and other on no dictionary
for key in d_keys:
    if isinstance(key, int): d1[key]=dictionary[key]
    elif isinstance(key, str): d2[key]=dictionary[key]
    elif isinstance(key,tuple):d3[key]=dictionary[key]
    else:
        continue
#print all 3 new dictionaries.
print("dictionary of int keys:", d1)
print("dictionary of strings keys:", d2)
print("dictionary of tuples keys:", d3)

#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/targil2.py
#dictionary of int keys: {1: [22], 2: [33]}
#dictionary of strings keys: {'a': [44], 'b': [55]}
#dictionary of tuples keys: {(22, 23): 4}
#Process finished with exit code 0

