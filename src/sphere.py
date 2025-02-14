import numpy as np
import pandas as pd


# Define number of points in each direction
num_points = 10

# Create 1d vectors for both angles
theta = np.linspace(0, np.pi, num_points)  # Longitude 
azimuthal = np.linspace(0, 2*(np.pi), num_points)  # Latitude (phi)

# Create a meshgrid
theta, azimuthal = np.meshgrid(theta, azimuthal)

print("Theta shape:", theta.shape)
print("Phi shape:", azimuthal.shape)

# x = sin(φ) cos(θ)
# y = sin(φ) sin(θ) 
# z = r cos(φ) & r = 1 for a unit sphere

x = np.sin(azimuthal) * np.cos(theta)
y = np.sin(azimuthal) * np.sin(theta)
z = np.cos(azimuthal)

print("x shape:", x.shape)
print("y shape:", y.shape)
print("z shape:", z.shape)