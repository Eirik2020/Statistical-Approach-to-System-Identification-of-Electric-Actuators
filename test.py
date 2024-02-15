import os
import matplotlib.pyplot as plt
import numpy as np

# Create the "figures" folder if it doesn't exist
if not os.path.exists('figures'):
    os.makedirs('figures')

# Sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)



# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$\sin(x)$')
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()

# Save as a PGF file in the "figures" folder
plt.savefig(os.path.join('figures', 'plot.pgf'), format='pgf')
