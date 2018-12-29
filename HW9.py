"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 9
"""


# part 1


def countDigits(num):
    """
    creating a new function that count the number of digits in a number and return it
    :param num: number
    :return: the number of digits in the number
    """
    if num == 0:
        return 1
    numDigits = 0
    while num > 0:
        numDigits += 1
        num = num // 10
    return numDigits


# part 2
def compString(str1, str2):
    return True if str1.lower() == str2.lower() else False


# part 3
def sameVowels(str1, str2):
    """
    checking if the vowles in str1 is equal to the vowles in str2
    :param str1: string
    :param str2: string
    :return: true or false
    """
    vowels = {'a', 'e', 'o', 'u', 'i'}
    # creating a dictionary per each strings vowels
    dictionary_vow_1 = {}
    dictionary_vow_2 = {}

    # looping on letters on str1- if they are vowels add to dictionary_vow_1 when key is letter and value is 1
    # if they are already in dictionary_vow_1, defined the new value as value+1
    for letter in str1:
        if letter in vowels:
            if letter in dictionary_vow_1:
                dictionary_vow_1[letter] = dictionary_vow_1[letter] + 1
            else:
                dictionary_vow_1[letter] = 1
        else:
            continue

    # looping on letters on str2- if they are vowels add to dictionary_vow_2 when key is letter and value is 1
    # if they are already in dictionary_vow_2, defined the new value as value+1
    for letter in str2:
        if letter in vowels:
            if letter in dictionary_vow_2:
                dictionary_vow_2[letter] = dictionary_vow_2[letter] + 1
            else:
                dictionary_vow_2[letter] = 1
        else:
            continue
    # checking if both dictionarys are equal- if there is return True, else- False
    return True if dictionary_vow_1 == dictionary_vow_2 else False


# Examples
# Part 1
print(countDigits(5))
print(countDigits(12345))
# 1
# 5
# Part 2
print(compString('help', 'Help'))
print(compString('heslp', 'Help'))
print(compString('help', 'Help'))
# True
# False
# True

# Part 3
print(sameVowels('this is is', 'this is nt is'))
print(sameVowels('this is is', 'this is not is'))
print(sameVowels('this is is u t o', 'tuohis is nt )is'))
# True
# False
# True
