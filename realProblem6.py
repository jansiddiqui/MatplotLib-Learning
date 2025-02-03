from matplotlib import pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
sales = [1000, 1200, 1500, 1300, 1600, 1800, 2000, 2100, 1900, 2200]

plt.plot(months, sales, marker='o', label='Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig('realProblem6.png')
plt.show()