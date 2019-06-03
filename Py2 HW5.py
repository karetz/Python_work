"""

# Kareen Sade id: 304924327
# Curse: Python
HW 5

"""

##4##
#function that compute the sum of numbers from 1 to n.
def sum(n):
    if n>1 or n==1:
        x =n + sum(n-1)
        return x
    else:
        # print()
        return 0

print(sum(57))

#1653

#%%

##5##
#function that compute snd returns the sum of N first elements of a list L.
def elementSum(L, N=None):
    if N is None:
        N=len(L)
        print(N)
    if N>1:
        x=L[N-1] + elementSum(L, N-1)
        return x
    else:
        return L[N-1]

#L=['h','c','a','i','t','a','v','a']
#print(elementSum(L))
#avatiach


#%%

##1##

def sum_even(n):
    if n==0:
        return 0
    if n%2 == 0:
        x=n +sum_even(n-2)
        return x
    else:
        return sum_even(n-1)

#print(sum_even(1577))
#621732

#%%

##3##

def prod(L):
    if len(L)>0:
        x= L[len(L)-1] * prod(L[:len(L)-1])
        return x
    else:
        return 1

L=[2,3,5,0]
print(prod(L))
#544698000
