dictionary = {'a':[44], 1:[22], 2:[33], 'b':[55], (22,23): 4}
#creating 3 diffrent dictionarys
d1={}
d2={}
d3={}
d_keys=dictionary.keys()

for value in d_keys:
    if isinstance(value, int): d1[value]=dictionary[value]
    elif isinstance(value, str): d2[value]=dictionary[value]
    elif isinstance(value,tuple):d3[value]=dictionary[value]
    else:
        continue
print("dictionary of initials keys:", d1)
print("dictionary of strings keys:", d2)
print("dictionary of tuples keys:", d3)

