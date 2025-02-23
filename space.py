import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dmx_to_xyz(dmx_pan, dmx_tilt):
    """
    Converts DMX channel values to a 3D unit vector that represents the beam direction.
    Assumes:
      - DMX channel 1 (pan): 0-255 maps to 0° to 540° rotation about the vertical (Z) axis.
      - DMX channel 3 (tilt): 0-255 maps to 0° to 205° rotation about the horizontal (X) axis.
      - The initial beam vector (before rotations) is [0, 1, 0] (pointing forward).
      - Tilt is applied first, then pan.
    """
    # Map DMX values to angles in degrees
    pan_deg = (dmx_pan / 255.0) * 540.0
    tilt_deg = (dmx_tilt / 255.0) * 205.0

    # Convert degrees to radians
    pan_rad = np.deg2rad(pan_deg)
    tilt_rad = np.deg2rad(tilt_deg)
    
    # The fixture's local beam vector (pointing forward)
    beam_local = np.array([0, 1, 0])
    
    # Create rotation matrix for tilt (rotation about the X-axis)
    Rx = np.array([[1,              0,               0],
                   [0, np.cos(tilt_rad), -np.sin(tilt_rad)],
                   [0, np.sin(tilt_rad),  np.cos(tilt_rad)]])
    
    # Create rotation matrix for pan (rotation about the Z-axis)
    Rz = np.array([[ np.cos(pan_rad), -np.sin(pan_rad), 0],
                   [ np.sin(pan_rad),  np.cos(pan_rad), 0],
                   [              0,               0, 1]])
    
    # Apply tilt first, then pan: beam_global = Rz * (Rx * beam_local)
    beam_global = Rz @ (Rx @ beam_local)
    return beam_global

# Create a grid of DMX values for channels 1 and 3
dmx_values = np.linspace(0, 255, num=50)
pan_grid, tilt_grid = np.meshgrid(dmx_values, dmx_values)

# Prepare arrays for x, y, z coordinates
x_grid = np.empty_like(pan_grid)
y_grid = np.empty_like(pan_grid)
z_grid = np.empty_like(pan_grid)

# Compute the 3D beam direction for each combination of DMX values
for i in range(pan_grid.shape[0]):
    for j in range(pan_grid.shape[1]):
        vec = dmx_to_xyz(pan_grid[i, j], tilt_grid[i, j])
        x_grid[i, j] = vec[0]
        y_grid[i, j] = vec[1]
        z_grid[i, j] = vec[2]

# Plot the resulting 3D points
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_grid, y_grid, z_grid, c=tilt_grid, cmap='viridis', s=10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D Mapping of DMX Pan (Ch1) and Tilt (Ch3) Values")
plt.show()
