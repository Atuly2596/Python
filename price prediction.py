from sklearn import linear_model as lm
import matplotlib.pyplot as plt


area = [[500], [550], [625], [425], [700], [575], [1000]]
prices = [15000, 18000, 22000, 14000, 2000, 16000, 30000]

l = lm.LinearRegression()
l.fit(area,prices)

x = input("Enter area\n")

y = l.predict(x)

print(y)

plt.scatter(area, prices, c ="blue")
plt.scatter(x, y, c ="red")
plt.xlabel("Area in meter squares")
plt.ylabel("prices")
plt.title("housing prices")
plt.show()