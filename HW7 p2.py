
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

fd=open("txthw8")


