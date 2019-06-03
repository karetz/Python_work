"""

# Kareen Sade id: 304924327
# Curse: Python 

"""
str1="which witch watch which swatch watch"
print(str1.count("which"))
print(str1.count("which, 1, 4"))

#output
#2
#0

str2="which\twitch\twatch\twhich\tswatch\twatch"
print(str2.expandtabs())
print(str2.expandtabs(14))


#output
#which   witch   watch   which   swatch  watch
#which         witch         watch         which         swatch        watch


str3= "actgatgtcgactggcaatgcttgggatgc"
print(str3.find('atg'))
print(str3.find('atg', 7,30 ))

#output
#4
#17

print('Miss'.join(["Dizzy","Lizzy", "Dizzy", "Lizzy"]))

#output
#DizzyMissLizzyMissDizzyMissLizzy

str4='ObLaDiObLaDa'
print(str4.partition('La'))

#output
#('Ob', 'La', 'DiObLaDa')

str4='ObLaDiObLaDa'
print(str4.replace('La', 'Mo'))
print(str4.replace('Ob', 'Bo', 1))

#output
#ObMoDiObMoDa
#BoLaDiObLaDa

str5="Pneumonoultramicroscopicsilicovolcanoconiosis"
print(str5.split('s'))
print((str5.split('s', 4)))

#output
#['Pneumonoultramicro', 'copic', 'ilicovolcanoconio', 'i', '']
#['Pneumonoultramicro', 'copic', 'ilicovolcanoconio', 'i', '']

str6="Well, shake it up, baby, now\n(Shake it up, baby)\nTwist and shout\n"
print(str6.splitlines())
print(str6.splitlines(True))

#output
#['Well, shake it up, baby, now', '(Shake it up, baby)', 'Twist and shout']
#['Well, shake it up, baby, now\n', '(Shake it up, baby)\n', 'Twist and shout\n']

print('        madam           '.strip())
print('oliboli'.strip('oli'))

#output
#madam
#b


def my_replace(s,o,n):
    lst=[]
    for i in s:
        if i == o:
            lst.append(n)
        else:
             lst.append(i)
    s2="".join(lst)
    return s2


print(my_replace('minimalism','m', 'L' ))

#output
#LiniLalisL