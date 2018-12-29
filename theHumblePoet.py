"""

# Kareen Sade id: 304924327
# Curse: Python 
# HW 3
"""

from random import randint


# filling the list of options
people = ['Amir', 'Itai', 'Sheli', 'Gil', 'Tamar', 'Peter']
verbs = ['talks', 'smiles', 'sings', 'listens', 'dances']
adverbs = ['slowly', 'quickly', 'solemnly', 'loudly', 'badly']
prepositions = ['to a', 'with a', 'towards a', 'with the', 'on the']
adjectives = ['white', 'blue', 'green', 'small', 'bit', 'tall']
animatedObjects = ['fish', 'parrot', 'flower', 'dog', 'man']
inanimatedObjects = ['chair', 'lamp', 'car', 'table', 'computer']



def print_song(n):
    '''
    This function will run a loop where each loop will print
    a line from the song
    :param n: Number of lines to print
    '''
    for i in range(n):

        mynewsong = []
        # Choose a random people, verbs, adverbs, prepositions, adjectives and add it to mynewsong list
        mynewsong.append(people[randint(0,5)])
        mynewsong.append(verbs[randint(0,4)])
        mynewsong.append(adverbs[randint(0,4)])
        mynewsong.append(prepositions[randint(0,4)])
        mynewsong.append(adjectives[randint(0,5)])

        # Connect both animatedObjects and inanimatedObjects to one group
        # so the randint will have to choose only from one group, choose one and add to the list
        new_line=animatedObjects+inanimatedObjects
        mynewsong.append(new_line[randint(0,9)])
        print(mynewsong)

if __name__ == '__main__':

    # program input

    print_song(int(input("choose a number between 1-10:")))

#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/theHumblePoet.py
# choose a number between 1-10:10
# ['Gil', 'talks', 'loudly', 'towards a', 'green', 'car']
# ['Gil', 'dances', 'solemnly', 'with the', 'green', 'dog']
# ['Amir', 'smiles', 'solemnly', 'with a', 'small', 'man']
# ['Itai', 'sings', 'slowly', 'towards a', 'green', 'table']
# ['Amir', 'listens', 'solemnly', 'with the', 'green', 'fish']
# ['Tamar', 'talks', 'quickly', 'on the', 'white', 'chair']
# ['Tamar', 'sings', 'solemnly', 'to a', 'white', 'flower']
# ['Peter', 'listens', 'loudly', 'on the', 'small', 'dog']
# ['Amir', 'listens', 'solemnly', 'to a', 'white', 'computer']
# ['Peter', 'talks', 'quickly', 'to a', 'green', 'table']
#
# Process finished with exit code 0

