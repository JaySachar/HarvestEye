import os
from classesCHANGE import PointCloudGenerator
import time
from sklearn.linear_model import RANSACRegressor

def append_ground_points(file_path, ground_points, ground_colors):
    # Load the original .PLY file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the end of the header
    end_header_idx = lines.index('end_header\n') + 1

    # Append ground points and colors to the existing vertex and color lists
    for i in range(len(ground_points)):
        x, y, z = ground_points[i]
        lines.append(f"{x} {y} {z}\n")

    # Update the element vertex count in the header
    lines[2] = f"element vertex {len(lines) - end_header_idx}\n"

    # Write the modified data back to the .PLY file
    with open(file_path, 'w') as f:
        f.writelines(lines)


def write_planes_to_ply(planes, filename='planes.ply'):
    header = '''ply
format ascii 1.0
element vertex {}
property float x
property float y
property float z
element face {}
property list uchar int vertex_index
end_header
'''
    num_vertices = sum(len(plane) for plane in planes)
    num_faces = sum(len(plane) - 2 for plane in planes)
    with open(filename, 'w') as f:
        f.write(header.format(num_vertices, num_faces))
        vertex_count = 0
        for plane in planes:
            for point in plane:
                f.write('{} {} {}\n'.format(point[0], point[1], point[2]))
                vertex_count += 1
        face_count = 0
        for plane in planes:
            for i in range(1, len(plane) - 1):
                f.write('3 {} {} {}\n'.format(vertex_count - len(plane), vertex_count - len(plane) + i, vertex_count - len(plane) + i + 1))
                face_count += 1
            vertex_count -= len(plane)
    print('PLY file saved as', filename)


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
#print(vertices)
#segments_of_point_cloud = point_cloud_generator.segment_point_cloud(vertices, segment_size=100000)
#ground_points, _, _ = point_cloud_generator.process_segmented_point_cloud(segments_of_point_cloud, colors=None)

planes = point_cloud_generator.region_growing_multiplane_fitting(vertices, distance_threshold=0.2)
print(planes)
write_planes_to_ply(planes)
#append_ground_points(ply_file_path, ground_points)
