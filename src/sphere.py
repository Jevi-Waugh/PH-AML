import numpy as np
import pandas as pd
import os


def Sphere(pts: int=5) -> None:
    """ Generates points on the surface of a unit sphere using spherical coordinates.

    x = sin(φ) cos(θ)
    y = sin(φ) sin(θ) 
    z = r cos(φ) & r = 1 for a unit sphere
    
    Create a 2D grid from the 1D arrays
    meshgrid creates two 2D arrays so that for every 𝑥 
    value, every  𝑦 value is paired with it. 
    This "duplication" ensures that  the entire 2D space are covered due to angle range incompatibility.

    Every row in theta is a copy of theta_values.
    Every column in phi is a copy of phi_values.
    
    Args:
        pts (int): Define number of points in each direction. Defaults to 5.
    """

    # Create 1d vectors for both angles
    theta = np.linspace(0, np.pi, pts)  # Longitude 
    azimuthal = np.linspace(0, 2*(np.pi), pts)  # Latitude (phi)
    
    theta, azimuthal = np.meshgrid(theta, azimuthal)
    
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

    # Stack them horizontally and transpose to get x, y, z
    sphere_matrix = np.vstack((x,y,z)).T

    # Exporting as a CSV file
    sphere_df = pd.DataFrame(sphere_matrix, columns=['x','y','z'])
    with open("folder_path.txt", "r") as file:
        folder = file.read()
    folder = os.path.join(folder, "data")
    file_path = os.path.join(folder, "sphere_coordinates.csv")
    sphere_csv = sphere_df.to_csv(file_path,index=False)

