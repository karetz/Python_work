"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 12
"""

#qa
birthdays = [(19, 3, 1968), (6, 4, 2011), (13, 1, 1972),
             (8, 7, 2005), (28, 4, 2003), (25, 7, 1985),
             (8, 3, 1978), (22, 8, 1988), (18, 9, 1974),
             (22, 10, 2004), (25, 5, 1969), (1, 3, 1943),
             (17, 2, 1990), (23, 12, 1986), (10, 3, 2000)]

#lopping on birthday list to find the birthday months from each tuple
#  and creating a set with all the months called birthday+months
birthday_months={(date[1]) for date in birthdays }

#print(birthday_months)
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW12.py
#{1, 2, 3, 4, 5, 7, 8, 9, 10, 12}
#Process finished with exit code 0

#qb
#looping for all the months (1-12) and finding the mounths that are not in birthday_mounths set
#creating a list with all those numbers
months_without_birthdays=[(month) for month in range(1,13) if month not in birthday_months]

#print(months_without_birthdays)
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW12.py
#[6, 11]
#Process finished with exit code 0

#qc
#creating a dictionary of months as keys and empty list as values
dict_months = {val[1]:[] for val in birthdays}

# add the corresponding dates to each month
for val in birthdays:
    dict_months[val[1]].append(val[0])

# printing the number of birthdays per month
for month in dict_months:
    print("month: ", month, 'freq: ', len(dict_months[month]))
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW12.py
#month:  3 freq:  4
#month:  4 freq:  2
#month:  1 freq:  1
#month:  7 freq:  2
#month:  8 freq:  1
#month:  9 freq:  1
#month:  10 freq:  1
#month:  5 freq:  1
#month:  2 freq:  1
#month:  12 freq:  1
#Process finished with exit code 0

#qd
#lopping on birthday list to collect birthday years and putting them in new list call year
year=[date[2] for date in birthdays]
#printing the year range fron year list
print("birthday year range from the list:", min(year), "-", max(year))

#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW12.py
#birthday year range from the list: 1943 - 2011
#Process finished with exit code 0
