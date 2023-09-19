import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev


for i in range(2,3):

    path = f'C:/Users/Vedran/Desktop/amine/contour_points_{i}.npy'
    data = np.load(path).astype(np.int32)
    plt.figure()

    contour_points =data
    
    # Perform spline interpolation on the contour points with different 's' values
    s_values = [0.0001, 0.1, 1.0, 100.0]  # Adjust these values to experiment with different smoothness levels
    
    plt.figure(figsize=(12, 8))
    
    for i, s in enumerate(s_values):
        # Perform spline interpolation on the contour points
        tck, _ = splprep(contour_points.T, s=s)
        
        # Define the number of points for interpolation
        num_points = 5000
        
        # Generate the interpolated points on the curve
        t = np.linspace(0, 1, num_points)
        interpolated_points = np.array(splev(t, tck)).T
        
        # Convert interpolated points to np.float32
        interpolated_points = interpolated_points.astype(np.float32)
        
        # Find the minimum area rectangle that encloses the interpolated points
        rect = cv2.minAreaRect(interpolated_points)
        
        # Get the corner points of the rectangle
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        
        # Plot the original points and overlay the rectangle
        plt.subplot(2, 2, i + 1)
        plt.scatter(contour_points[:, 0], contour_points[:, 1], color='blue', s=1, label='Original Points')
        plt.plot(box[:, 0], box[:, 1], color='red', label='Approximated Rectangle')
        plt.title(f"s={s}")
        plt.legend()

    plt.tight_layout()
    plt.show()
        
        
  