from matplotlib import pyplot as plt
plt.xkcd()
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cases = [10, 20, 50, 100, 200, 400, 800, 1600, 3200, 6400]

plt.plot(days, cases, color='r', linestyle='--', marker='o', label='Covid-19 cases')
plt.xlabel('Days')
plt.ylabel('Covid-19 cases')
plt.title('Daily Covid-19 Cases')
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('realProblem2.png')
plt.show()