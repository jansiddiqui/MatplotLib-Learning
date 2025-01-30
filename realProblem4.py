from matplotlib import pyplot as plt

sepal_length = [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9]
sepal_width = [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1]

plt.plot(sepal_length, sepal_width, color='k', marker='_', label='Iris Data')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig('realProblem4.png')
plt.show()
