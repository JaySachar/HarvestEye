import os
from classesCHANGE import PointCloudGenerator
import time
from sklearn.linear_model import RANSACRegressor
# Define the directory containing the images
start = time.time()
img_directory = r"C:\Users\Jay\Desktop\Pix4Dmatic_example_100_images\image_subset_100"
ply_file_path =  r"C:\Users\Jay\Desktop\Pix4Dmatic_example_100_images\image_subset_100\output.ply"
# Initialize the PointCloudGenerator with the image directory
point_cloud_generator = PointCloudGenerator(img_directory)
vertices, colors = point_cloud_generator.read_ply(ply_file_path)

# Run the image processing and point cloud generation
#point_cloud_generator.generatePointCloud()

# Access the point cloud data
#point_cloud_data = point_cloud_generator.point_cloud_data

# Print the data to verify it was generated successfully
print(colors)
