from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.figure(figsize=(10,8))
plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.legend(payment_method_names)
plt.axis('equal')

plt.show()