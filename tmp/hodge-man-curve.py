pip install numpy
pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Generate data to represent a Hodge-Man curve
temperature = np.linspace(50, 1000, 500)  # Temperature range from 50 to 1000 Kelvin
Cp = 20 + 0.1 * temperature - 0.00005 * temperature**2  # Example of Cp dependence on temperature

# Plotting the Hodge-Man curve
plt.figure(figsize=(8,6))
plt.plot(temperature, Cp, color='b', label="Specific Heat Capacity (Cp)")

# Adding labels and title
plt.title("Hodge-Man Curve (Cp vs Temperature)")
plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat Capacity at Constant Pressure (Cp)")

# Displaying the plot
plt.grid(True)
plt.legend()
plt.show()