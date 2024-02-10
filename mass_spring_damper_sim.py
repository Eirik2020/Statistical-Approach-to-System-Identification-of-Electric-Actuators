# All Packages
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import tikzplotlib
#import os                        # To add paths to folders.


def mass_spring_damper(m, c, k, external_force, dt, num_steps):
    # Initialize arrays to store values
    time = np.linspace(0, dt * num_steps, num_steps)
    displacement = np.zeros(num_steps)
    velocity = np.zeros(num_steps)

    # Initial conditions
    displacement[0] = 0
    velocity[0] = 0

    # Euler method simulation
    for i in range(1, num_steps):
        acceleration = (external_force(time[i - 1]) - c * velocity[i - 1] - k * displacement[i - 1]) / m
        velocity[i] = velocity[i - 1] + acceleration * dt
        displacement[i] = displacement[i - 1] + velocity[i] * dt

    return time, displacement

# System parameters
mass = 1.0  # Mass (kg)
damping_coefficient = 0.5  # Damping coefficient (Ns/m)
spring_constant = 10.0  # Spring constant (N/m)
force_amplitude = 5.0  # External force amplitude (N)

# Simulation parameters
time_step = 0.01  # Time step (s)
num_steps = 1000  # Number of steps

# External force function (e.g., a step input)
external_force = lambda t: force_amplitude if t >= 1.0 else 0.0

# Simulate the system
time, displacement = mass_spring_damper(mass, damping_coefficient, spring_constant, external_force, time_step, num_steps)





# Plotting
##  Import additional packages  ##
import matplotlib.pyplot as plt
import seaborn as sns

## Configure style and size
sns.set_style("whitegrid")  # Apply a clean style
plt.figure(figsize=(10,  6))  # Set the figure size

## Create Plot
sns.plot(time, displacement)

## Plotting options
plt.xlabel('Time in seconds [mm]', fontsize=14)
plt.ylabel('Displacment in millimeters [mm]', fontsize=14)
plt.title('Behavior of a Mass-Spring-Damper System', fontsize=18)
plt.legend(fontsize=12)



# Save plots
## Import additonal packages
import tikzplotlib
import os                        # To add paths to folders.


# Specify the directory where you want to save the plot
output_dir = "figures/"


# Check if the directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

tikzplotlib.save(os.path.join(output_dir, 'my_plot.tex'))

