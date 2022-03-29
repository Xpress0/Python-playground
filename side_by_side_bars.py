from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here

plt.figure(figsize=(10,8))
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(middle_school_a) # Number of sets of bars
w = .8 # Width of each bar
school_a_x = create_x(t,w,n,d)
plt.bar(school_a_x, middle_school_a)

t = 2
w = .8
n = 2
d = len(middle_school_b)
school_b_x = create_x(t,w,n,d) 
plt.bar(school_b_x, middle_school_b)
ax = plt.subplot()
middle_x = [(middle_school_a + middle_school_b)/2.0 for middle_school_a, middle_school_b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend(["Middle School A", "Middle School B"])
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")

plt.show()

# If you want to save the figure remove the # from the next line 
# plt.savefig("my_side_by_side.png")