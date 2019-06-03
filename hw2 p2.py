"""

# Kareen Sade id: 304924327
# Curse: Python 

"""
#a

b=str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvustrqponmlkjihgfedcba")
a="donafabiola"
print(a.translate(b))

#output
#wlmzuzyrloz

b=str.maketrans("efghijklmnopqrstuvwxyz", "zyxwvustrqponmlkjihgfe", "abcd")
a="donafabiola"
print(a.translate(b))

#output
#pqyvpt

#b
#string

str1="iblameitonmyaddbaby"
print(str1[1:6])
print(str1[1:8:2])
print(str1[8:1:-1])

#output
#blame
#baet
#otiemal

#list
lst=["italy","Humpty",9,"Dumpty","order", "was", 11, "pushed"]
print(lst[1:9])
print(lst[1::2])
print(lst[7:3:-2])

#output
#['Humpty', 9, 'Dumpty', 'order', 'was', 11, 'pushed']
#['Humpty', 'Dumpty', 'was', 'pushed']
#['pushed', 'was']

#tuple
t=(1, "this","get", "gag", "is", 8, "", "sparta!!")
print(t[5:6])
print(t[1::3])
print(t[5::-5])

#output
#(8,)
#('this', 'is', 'sparta!!')
#(8, 1)


s="skyscanner"
print(s.index("y"))
print(s.index("n", 7, 10))

#output
#2
#7

L=["b", 0, "dog", 777]
L.insert(2,"a")
print(L)

#output
#['b', 0, 'a', 'dog', 777]

L1=["last", "item", "is", "removed", "and", "returned"]
L1.pop()
print(L1)

#output
#['last', 'item', 'is', 'removed', 'and']

L1=["last", "item", "is", "removed", "and", "returned"]
L1.pop(2)
print(L1)

#output
#['last', 'item', 'removed', 'and', 'returned']

L2=[1,2,3,4,5,6,7,""]
L2.remove("")
print(L2)

#output
#[1, 2, 3, 4, 5, 6, 7]

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

