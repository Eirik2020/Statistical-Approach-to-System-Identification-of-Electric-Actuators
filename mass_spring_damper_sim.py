import numpy as np
import matplotlib.pyplot as plt

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

# Set font size
plt.rcParams.update({'font.size': 14})

# Set figure size to 210mm width
fig, ax = plt.subplots(figsize=(8.27, 5.82))  # A5 size in inches (210mm x 148mm)

# Plot the results
ax.plot(time, displacement)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (m)')
ax.set_title('Mass-Spring-Damper System Response')
ax.grid(True)

# Choose whether to display or save the figure
save_figure = True  # Change to False if you want to display the figure
if save_figure:
    pgf_filepath = 'mass_spring_damper_response.pgf'
    fig.savefig(pgf_filepath, format='pgf', bbox_inches='tight')
    print(f"Figure saved as {pgf_filepath}")
else:
    plt.show()
