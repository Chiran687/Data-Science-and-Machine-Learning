import numpy as np
import matplotlib.pyplot as plt

# Generate right-skewed data
right_skewed_data = np.random.gamma(shape=2, scale=2, size=1000)

# Generate left-skewed data by taking the reciprocal of right-skewed data
left_skewed_data = 1 / right_skewed_data

# Generate non-skewed (symmetric) data from a normal distribution
non_skewed_data = np.random.normal(loc=0, scale=1, size=1000)

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot histogram for right-skewed data
axs[0].hist(right_skewed_data, bins=30, color='skyblue', edgecolor='black')
axs[0].set_title('Right-skewed Distribution')


# Plot histogram for non-skewed data
axs[2].hist(non_skewed_data, bins=30, color='lightgreen', edgecolor='black')
axs[2].set_title('Non-skewed (Symmetric) Distribution')

# Plot histogram for left-skewed data
axs[1].hist(left_skewed_data, bins=30, color='salmon', edgecolor='black')
axs[1].set_title('Left-skewed Distribution')

# Show plots
plt.tight_layout()
plt.show()
