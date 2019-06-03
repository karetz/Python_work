"""

# Kareen Sade id: 304924327
# Curse: Python 2
HW 3

"""
from operator import itemgetter

L=("o",0,"X"),("m",9,"K"),("p",2,"A")
L2=sorted(L, key=itemgetter(1), reverse=True)
print(L2)

L=[("o",0,"X"),("m",9,"K"),("p",2,"A")]
L.sort(key=itemgetter(2), reverse=True)
print(L)

#output
#[('m', 9, 'K'), ('p', 2, 'A'), ('o', 0, 'X')]
#[('o', 0, 'X'), ('m', 9, 'K'), ('p', 2, 'A')]


def my_sort(L):
    min_value=min(L)
    index_min=L.index(min_value)
    L.pop(index_min)
    return min_value


def sortedzip(L1,L2,L3):
    L_1=[]
    L_2=[]
    L_3=[]
    L1=L1.copy()
    L2=L2.copy()
    L3=L3.copy()

    while len(L1)>0:
        L_1.append(my_sort(L1))
    while len(L2)>0:
        L_2.append(my_sort(L2))
    while len(L3) > 0:
        L_3.append(my_sort(L3))

    return zip(L_1, L_2, L_3)

L1=[3,1,2]
L2=[5,6,4]
L3=['a','b','c']

print(list(sortedzip(L1,L2,L3)))

#output
#[(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

def my_reverse(L):
    last=L[-1]
    L.pop(-1)
    return last

def reversedzip(L1,L2,L3):
    L_1=[]
    L_2=[]
    L_3=[]
    L1=L1.copy()
    L2=L2.copy()
    L3=L3.copy()

    while len(L1)>0:
        L_1.append(my_reverse(L1))
    while len(L2)>0:
        L_2.append(my_reverse(L2))
    while len(L3) > 0:
        L_3.append(my_reverse(L3))

    return zip(L_1, L_2, L_3)

L1=[3,1,2]
L2=[5,6,4]
L3=['a','b','c']
print(list(reversedzip(L1,L2,L3)))


#output
#[(2, 4, 'c'), (1, 6, 'b'), (3, 5, 'a')]




L2=[1,2,3,4,5,6,7,""]
L2.reverse()
print(L2)

#output
#['', 7, 6, 5, 4, 3, 2, 1]

L3=[7, 6, 5, 4, 3, 2, 1]
L3.sort()
print(L3)

#output
#[1, 2, 3, 4, 5, 6, 7]

L3=[7, 6, 5, 4, 3, 2, 1]
L3.sort(reverse = True)
print(L3)

#output
#[7, 6, 5, 4, 3, 2, 1]

L4=[1,8,4,6,2]
print(sorted(L4))

#output
#[1, 2, 4, 6, 8]

l=[(2, 4, 'c'), (1, 6, 'b'), (3, 5, 'a')]

def unzippy(list_k):
    n=len(list_k[0])
    l2=[[] for i in range(n)]
    for tup in list_k:
        for index, item in enumerate(tup):
            l2[index].append(item)
    return l2

print(unzippy(l))

#output
#[[2, 1, 3], [4, 6, 5], ['c', 'b', 'a']]


import copy
the_list=[1,2,['a', 'b'],3]
the_deepcopy_list=copy.deepcopy(the_list)
the_deepcopy_list[2][0]='banana'

print("this is the first list:", the_list)
print(" this is the deepcopy list:", the_deepcopy_list)

the_list=[1,2,['a', 'b'],3]
the_shallow_list=list(the_list)
the_shallow_list[2][0]='banana'

print("this is the first list:", the_list)
print(" this is the shallow list:", the_shallow_list)

#output
# this is the first list: [1, 2, ['a', 'b'], 3]
# this is the deepcopy list: [1, 2, ['banana', 'b'], 3]
# this is the first list: [1, 2, ['banana', 'b'], 3]
#  this is the shallow list: [1, 2, ['banana', 'b'], 3]


#creating a shallow copy and than remove 'b' from inner list. item will change in the_list too,
the_list=[1,2,['a', 'b'],3]
the_shallow_list=list(the_list)
the_shallow_list[2].remove('b')

print("this is the first list:", the_list)
print(" this is the shallow list:", the_shallow_list)

#creating a deepcopy copy and than remove 'a' from inner list. item will not change in the_list too.

the_list=[1,2,['a', 'b'],3]
the_deepcopy_list=copy.deepcopy(the_list)
the_deepcopy_list[2].remove('a')

print("this is the first list:", the_list)
print(" this is the deepcopy list:", the_deepcopy_list)

# #this is the first list: [1, 2, ['a'], 3]
#  this is the shallow list: [1, 2, ['a'], 3]

# this is the first list: [1, 2, ['a', 'b'], 3]
#  this is the deepcopy list: [1, 2, ['b'], 3]

