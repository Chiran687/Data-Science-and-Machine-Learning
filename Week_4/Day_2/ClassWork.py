def calculate_bulb_lifespan_variability(data):

    # Calculate the mean lifespan
    total_bulbs = sum(data.values())
    mean_lifespan = sum([midpoint * count for midpoint,
                        count in data.items()]) / total_bulbs

    # Calculate variance
    variance = 0
    for midpoint, count in data.items():
        squared_deviation = (midpoint - mean_lifespan) ** 2
        variance += count * squared_deviation

    # Bessel's correction for unbiased variance estimate
    variance /= (total_bulbs - 1)

    # Calculate standard deviation
    standard_deviation = variance ** 0.5

    return standard_deviation


# Supplier data
supplier_a_data = {
    (400 + 500) / 2: 8,
    (500 + 600) / 2: 20,
    (600 + 700) / 2: 16,
    (700 + 800) / 2: 6,
}

supplier_b_data = {
    (400 + 500) / 2: 6,
    (500 + 600) / 2: 24,
    (600 + 700) / 2: 12,
    (700 + 800) / 2: 8,
}

# Calculate standard deviations
supplier_a_sd = calculate_bulb_lifespan_variability(supplier_a_data)
supplier_b_sd = calculate_bulb_lifespan_variability(supplier_b_data)

# Compare standard deviations
if supplier_a_sd > supplier_b_sd:
    print("Supplier A has bulbs with a wider range of lifespans.")
elif supplier_a_sd < supplier_b_sd:
    print("Supplier B has bulbs with a wider range of lifespans.")
else:
    print("Both suppliers have the same variability in bulb lifespans.")
