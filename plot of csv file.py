import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('C:\Users\Atul yadav\Downloads\GOOG.csv')
plt.scatter(data["Open"],data["Close"])
plt.xscale('log')
plt.yscale('log')
plt.xlabel("OPEN")
plt.ylabel("CLOSE")
plt.title("Stocks")
plt.show()
