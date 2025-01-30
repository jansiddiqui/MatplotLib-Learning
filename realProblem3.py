from matplotlib import pyplot as plt

genders = ['Male', 'Female']
survival_count = [100, 200]

plt.plot(genders, survival_count, color='g', linestyle=':', marker='v', label='Titanic Data')
plt.xlabel('Gender')
plt.ylabel('Survival Count')
plt.title('Survival Rates by Gender')
plt.legend()
plt.savefig('realProblem3.png')
plt.tight_layout()
plt.show()
