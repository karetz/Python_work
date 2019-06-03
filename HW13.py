"""

# Kareen Sade id: 304924327
# Curse: Python 
HW 13
"""

#creating a function that take a sub-list that in index 1-6 have grades and check how many pass grade it have
#if there is at list 4 pass grades- the function will return True. else, it will return false.
def exes(grade_list):
    #creating a varible that count the number of pass grade
    check=0
    #running on all grades and check if they are pass (1) if they are- add +1 to check.
    for x in range(1, 7):
        if grade_list[x] == 1:
            check +=1
        else:
            continue
    #check if the varible check is bigger or equal to 4, if it is return True, else- return False.
    if check >= 4:
        return True
    else:
        return False

# print(exes(["Or" , 1, 1, 1, 1, 1, 95]))
# print(exes( ["Sheli", 0,0, 1, 0, 1, 60] ))
# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW13.py
# True
# False
# Process finished with exit code 0


#creating a function that increase the final score that is in last place on the list in 10%
def up(grade_list):
    #finding the score
    x=grade_list[-1]
    #removing the old score from the list
    grade_list.pop()
    #adding the new, improved score to the end of the list
    grade_list.append(x*1.1)
    return grade_list

#print(grade_list)
#up(["Or" , 1, 1, 1, 1, 1, 95])
#up(  ["Sheli", 0,0, 1, 0, 1, 60])
#C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/HW13.py
#['Or', 1, 1, 1, 1, 1, 104.50000000000001]
#['Sheli', 0, 0, 1, 0, 1, 66.0]
#Process finished with exit code 0

students = [["Dan" , 1, 0, 1, 1, 1, 90], ["Or" , 1, 1, 1, 1, 1, 95], ["Sheli", 0,0, 1, 0, 1, 60], ["Oren", 1,1,1,1,1, 80]]

#filter acording to exes
filteredStudents=list(filter(exes,students))
print(filteredStudents)
#[['Dan', 1, 0, 1, 1, 1, 90], ['Or', 1, 1, 1, 1, 1, 95], ['Oren', 1, 1, 1, 1, 1, 80]]


filteredStudentsUp=list(map(up,filteredStudents))
print(filteredStudentsUp)

# [['Dan', 1, 0, 1, 1, 1, 99.00000000000001], ['Or', 1, 1, 1, 1, 1, 104.50000000000001], ['Oren', 1, 1, 1, 1, 1, 88.0]]