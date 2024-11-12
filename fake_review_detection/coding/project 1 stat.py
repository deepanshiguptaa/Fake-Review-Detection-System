# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import statistics

# Sample Dataset
data = [15, 28, 11, 10, 29, 35, 44, 30, 55, 12]

# Central Tendency
mean_value = np.mean(data)
median_value = np.median(data)
mode_value = statistics.mode(data)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

# Dispersion Measures
range_value = np.ptp(data)
variance_value = np.var(data)
print(f"Mode: {mode_value}")
std_deviation = np.std(data)
print(f"Range: {range_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_deviation}")

# Plotting Histogram
plt.hist(data, bins=6, color='blue', edgecolor='black')
plt.axvline(mean_value, color='green', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value}')
plt.axvline(median_value, color='red', linestyle='dashed', linewidth=2, label=f'Median: {median_value}')
plt.axvline(mode_value, color='pink', linestyle='dashed', linewidth=2, label=f'Mode: {mode_value}')
plt.legend()
plt.title('Histogram with Mean, Median, Mode')
plt.show()