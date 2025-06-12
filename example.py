# Import necessary packages.
# numpy is used for numerical operations and creating arrays.
# matplotlib.pyplot is the main plotting module.
import numpy as np
import matplotlib.pyplot as plt

# The mpl_toolkits.mplot3d module adds 3D plotting capabilities to matplotlib.
from mpl_toolkits.mplot3d import Axes3D  # This import registers the 3D projection, no explicit use is needed.

# ------------------------------------------------------------------------------
# Data Generation
# ------------------------------------------------------------------------------
# Here we create a synthetic dataset by defining a grid of x and y values and computing z as a function of x and y.
# You can consider this a "dataset" generated on the fly.
x = np.linspace(-5, 5, 50)  
# np.linspace creates 50 evenly spaced numbers between -5 and 5. These values represent the x-axis.
y = np.linspace(-5, 5, 50)  
# Similarly, we create 50 evenly spaced values for the y-axis.
X, Y = np.meshgrid(x, y)  
# np.meshgrid converts the 1D arrays into 2D grid coordinates, where X contains the x-coordinates and Y contains the y-coordinates for each point.
Z = np.sin(np.sqrt(X**2 + Y**2))  
# For each (x, y) pair in the grid, we compute z = sin(sqrt(x^2 + y^2)).
# This function produces a radial wave-like pattern over the grid.

# ------------------------------------------------------------------------------
# Plotting the 3D Mesh Plot
# ------------------------------------------------------------------------------
# Create a figure for plotting.
fig = plt.figure(figsize=(10, 7))  
# This creates a new figure with a specified size (width 10 inches, height 7 inches).

# Add a 3D subplot to the figure.
ax = fig.add_subplot(111, projection='3d')  
# The add_subplot(111) means "1 row, 1 column, subplot #1".
# The projection='3d' argument transforms the subplot into a 3D Axes.

# Create the 3D mesh plot (wireframe plot).
ax.plot_wireframe(X, Y, Z, color='green')  
# The plot_wireframe() method draws a wireframe mesh using the 2D arrays X, Y, and Z.
# The color parameter sets the color of the wireframe lines.

# ------------------------------------------------------------------------------
# Customizing the Plot
# ------------------------------------------------------------------------------
# Set the title and labels for each axis.
ax.set_title("3D Mesh Plot")    # Sets the main title of the plot.
ax.set_xlabel("X axis")         # Labels the x-axis.
ax.set_ylabel("Y axis")         # Labels the y-axis.
ax.set_zlabel("Z axis")         # Labels the z-axis.

# Display the plot.
plt.show()  
# plt.show() renders the plot in the notebook.