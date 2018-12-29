"""

# Kareen Sade id: 304924327
# Curse: Python
# THE CODE IS TCCCTAGCTAAGTGAATTCTATGAATGGACTGTCCCCAAAGAAGTAGGACCCACTAATGCAGA

"""

s=input("write dna code")

s2=s.replace('A','X')
s2=s2.replace('T','A')
s2=s2.replace('X','T')
s2=s2.replace('G','Y')
s2=s2.replace('C','G')
s2=s2.replace('Y','C')

print('the original dna sequence is:')
print(s)
print('the dna complementary sequence is: ')
print(s2)

NbAdna=s.count('A')
NbTdna=s.count('T')
NbGdna=s.count('G')
NbCdna=s.count('C')

print('number of times A in original sequence: ',NbAdna )
print('number of times T in original sequence: ',NbTdna )
print('number of times C in original sequence: ',NbCdna )
print('number of times G in original sequence: ',NbGdna )

NbAdna2=NbTdna
NbTdna2=NbAdna
NbCdna2=NbGdna
NbGdna2=NbCdna

print('number of times A in complementary sequence is: ', NbAdna2)
print('number of times T in complementary sequence is: ', NbTdna2)
print('number of times C in complementary sequence is: ', NbCdna2)
print('number of times G in complementary sequence is: ', NbGdna2)

NCG=NbGdna+NbCdna
PCG=(NCG/len(s))*100
print('C+G PERCENT IN THE ORIGINAL SEQUENCE IS: ', PCG)

NAT=NbAdna+NbTdna
PAT=(NAT/len(s))*100
print('A+T PERCENT IN THE ORIGINAL SEQUENCE IS: ', PAT)


#Run-
# C:\ProgramData\Anaconda3\python.exe C:/Users/sadek/OneDrive/Documents/Hebrew_University/Semester1/untitled/targil.py
# write dna codeTCCCTAGCTAAGTGAATTCTATGAATGGACTGTCCCCAAAGAAGTAGGACCCACTAATGCAGA
# the original dna sequence is:
# TCCCTAGCTAAGTGAATTCTATGAATGGACTGTCCCCAAAGAAGTAGGACCCACTAATGCAGA
# the dna complementary sequence is:
# AGGGATCGATTCACTTAAGATACTTACCTGACAGGGGTTTCTTCATCCTGGGTGATTACGTCT
# number of times A in original sequence:  21
# number of times T in original sequence:  14
# number of times C in original sequence:  15
# number of times G in original sequence:  13
# number of times A in complementary sequence is:  14
# number of times T in complementary sequence is:  21
# number of times C in complementary sequence is:  13
# number of times G in complementary sequence is:  15
# C+G PERCENT IN THE ORIGINAL SEQUENCE IS:  44.44444444444444
# A+T PERCENT IN THE ORIGINAL SEQUENCE IS:  55.55555555555556
#
# Process finished with exit code 0

