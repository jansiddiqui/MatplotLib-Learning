from matplotlib import pyplot as plt

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
anomalies = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]

plt.plot(years, anomalies, color='y', marker='o', label='Global Temperature Data')
plt.xlabel('Years')
plt.ylabel('Temperature Anomalies')
plt.title('Global Temperature Anomalies Over Time')
plt.legend()
plt.tight_layout()
plt.savefig('realProblem5.png')
plt.grid(True)
plt.show()