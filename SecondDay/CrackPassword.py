import pandas as pd 
import matplotlib.pyplot as plt
import time
import math

dictPassword = {}
passwordHolder = []
dictWithTimer = {}
data = pd.read_csv("/home/boing/Documents/Python30Days/SecondDay/PasswordList.txt", sep="    " ,header=None, dtype= str)

for i in data[0]:
    dummyList = []
    if (len(str(i)) not in dictPassword.keys()):
        dummyList.append(len(str(i)))
        dictPassword[len(str(i))] = []
    
    dictPassword[len(str(i))].append(i)
 

# brude force 
# Assume we number mix
def brudeForce(password):
    passwordHolder.clear()
    start_time = time.time()
    characterSize = len(str(password))

    for i in range(characterSize):
        passwordHolder.append(0)
    
    while(True):
        passwordTest = "".join(str(number) for number in passwordHolder)
        passwordHolder[characterSize - 1] += 1

        if (passwordTest == str(password)):
            end_time = time.time()
            print(round(end_time - start_time, 2))
            return round(end_time - start_time, 1)

        for i in range(characterSize - 1, 0, -1):
            if (passwordHolder[i] > 9):
                passwordHolder[i] = 0
                passwordHolder[i - 1] += 1
        
for key in dictPassword.keys():
    dictWithTimer[key] = []
    for number in dictPassword[key]:
        dictWithTimer[key].append(brudeForce(number))
        
df = pd.DataFrame.from_dict(dictWithTimer, orient='index').transpose()

for column in df.columns:
    plt.plot(df.index, df[column], label=column)


plt.xlabel('Amout of password')
plt.ylabel('Time (s)')
plt.title('Brute Force Time vs. Password Length')
plt.legend()

plt.show()