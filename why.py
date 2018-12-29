"""

# Kareen Sade id: 304924327
# Curse: Python
HW 10

"""

#creating a function that will get a parameter (positive whole number) and
# reaturning a number that his order of numbers is reverse to the parameter.
def reverse(n):
    #truning the parameter into a string
    st=str(n)
    #reverse the order of notes inside the string
    st=st[::-1]
    #turning the string into a number
    return int(st)

#print(reverse(1234567))
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/why.py
#7654321
#Process finished with exit code 0

#creating a function that is checking if a number is a polindrom and returining True for palindrom
#and False for not palindrom
def isPalindrome(n):
    if reverse(n) == n:
        return True
    else:
        return False

#print(isPalindrome(1234567), isPalindrome(1234321))
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/why.py
#False True
#Process finished with exit code 0

#creating a function that check if a number is primarily or not and returning True for primaraly
#and False for not primarily
def isPrime(n):
    #if the number is 1 or 0, it is not a primarily number, if not the function will continue to check the number
    if n == 1 or n == 0:
        return False
    #checking if the number can be diveided with one of the numbers that is smaller than him without reminder.
    #if it does, than the number is not primarily, if it dosn't the number is primarily.
    for x in range(2,n):
        if n % x == 0:
            return False
        else:
            continue
    return True

#print(isPrime(7), isPrime(10))
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/why.py
#True False
#Process finished with exit code 0

#creating a function that find an n number of the first primarily numbers that are also polindroms.
def palindromePrimes(n):
    x=2
    #creating a group that will save all the primarily-polindrom number the function will find
    primarily=[]
    #running the check until we get to n number of primarily-polindrom number the function will find
    while len(primarily) < n:
        #checking if the number is primarily-polindrom number, if it is adding it to the primarily list
        if isPrime(x) and isPalindrome(x):
            primarily.append(x)
        #redifine x in order to check the next number
        x += 1
    print(primarily)

# palindromePrimes(10)
# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/why.py
# [2, 3, 5, 7, 11, 101, 131, 151, 181, 191]
# Process finished with exit code 0

#creating a function that gets an parameter and print all the pairs of numbers that are smaller than the parameter
#and that they are both primarily and the skip between then is on 2 numbers
def twinPrimes(n):
    #creating 2 groups- one for the primeraly numbers that are smaller than n and one for the primarily-twin-pairs.
    prime=[]
    twin_prime=[]
    #searching for primarily number that are smaller than n and adding them to the prime list.
    for x in range(0,n):
        if isPrime(x):
            prime.append(x)
    #searching in prime list for pairs that between them is 2 and add them to twin_prime lise.
    for index in range(1,len(prime)):
        y= index - 1
        if prime[index] - prime[y] == 2:
            twin_prime.append((prime[y],prime[index]))
    print(twin_prime)

#twinPrimes(100)
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/why.py
#[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
#Process finished with exit code 0
