"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 11
"""


def readtxt(text_name):
    """
    This function read the file given, make a list of all the words and
    then create a dictionary where the key is a word and the value is the frequency
    :param text_name: path to the file
    :return: dictionary
    """
    # File operations
    dictionary = {}
    fd = open(text_name, 'r')
    text = fd.readlines()
    fd.close()

    # List of words
    word_list = []
    for sentence in text:
        word_list.extend(sentence.split())

    # Create the dictionary of word frequency
    for word in word_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] + 1
    return dictionary


def printer(dictionary, text_name):
    """
    Prints the results from the dictionay as request on the HW
    :param dictionary: Frequency dictionary
    :param text_name: Name of the file
    :return:
    """

    # Looping the keys and add the total value
    total = 0
    for key in dictionary:
        print('word: ', key, " ", 'frequency: ', dictionary[key])
        total = total + dictionary[key]
    print('number of words in', text_name, total)


def activate(text_name):
    """
    Activate combines two functions to solve question #1
    :param text_name: path to the file
    """
    dict_word = readtxt(text_name)
    printer(dict_word, text_name.split("\\")[-1])


def q2(txt1, txt2):
    """
    This function uses the functions from question 1 to generate a dictionaries of the [words,value].
    given this dictionaries it will use the keys to generate sets of words each set represents
    the words from each file and print the results as request on the HW
    :param txt1: path to the file 1
    :param txt2: path to the file 2
    :return:
    """

    # Generate sets
    txt1_dict = readtxt(txt1)
    txt2_dict = readtxt(txt2)
    txt1_set = set(txt1_dict)
    txt2_set = set(txt2_dict)

    # Printing results
    print("combind words: ", txt1_set & txt2_set)
    print("words that are only in text1: ", txt1_set - txt2_set)
    print("word that are only in text2: ", txt2_set - txt1_set)


# Running the HW
# Q1
activate(r'C:\Users\sadek\OneDrive\Documents\Hebrew_University\Semester1\untitled\text1.txt')
activate(r'C:\Users\sadek\OneDrive\Documents\Hebrew_University\Semester1\untitled\text2.txt')
# Q2
q2(r'C:\Users\sadek\OneDrive\Documents\Hebrew_University\Semester1\untitled\text1.txt',
   r'C:\Users\sadek\OneDrive\Documents\Hebrew_University\Semester1\untitled\text2.txt')
#
#  C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW11.py
# word:  Here   frequency:  10
# word:  comes   frequency:  15
# word:  the   frequency:  12
# word:  sun   frequency:  20
# word:  doo   frequency:  4
# word:  and   frequency:  5
# word:  I   frequency:  6
# word:  say   frequency:  5
# word:  It's   frequency:  6
# word:  all   frequency:  6
# word:  right   frequency:  6
# word:  Little   frequency:  6
# word:  darling   frequency:  6
# word:  it's   frequency:  4
# word:  been   frequency:  4
# word:  a   frequency:  1
# word:  long   frequency:  1
# word:  cold   frequency:  1
# word:  lonely   frequency:  1
# word:  winter   frequency:  1
# word:  it   frequency:  8
# word:  feels   frequency:  1
# word:  like   frequency:  3
# word:  years   frequency:  3
# word:  since   frequency:  3
# word:  here   frequency:  7
# word:  smiles   frequency:  1
# word:  returning   frequency:  1
# word:  to   frequency:  1
# word:  faces   frequency:  1
# word:  seems   frequency:  2
# word:  Sun   frequency:  5
# word:  feel   frequency:  1
# word:  that   frequency:  1
# word:  ice   frequency:  1
# word:  is   frequency:  1
# word:  slowly   frequency:  1
# word:  melting   frequency:  1
# word:  clear   frequency:  1
# number of words in text1.txt 163
# word:  Penny   frequency:  7
# word:  Lane   frequency:  7
# word:  there   frequency:  2
# word:  is   frequency:  10
# word:  a   frequency:  11
# word:  barber   frequency:  2
# word:  showing   frequency:  1
# word:  photographs   frequency:  1
# word:  Of   frequency:  1
# word:  every   frequency:  1
# word:  head   frequency:  1
# word:  he's   frequency:  1
# word:  had   frequency:  1
# word:  the   frequency:  15
# word:  pleasure   frequency:  1
# word:  to   frequency:  2
# word:  have   frequency:  1
# word:  known   frequency:  1
# word:  And   frequency:  4
# word:  all   frequency:  1
# word:  people   frequency:  1
# word:  that   frequency:  1
# word:  come   frequency:  1
# word:  and   frequency:  10
# word:  go   frequency:  1
# word:  Stop   frequency:  1
# word:  say   frequency:  1
# word:  hello   frequency:  1
# word:  On   frequency:  1
# word:  corner   frequency:  1
# word:  banker   frequency:  3
# word:  with   frequency:  2
# word:  motorcar   frequency:  1
# word:  The   frequency:  1
# word:  little   frequency:  1
# word:  children   frequency:  1
# word:  laugh   frequency:  1
# word:  at   frequency:  1
# word:  him   frequency:  1
# word:  behind   frequency:  1
# word:  his   frequency:  3
# word:  back   frequency:  5
# word:  never   frequency:  1
# word:  wears   frequency:  1
# word:  mac   frequency:  1
# word:  In   frequency:  3
# word:  pouring   frequency:  2
# word:  rain   frequency:  2
# word:  Very   frequency:  2
# word:  strange   frequency:  2
# word:  in   frequency:  12
# word:  my   frequency:  8
# word:  ears   frequency:  4
# word:  eyes   frequency:  4
# word:  There   frequency:  3
# word:  beneath   frequency:  3
# word:  blue   frequency:  3
# word:  suburban   frequency:  3
# word:  skies   frequency:  3
# word:  I   frequency:  3
# word:  sit   frequency:  3
# word:  meanwhile   frequency:  4
# word:  fireman   frequency:  2
# word:  an   frequency:  1
# word:  hourglass   frequency:  1
# word:  pocket   frequency:  1
# word:  portrait   frequency:  1
# word:  of   frequency:  3
# word:  Queen   frequency:  1
# word:  He   frequency:  1
# word:  likes   frequency:  1
# word:  keep   frequency:  1
# word:  fire   frequency:  1
# word:  engine   frequency:  1
# word:  clean   frequency:  2
# word:  It's   frequency:  1
# word:  machine   frequency:  1
# word:  A   frequency:  2
# word:  four   frequency:  1
# word:  fish   frequency:  1
# word:  finger   frequency:  1
# word:  pies   frequency:  1
# word:  summer   frequency:  1
# word:  Behind   frequency:  1
# word:  shelter   frequency:  1
# word:  middle   frequency:  1
# word:  roundabout   frequency:  1
# word:  pretty   frequency:  1
# word:  nurse   frequency:  1
# word:  selling   frequency:  1
# word:  poppies   frequency:  1
# word:  from   frequency:  1
# word:  tray   frequency:  1
# word:  though   frequency:  1
# word:  she   frequency:  1
# word:  feels   frequency:  1
# word:  as   frequency:  1
# word:  if   frequency:  1
# word:  she's   frequency:  1
# word:  play   frequency:  1
# word:  She   frequency:  1
# word:  anyway   frequency:  1
# word:  shaves   frequency:  1
# word:  another   frequency:  1
# word:  customer   frequency:  1
# word:  We   frequency:  1
# word:  see   frequency:  1
# word:  sitting   frequency:  1
# word:  waiting   frequency:  1
# word:  for   frequency:  1
# word:  trim   frequency:  1
# word:  Then   frequency:  1
# word:  rushes   frequency:  1
# word:  From   frequency:  1
# number of words in text2.txt 235
# combind words:  {'I', 'and', 'that', "It's", 'the', 'say', 'feels', 'all', 'to', 'is', 'a'}
# words that are only in text1:  {'faces', 'doo', 'slowly', 'darling', 'right', 'long', 'it', 'seems', 'returning', 'Little', 'cold', 'since', 'melting', 'sun', "it's", 'years', 'feel', 'smiles', 'clear', 'been', 'winter', 'Sun', 'here', 'like', 'ice', 'Here', 'comes', 'lonely'}
# word that are only in text2:  {'had', 'middle', 'head', 'an', 'tray', 'people', 'portrait', 'photographs', 'rushes', 'fireman', 'selling', 'children', 'Stop', 'Penny', 'finger', 'pouring', 'Behind', 'Of', 'little', 'skies', 'four', 'waiting', 'And', 'fire', 'poppies', 'pies', "she's", 'behind', 'in', 'barber', 'another', 'Queen', 'for', 'ears', 'mac', 'at', 'if', 'Very', 'meanwhile', 'hourglass', 'engine', 'beneath', 'anyway', 'A', 'From', 'rain', 'summer', "he's", 'as', 'of', 'He', 'banker', 'fish', 'corner', 'clean', 'pleasure', 'play', 'She', 'There', 'motorcar', 'from', 'We', 'every', 'Lane', 'come', 'with', 'sitting', 'his', 'pocket', 'never', 'keep', 'trim', 'wears', 'shelter', 'nurse', 'have', 'laugh', 'shaves', 'showing', 'hello', 'she', 'there', 'suburban', 'though', 'see', 'eyes', 'my', 'strange', 'known', 'go', 'The', 'On', 'Then', 'roundabout', 'sit', 'customer', 'back', 'likes', 'him', 'pretty', 'In', 'machine', 'blue'}
#
# Process finished with exit code 0
