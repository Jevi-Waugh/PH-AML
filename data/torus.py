# Ensuring that the output format strictly follows:
# First row: All x values
# Second row: All y values
# Third row: All z values

import numpy as np
import pandas as pd

def generate_torus(n_points=500, R=2.0, r=1.0):
    """
    Generate a torus in 3D coordinates with all x values in the first row,
    all y values in the second row, and all z values in the third row.
    
    Parameters:
    - n_points: Number of points to generate
    - R: Major radius (distance from center to tube center)
    - r: Minor radius (tube radius)

    Returns:
    - A 3xN array where the first row contains all x values,
      the second row contains all y values, and the third row contains all z values.
    """
    theta = np.random.uniform(0, 2*np.pi, n_points)  # Angle around the torus
    phi = np.random.uniform(0, 2*np.pi, n_points)    # Angle around the tube

    x = (R + r * np.cos(phi)) * np.cos(theta)
    y = (R + r * np.cos(phi)) * np.sin(theta)
    z = r * np.sin(phi)

    return np.array([x, y, z])  # Ensuring correct row-major format (3 x N)

# Generate torus point cloud
torus_points = generate_torus(n_points=1000)

# Save the correctly formatted CSV file
csv_filename = "torus_points_corrected.csv"
np.savetxt(csv_filename, torus_points, delimiter=",", fmt="%.6f")

# Return CSV file path
csv_filename
