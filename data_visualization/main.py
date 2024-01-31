import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

input_values = range(1, 1001)
squares = [x**2 for x in input_values]

# Using the inbuilt styles
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.scatter(input_values, squares, s=10)

# Set chart title and label axes. 
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis. 
ax.axis([0, 1100, 0, 1_100_100])

# Set size of tick labels. 
ax.tick_params(labelsize=14)

plt.show()
