import os
from classesCHANGE import PointCloudGenerator
import time
import cv2
import matplotlib.pyplot as plt

def write_ply(vertices, colors, output_file):
    # Write vertices and colors to a new .ply file
    with open(output_file, 'w') as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write("element vertex {}\n".format(len(vertices)))
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("property uchar red\n")
        f.write("property uchar green\n")
        f.write("property uchar blue\n")
        f.write("end_header\n")
        for i in range(len(vertices)):
            f.write("{} {} {} {} {} {}\n".format(vertices[i][0], vertices[i][1], vertices[i][2], colors[i][0], colors[i][1], colors[i][2]))


# Define the directory containing the images
start = time.time()
img_directory = r"C:\Users\Jay\Desktop\DJI_20240405 Park_nadir"
ply_file_path =  r"C:\Users\Jay\Desktop\DJI_20240405 Park_nadir\output.ply"

# Initialize the PointCloudGenerator with the image directory
point_cloud_generator = PointCloudGenerator(img_directory)

# Run the image processing and point cloud generation
ply_file = point_cloud_generator.generatePointCloud()

# Access the point cloud data
point_cloud_data = point_cloud_generator.point_cloud_data
print(point_cloud_data)
print(ply_file)
vertices, colours =point_cloud_generator.read_ply(point_cloud_data)
print(vertices, colours)
write_ply(vertices, colours, ply_file_path)