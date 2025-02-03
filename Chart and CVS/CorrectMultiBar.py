import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
x_indexes = np.arange(len(ages_x))
width = 0.25
plt.bar(x_indexes - width, dev_y, width = width, color="k", label="All dev")
py_dev_y = [29500, 32000, 35840, 38500, 41200, 44500, 47800, 50200, 53400, 56200, 59800]
plt.bar(x_indexes, py_dev_y, width = width, color="y", label="Python Dev")
js_dev_y = [41000, 43500, 46200, 48900, 51400, 54200, 57600, 60500, 63200, 65800, 69100]
plt.bar(x_indexes + width, js_dev_y, width = width, color="b", label="JavaScript Dev")

plt.legend()
plt.title("Median Salary (USD) by Age")
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")
plt.tight_layout()
plt.savefig("CorrectMultiBar.png")
plt.show()
