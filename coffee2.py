from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
ax = plt.subplot()
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
plt.xlabel("Amazing Drinks")
plt.ylabel("Milk in ounces")
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()
