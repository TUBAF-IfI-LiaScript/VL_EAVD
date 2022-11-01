import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.txt', sep= ";") 
print(data.head())

fig, ax = plt.subplots()
data.plot(ax=ax)
plt.show()


#import pandas as pd
#import matplotlib.pyplot as plt
#
#data = pd.read_csv('data.txt', sep= ";") 
#print(data.head())
#
#data["time"] = data.index * 0.05
#
#fig, ax = plt.subplots()
#data.plot(x="time", y=["X", "Y", "Z"], ax=ax)
#ax.set_xlabel("Measurement index")
#ax.set_ylabel("Acceleration (10Bit resolution)")
#plt.show()
