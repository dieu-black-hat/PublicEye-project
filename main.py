import numpy as np

# Create a NumPy array
data = np.array([1, 2, 3, 4, 5])

# Perform basic operations
squared = data ** 2
mean_value = np.mean(data)
std_deviation = np.std(data)

# Print results
print("Original data:", data)
print("Squared data:", squared)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)