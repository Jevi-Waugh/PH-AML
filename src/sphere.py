import numpy as np
import pandas as pd

# Generate data for a sphere
# Using spherical coordinates: r, theta, phi
# Assume a unit sphere (r = 1), theta varies from 0 to 2pi, phi varies from 0 to pi

theta = np.linspace(0, 2*np.pi, 10)
phi = np.linspace(0, np.pi, 10)

# Creating a meshgrid for spherical coordinates
theta, phi = np.meshgrid(theta, phi)

# Convert spherical coordinates to Cartesian coordinates
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Stack the x, y, z coordinates into a 3x100 array
sphere_data = np.vstack((x.flatten(), y.flatten(), z.flatten()))

# Create a DataFrame and export as CSV
sphere_df = pd.DataFrame(sphere_data)

# Saving as CSV
# folder_path = "C:/Users/jevin/Documents/Documents/Education/Self-Learning/Persistant Homology/PHAML/src/"
csv_path = "sphere_coordinates.csv"
sphere_df.to_csv(csv_path, index=False, header=False)

csv_path
