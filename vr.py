import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
np.random.seed(0)
x = np.random.rand(50) * 10
y = 2 * x + 1 + np.random.randn(50) * 2  # Linear relationship with some noise

# Plot the data points
plt.scatter(x, y, label='Data Points')

# Fit a linear regression line
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
x_values = np.linspace(0, 10, 100)  # Create values for x-axis from 0 to 10
plt.plot(x_values, polynomial(x_values), color='red', label='Linear Fit')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Relationship Visualization')

# Show legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()
