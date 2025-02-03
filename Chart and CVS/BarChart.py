from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(ages_x, dev_y, color="k", label="All dev")

plt.legend()
plt.title("Median Salary (USD) by Age")
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")
plt.tight_layout()
plt.savefig("BarChar.png")
plt.show()