import numpy as np
import pandas as pd
import os


def Sphere(pts: int=5, iter: int=None, noise_level=0.0) -> None:
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

    # # Create 1d vectors for both angles
    theta = np.linspace(0, 2*(np.pi), pts)  # Longitude 
    azimuthal = np.linspace(0, (np.pi), pts)  # Latitude (phi)
    
    theta, azimuthal = np.meshgrid(theta, azimuthal)
    
    x = np.sin(azimuthal) * np.cos(theta)
    y = np.sin(azimuthal) * np.sin(theta)
    z = np.cos(azimuthal)

    # Stack them horizontally and transpose to get x, y, z in individual lists
        #sphere_matrix = np.vstack((x,y,z)).T
    sphere_matrix = np.vstack((x.flatten(),y.flatten(),z.flatten()))
    # Add noise if specified
    if noise_level > 0:
        noise = np.random.normal(0, noise_level, sphere_matrix.shape)
        sphere_matrix = sphere_matrix + noise

    # Exporting as a CSV file
    sphere_df = pd.DataFrame(sphere_matrix)
    
    # with open("folder_path.txt", "r") as file:
    #     folder = file.read()
    # folder = os.path.join(folder, "data/")
    # file_path = os.path.join(folder, "sphere_coordinates_1.csv")
    file_path = f"C:/Users/jevin/Documents/Documents/Education/Self-Learning/Persistant Homology/PHAML/data/sphere/sphere_coordinates_{iter}.csv"
    sphere_csv = sphere_df.to_csv(file_path,index=False,header=False)


def main():
    
    # was 12 pts for sphere 1
    # was 8 pts for sphere 2
    N = 10 # 10 spheres
    for i in range(0,N):
        Sphere(i+6, iter=i)

    
    # 6,7,8,12,15
    
if __name__ == "__main__":
    main()