
import re

t="dkjf, dmjk, rjfhjk"
print(re.findall(r"\b\w+\b",t))

#%%
x="xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp"
print(re.findall(r"\b\w*d\w*e\w*\b",x))
#['chdsye847', 'hedle3455', 'xjhd53e', 'de37dp']
#%%
print(re.findall(r"\b\w*e\w*d\w*\b|\b\w*d\w*e\w*\b",x))
#['eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', 'de37dp']

#%%
print(re.findall(r"\b\w*\d{3,}\w*\b",x))
#['xkn59438', 'chdsye847', 'hedle3455']

#%% Question 2

fd=open("txthw8.txt","r")
lines=fd.readlines()
fd.close()
for line in lines:
    if re.search(r"From\s\w+@\w*(\.\w*)*\s\w{3}\s\w{3}\s+\d\s\d{1,2}:\d{1,2}:\d{1,2}\s\d{4}",line):
        print(line)

# From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
# From zqian@umich.edu Fri Jan  4 16:10:39 2008
# From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
# From zqian@umich.edu Fri Jan  4 15:03:18 2008
# From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008
# From cwen@iupui.edu Fri Jan  4 11:37:30 2008
# From cwen@iupui.edu Fri Jan  4 11:35:08 2008
# From gsilver@umich.edu Fri Jan  4 11:12:37 2008
# From gsilver@umich.edu Fri Jan  4 11:11:52 2008
# From zqian@umich.edu Fri Jan  4 11:11:03 2008
# From gsilver@umich.edu Fri Jan  4 11:10:22 2008
# From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008
# From zqian@umich.edu Fri Jan  4 10:17:43 2008
# From antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008
# From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008
# From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008
# From ray@media.berkeley.edu Thu Jan  3 17:07:00 2008
# From cwen@iupui.edu Thu Jan  3 16:34:40 2008
# From cwen@iupui.edu Thu Jan  3 16:29:07 2008
# From cwen@iupui.edu Thu Jan  3 16:23:48 2008

#%%
fd=open("txthw8.txt","r")
lines=fd.readlines()
fd.close()
for line in lines:
    if re.search(r"From\s\w+@\w*(\.\w*)*\s\w{3}\s\w{3}\s+\d\s\d{1,2}:\d{1,2}:\d{1,2}\s\d{4}",line):

        print(line[5:])

# louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
# zqian@umich.edu Fri Jan  4 16:10:39 2008
# rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
# zqian@umich.edu Fri Jan  4 15:03:18 2008
# rjlowe@iupui.edu Fri Jan  4 14:50:18 2008
# cwen@iupui.edu Fri Jan  4 11:37:30 2008
# cwen@iupui.edu Fri Jan  4 11:35:08 2008
# gsilver@umich.edu Fri Jan  4 11:12:37 2008
# gsilver@umich.edu Fri Jan  4 11:11:52 2008
# zqian@umich.edu Fri Jan  4 11:11:03 2008
# gsilver@umich.edu Fri Jan  4 11:10:22 2008
# wagnermr@iupui.edu Fri Jan  4 10:38:42 2008
# zqian@umich.edu Fri Jan  4 10:17:43 2008
# antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008
# louis@media.berkeley.edu Thu Jan  3 19:51:21 2008
# louis@media.berkeley.edu Thu Jan  3 17:18:23 2008
# ray@media.berkeley.edu Thu Jan  3 17:07:00 2008
# cwen@iupui.edu Thu Jan  3 16:34:40 2008
# cwen@iupui.edu Thu Jan  3 16:29:07 2008
# cwen@iupui.edu Thu Jan  3 16:23:48 2008

##%
l="CAGATCCTAGCGTGCACGGCCCCTCCTGAGTCAGGAA"
print(len(l))
