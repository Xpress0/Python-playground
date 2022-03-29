from matplotlib import pyplot as plt

# This will have data by year based on the number of bedrooms and price per square foot

x_labels = ["Studio", "1-BR", "2-BR", "3-BR", "4+-BR"]
x = [0,1,2,3,4]
y0 = [1632, 1918,2498,3041, 4000]
y1 = [1677, 2024, 2627,3367, 4400]
y2 = [1563,1908,2490,3304,4375]

ax = plt.subplot()
plt.plot(x,y0, color="gold", marker='o')
plt.plot(x, y1, color="blue", marker='o')
plt.plot(x,y2, color ="green", marker='o')
ax.set_xticks([0,1,2,3,4])
ax.set_xticklabels(x_labels)
ax.yaxis.set_major_formatter('${x:1.0f}')
plt.title("Rental Rates in Arlington County")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Amount in Dollars")
plt.legend([2019,2020,2021], loc=4)
plt.show()