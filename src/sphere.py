import numpy as np
import pandas as pd


# def sphere() -> 
# Define number of points in each direction
num_points = 2

# Create 1d vectors for both angles
theta = np.linspace(0, np.pi, num_points)  # Longitude 
azimuthal = np.linspace(0, 2*(np.pi), num_points)  # Latitude (phi)

# Create a meshgrid
theta, azimuthal = np.meshgrid(theta, azimuthal)
# Create a 2D grid from the 1D arrays
# meshgrid creates two 2D arrays so that for every 𝑥 
# value, every  𝑦 value is paired with it. 
# This "duplication" ensures that you cover the entire 2D space.

# Every row in theta is a copy of theta_values.
# Every column in phi is a copy of phi_values.

# remember
# x = sin(φ) cos(θ)
# y = sin(φ) sin(θ) 
# z = r cos(φ) & r = 1 for a unit sphere

# print(f"Theta: {theta}\n")
# print(f"Azimuthal: {azimuthal}")

x = np.sin(azimuthal) * np.cos(theta)
y = np.sin(azimuthal) * np.sin(theta)
z = np.cos(azimuthal)

# print("x shape:", x.shape)
# print("y shape:", y.shape)
# print("z shape:", z.shape)


# now we want every row to be x,y,z in a vector
x = x.flatten()
y = y.flatten()
z = z.flatten()

print(x)
print(y)
print(z)

matrix = np.vstack((x,y,z))
matrix_t = matrix.T
print(matrix_t)