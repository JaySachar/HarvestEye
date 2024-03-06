import os
from classesCHANGE import PointCloudGenerator
import time

# Define the directory containing the images
start = time.time()
img_directory = r"C:\Users\Jay\Desktop\Pix4Dmatic_example_100_images\image_subset_100"

# Initialize the PointCloudGenerator with the image directory
point_cloud_generator = PointCloudGenerator(img_directory)

# Run the image processing and point cloud generation
point_cloud_generator.generatePointCloud()

# Access the point cloud data
point_cloud_data = point_cloud_generator.point_cloud_data

# Print the data to verify it was generated successfully
print(point_cloud_data)

output_file = os.path.join(img_directory, 'output.ply')

# Write the content into a new .PLY file
with open(output_file, 'w') as f:
    f.write(point_cloud_generator.point_cloud_data)

end = time.time()
elapsed_time = end - start
print(f"Elapsed Time = {elapsed_time}")