import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.txt', sep= ";") 
print(data.head())

fig, ax = plt.subplots()
data.plot(ax=ax)
plt.show()
