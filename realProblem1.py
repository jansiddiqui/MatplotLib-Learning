from matplotlib import pyplot as plt

days = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stock_price = [100, 102, 105, 107, 110, 108, 109, 112, 115, 120]

plt.plot(days, stock_price, color='b', linestyle='--', marker='.', label='Stock Price')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Stock Price Visualization')
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.savefig('realProblem1.png')
plt.show()
