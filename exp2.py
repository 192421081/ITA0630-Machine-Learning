import numpy as np

data = np.array([
['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
['Sunny','Warm','High','Strong','Warm','Same','Yes'],
['Rainy','Cold','High','Strong','Warm','Change','No']
])

S = ['0']*6
G = ['?']*6

for row in data:
    if row[-1]=='Yes':
        for i in range(6):
            if S[i]=='0':
                S[i]=row[i]
            elif S[i]!=row[i]:
                S[i]='?'
    else:
        for i in range(6):
            if S[i]!=row[i]:
                G[i]=S[i]

print("S:",S)
print("G:",G)
