import numpy as np
import pandas as pd
import subprocess
import os
import tempfile
from sklearn.linear_model import RANSACRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
import open3d as o3d
from matplotlib.colors import Normalize
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# ImageProcessor is responsible for housing general image processing functions
# This includes downsampling images, and any other edits we'd have to make to them 
class ImageProcessor:
    
    def __init__(self, img_directory):
        # directory [STRING]: "C:/Users/.../XXX"
        self.img_directory = img_directory
        self.imgs, self.img_type = self.file_extension_grabber(img_directory)

    def image_preprocessing(self):
        # Define any preprocessing we want. Could break this up to different functions as well, ie a image format changer format
        pass 

    def file_extension_grabber(self, img_directory):
        # Takes the directory holding the images, and checks for what type of files there are in that directory, and isolates and returns only
        # The image extensions present

        image_extensions = ['.jpg', '.png', '.jpeg', '.svg', 'avif'] # acceptable file formats
        
        image_files = [] # List holding the directory to each image
        image_ext = [] # List holding the file extension present and corresponds to each image
        
        for file in os.listdir(img_directory): # For each file in the directory given
            if os.path.isfile(os.path.join(img_directory, file)): # Checks if the file is a file and not a directory or the like
                _, ext = os.path.splitext(file) # Split it so the extension is recieved (ie .txt)

                if ext.lower() in image_extensions: 
                    image_files.append(file) 
                    image_ext.append(ext)
                
        return image_files, image_ext # Return all the image files in the directory and the extensions of them                
   
    def read_ply(self, ply_data_or_file_path):
        vertices = []
        colors = []

        # Check if the input is a file path or string data
        if os.path.isfile(ply_data_or_file_path):
            with open(ply_data_or_file_path, 'r') as f:
                lines = f.readlines()
        else:
            # Split the string data by newline characters
            lines = ply_data_or_file_path.strip().split('\n')

        # Skip the first line which contains the number of vertices
        for line in lines[1:]:
            data = line.strip().split()
            vertex = [float(data[0]), float(data[1]), float(data[2])]
            vertices.append(vertex)

            if len(data) > 3:  # Check if RGB values are present
                rgb = [int(data[3]), int(data[4]), int(data[5])]
                colors.append(rgb)

        vertices_np = np.array(vertices)
        colors_np = np.array(colors) if colors else None

        return vertices_np, colors_np
    
# Create PointCloudGenerator as a child to ImageProcessor so we can encapsulate
# All image preprocessing functions
class PointCloudGenerator(ImageProcessor):
    def __init__(self, img_directory):
        super().__init__(img_directory) # Calls initializer for the ImageProcessor class
                                        # Takes the img_directory, and initializes the imgs and img_type attributes
                                        # The imgs attribute is a list of file names in the img_directory that are image files (based on the specified image_extensions)
                                        # The img_type attribute is the file extension of the first image file found in the img_directory (or None if no image files are found)
        
        global_pipeline_dir = os.path.dirname(os.path.realpath(__file__))

        # Navigate up the directory structure until you reach the HarvestEye directory
        while not os.path.basename(global_pipeline_dir) == 'HarvestEye':
            global_pipeline_dir = os.path.dirname(global_pipeline_dir)

        # Combine the path to the openMVG executable
        self.openmvg_bin = os.path.join(global_pipeline_dir, 'openMVG Built', 'Windows-AMD64-', 'Release')

        # sensor_width_database
        self.cam_params = os.path.join(global_pipeline_dir, 'openMVG Built', 'openMVG', 'exif', 'sensor_width_database', 'sensor_width_camera_database.txt')

        # Point cloud data
        self.point_cloud_data = np.NaN
        
 
    def generatePointCloud(self):
        # Create a temporary directory for the matches
        with tempfile.TemporaryDirectory() as matches_dir:
            # Compute Intrinsic Analysis and Image Listing
            pIntrisics = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_SfMInit_ImageListing"), "-i", self.img_directory, "-o", matches_dir, "-d", self.cam_params])
            pIntrisics.wait()

            # Compute Features
            pFeatures = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_ComputeFeatures"), "-i", os.path.join(matches_dir, "sfm_data.json"), "-o", matches_dir, "-m", "SIFT"])
            pFeatures.wait()

            # Compute matching pairs
            pPairs = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_PairGenerator"), "-i", os.path.join(matches_dir, "sfm_data.json"), "-o", os.path.join(matches_dir, "pairs.bin")])
            pPairs.wait()

            # Compute Matches
            pMatches = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_ComputeMatches"), "-i", os.path.join(matches_dir, "sfm_data.json"), "-p", os.path.join(matches_dir, "pairs.bin"), "-o", os.path.join(matches_dir, "matches.putative.bin")])
            pMatches.wait()

            # Filter Matches
            pFiltering = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_GeometricFilter"), "-i", os.path.join(matches_dir, "sfm_data.json"), "-m", os.path.join(matches_dir, "matches.putative.bin"), "-g", "e", "-o", os.path.join(matches_dir, "matches.e.bin")])
            pFiltering.wait()

            with tempfile.TemporaryDirectory() as reconstruction_dir:
            # Do global reconstruction

                pRecons = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_SfM"), "--sfm_engine", "GLOBAL", "--input_file", os.path.join(matches_dir, "sfm_data.json"), "--match_file", os.path.join(matches_dir, "matches.e.bin"), "--output_dir", reconstruction_dir])
                pRecons.wait()

                # Colorize the structure
                pRecons = subprocess.Popen([os.path.join(self.openmvg_bin, "openMVG_main_ComputeSfM_DataColor"), "-i", os.path.join(reconstruction_dir, "sfm_data.bin"), "-o", os.path.join(self.img_directory, "colorized.ply")])
                pRecons.wait()

                # Return the PLY File's Data
                ply_dir = os.path.join(self.img_directory, 'colorized.ply')
                with open(ply_dir, 'r') as f:
                    ply_data = f.read()

                # Return the PLY file's data
                return ply_data, self.point_cloud_data
            # In temporary matches folder, we can run stiching from OpenCV, so we don't have to keep such a large file on hand per run. 
   
    def downsamples_pointcloud(self, pcd, voxel_size):
        downsampled_pcd = pcd.voxel_down_sample(voxel_size)
        return downsampled_pcd
        # A function for turning a .TIF to a .JPG to pass to the PointCloudGenerator 

    def pcd_array_normalized(self, pcd):
        # Assuming pcd is an o3d object, and thus can be returned as pcd.colors and pcd.points
        points = np.asarray(pcd.points)
        colors = np.asarray(pcd.colors)

        # Concatenate XYZ and RGB values
        xyzrgb = np.hstack((points, colors))  
        scaler = StandardScaler()
        xyzrgb_normalized = scaler.fit_transform(xyzrgb)
        return xyzrgb_normalized
    
    def densify_point_cloud(self, pcd):
        pass 
# The UnsupervisedSegmentationAlgorithm is responsible for housing unsupervised segmentation algorithms, namely KMeans clustering and DBSCAN
# To separate the ground and the plant. 
class UnsupervisedSegmentationAlgorithm:
    """
    Houses the algorithms for Unsupervised Segmentation, including KMeans and DBSCAN.
    """

    def __init__(self):
        pass

    def normalized_and_weighted_kmeans(self, weights, xyzrgb_normalized, num_clusters = 2):
        """
        Perform KMeans clustering on weighted and normalized xyzrgb data.

        Parameters:
        - weights: array of weights to apply to the xyzrgb data.
        - xyzrgb_normalized: normalized xyzrgb data as a numpy array.
        - num_clusters: number of clusters for KMeans.

        Returns:
        - labels: cluster labels for each point.
        - kmeans: the fitted KMeans model.
        """

        weighted_xyzrgb = xyzrgb_normalized * weights[:]
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(weighted_xyzrgb)
        labels = kmeans.labels_

        return labels, kmeans

    def crop_clustering_dbscan(self, eps, xyz_pcd_points):
        """
        Perform DBSCAN clustering on xy components of point cloud data.

        Parameters:
        - eps: the maximum distance between two samples for one to be considered as in the neighborhood of the other.
        - xyz_pcd_points: point cloud data as a numpy array.

        Returns:
        - dbscan_labels: cluster labels for each point, with -1 indicating noise.
        - clustered_points_xyz: points that are not noise as a numpy array.
        """

        min_samples = 1
        xy_points = xyz_pcd_points[:, :2]
        dbscan = DBSCAN(eps=eps, min_samples=min_samples).fit(xy_points)
        dbscan_labels = dbscan.labels_
        clustered_tree_indices = np.where(dbscan_labels != -1)[0]  # Indices of points that are not noise
        
        clustered_points_xyz = xyz_pcd_points[clustered_tree_indices]
        return dbscan_labels, clustered_points_xyz
        
class PointCloudFiltering(ImageProcessor):
    def __init__(self):
        pass

    def filter_points_by_grid(self, points, grid_resolution, std_limit, avg_z_filter_iteration_times):
        """
        Filters points in a point cloud based on a grid resolution and standard deviation limit.

        Parameters:
        - points: numpy array with xyz coordinates of the points.
        - grid_resolution: size of the grid cells.
        - std_limit: standard deviation limit for outlier detection.

        Returns:
        - Filtered points as a numpy array.
        """

        x_min, x_max = np.min(points[:, 0]), np.max(points[:, 0])
        y_min, y_max = np.min(points[:, 1]), np.max(points[:, 1])
        z_min, z_max = np.min(points[:, 2]), np.max(points[:, 2])

        # Create the grid
        x_bins = np.arange(x_min, x_max, grid_resolution)
        y_bins = np.arange(y_min, y_max, grid_resolution)

        # Digitize points into grid cells
        x_indices = np.digitize(points[:, 0], x_bins)
        y_indices = np.digitize(points[:, 1], y_bins)

        # Calculate local averages and standard deviations for each grid cell
        local_averages = np.zeros((len(x_bins)-1, len(y_bins)-1))
        local_std_devs = np.zeros((len(x_bins)-1, len(y_bins)-1))

        for i in range(1, len(x_bins)):
            for j in range(1, len(y_bins)):
                mask = (x_indices == i) & (y_indices == j)
                points_in_cell = points[mask]
                if len(points_in_cell) > 0:
                    local_averages[i-1, j-1] = np.mean(points_in_cell[:, 2])
                    local_std_devs[i-1, j-1] = np.std(points_in_cell[:, 2])

        # Filter out points based on local averages and standard deviations
        thresholds = local_averages + std_limit * local_std_devs
        mask = np.zeros(len(points), dtype=bool)
        for _ in range(avg_z_filter_iteration_times):
            for i in range(1, len(x_bins)):
                for j in range(1, len(y_bins)):
                    cell_mask = (x_indices == i) & (y_indices == j)
                    if np.any(cell_mask):
                        mask |= (cell_mask) & (points[:, 2] < thresholds[i-1, j-1])
            filtered_points = points[mask]

        return filtered_points
    
    def filter_ground_points(self, ground_points, avg_z_filter_interation_times, grid_resolution, std_limit):
        """
        Filters ground points based on the average z-value and a grid-based local filtering method.

        Parameters:
        - ground_points: numpy array with xyz coordinates of the ground points.
        - avg_z_filter_iteration_times: number of iterations for z-average filtering.
        - grid_resolution: size of the grid cells.
        - std_limit: standard deviation limit for outlier detection.

        Returns:
        - Filtered ground points as a numpy array.
        """
        # for _ in range(avg_z_filter_interation_times):
        #     z_average = np.mean(ground_points[:, 2])
        #     z_std = np.std(ground_points[:, 2])
        #     print("hello wrld 3", z_average, z_std)
        #     threshold = z_average + std_limit*z_std
        #     mask = ground_points[:, 2] < threshold # Remove points that are1 standard deviation or more away from the mean
        #     ground_points = groucreatingnd_points[mask]

        # Use filtering by  a grid and local averages to filter out ground points more, locally however
        filtered_ground_points = self.filter_points_by_grid(ground_points, grid_resolution, std_limit, avg_z_filter_interation_times)

        return filtered_ground_points   
   
    def dbscan_cluster_filtering(self, pcd, min_cluster_size, max_cluster_size, labels):
        """
        Filter clusters after running DBSCAN on a point cloud based on cluster size using the DBSCAN labels.

        Parameters:
        - pcd: open3d.geometry.PointCloud object.
        - min_cluster_size: minimum number of points in a cluster.
        - max_cluster_size: maximum number of points in a cluster.
        - labels: array of DBSCAN labels for each point in the point cloud.

        Returns:
        - dbscan_clusters_pcd_filtered: filtered open3d.geometry.PointCloud object.
        """
        # Remove the noise label (-1)
        valid_labels = labels[labels != -1]
        unique_labels, counts = np.unique(valid_labels, return_counts=True)
        label_counts = dict(zip(unique_labels, counts))

        # Create a list idx that stores each index that matches the required max and min cluster sizes
        idx = [i for i, label in enumerate(labels) if label != -1 and min_cluster_size <= label_counts[label] <= max_cluster_size]

        # Filter the point cloud based on idx
        dbscan_clusters_pcd_filtered = o3d.geometry.PointCloud()
        dbscan_clusters_pcd_filtered.points = o3d.utility.Vector3dVector(np.asarray(pcd.points)[idx])
        if pcd.colors:  # Ensure that colors exist before attempting to filter them
            dbscan_clusters_pcd_filtered.colors = o3d.utility.Vector3dVector(np.asarray(pcd.colors)[idx])
        print(labels[idx])
        return dbscan_clusters_pcd_filtered, labels[idx]

class CropAnalyzer:
    def __init__(self):
        pass

    def calculate_highest_point(self, cluster_points):
        """
        Calculate the highest point in a cluster.

        Parameters:
        - cluster_points: numpy array of points in the cluster.

        Returns:
        - The highest point in the cluster.
        """
        return np.max(cluster_points, axis=0)  # Calculate maximum along Z-axis

    def find_closest_ground_point(self, point, ground_points):
        """
        Find the closest ground point to a given point.

        Parameters:
        - point: The point for which to find the closest ground point.
        - ground_points: numpy array of ground points.

        Returns:
        - The closest ground point.
        """
        distances = np.linalg.norm(ground_points[:, :2] - point[:2], axis=1)  # Calculate Euclidean distances in XY plane
        closest_index = np.argmin(distances)
        return ground_points[closest_index]

    def calculate_height_difference(self, highest_point, closest_ground_point):
        """
        Calculate height difference between a crop cluster and the closest ground point.

        Parameters:
        - highest_point: The highest point in the cluster.
        - closest_ground_point: The closest ground point to the highest point.

        Returns:
        - Height difference.
        """
        return highest_point[2] - closest_ground_point[2]  # Calculate difference in Z-coordinates

    def calculate_cluster_centers(self, labels, points):
        """
        Calculate the centers of clusters.

        Parameters:
        - labels: Cluster labels for each point.
        - points: numpy array of points.

        Returns:
        - A dictionary mapping cluster labels to their centers.
        """
        unique_labels = np.unique(labels)
        cluster_centers = {}
        for label in unique_labels:
            if label == -1:
                continue
            cluster_points = points[labels == label]
            center = np.mean(cluster_points, axis=0)
            cluster_centers[label] = center
        return cluster_centers
    
    def calculate_heights_and_labels(self, filtered_labels, clustered_points, filtered_ground_pcd):
        """
        Calculate height and labels for filtered DBSCAN clusters.

        Parameters:
        - filtered_labels: Labels of the filtered clusters.
        - clustered_points: Point cloud of the clusters.
        - filtered_ground_points: Point cloud of the ground points.

        Returns:
        - heights: List of height differences for each cluster.
        - labels: List of cluster labels.
        """
        filtered_ground_points = np.asarray(filtered_ground_pcd.points)
        heights_dict = {}
        labels = []
        for label in np.unique(filtered_labels):
            if label == -1:  # Skip noise points
                continue
            
            # Get points belonging to the current cluster
            cluster_indices = np.where(filtered_labels == label)[0]
            cluster_points = np.asarray(clustered_points.points)[cluster_indices]

            # Calculate the highest point in the cluster
            highest_point = self.calculate_highest_point(cluster_points)
            
            # Find the closest ground point
            closest_ground_point = self.find_closest_ground_point(highest_point, filtered_ground_points)
            
            # Calculate height difference
            height_difference = self.calculate_height_difference(highest_point, closest_ground_point)
            
            heights_dict[label] = (height_difference)
            labels.append(label)
        
        return heights_dict, labels

    def visualize_the_heights_and_pcd(self, cluster_heights_dict, dbscan_filtered_pcd, cluster_centers):
        """
        Visualize the heights and point cloud data.

        Parameters:
        - cluster_heights_dict: Dictionary of heights for each cluster.
        - dbscan_filtered_pcd: Filtered point cloud.
        - cluster_centers: Dictionary of cluster centers.
        """
        points = np.asarray(dbscan_filtered_pcd.points)
        # Create a 3D plot
        fig = plt.figure(figsize=(30, 24))
        ax = fig.add_subplot(111, projection='3d')

        # Plot the point cloud
        ax.scatter(points[:, 0], points[:, 1], points[:, 2])

        # Add label annotations for cluster centers
        for label, center in cluster_centers.items():
            try:
                height = cluster_heights_dict[label]  # Get height for the current cluster
                ax.text(center[0], center[1], center[2], f'Cluster {label}\nHeight: {height:.2f}', color='red')
            except IndexError:
                print(f"IndexError occurred for label: {label}")
        # Set labels for axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Set the view to top-down
        ax.view_init(elev=90, azim=0)

        # Show the plot
        plt.show()
    def calculate_heights(self, points, ground_points):
        """
        Calculate the height of each point relative to the closest ground point.

        Parameters:
        - points: numpy array of points in the clusters.
        - ground_points: numpy array of ground points.

        Returns:
        - heights: numpy array of height differences.
        """
        heights = np.zeros(points.shape[0])
        for i, point in enumerate(points):
            closest_ground_point = self.find_closest_ground_point(point, ground_points)
            heights[i] = point[2] - closest_ground_point[2]
        return heights

    def visualize_height_gradient(self, dbscan_clusters_filtered_points, filtered_ground_pcd):
        """
        Visualize the height of each point with a gradient color from blue to red using Open3D,
        including visualization of the ground points.

        Parameters:
        - dbscan_clusters_filtered_points: Filtered point cloud.
        - filtered_ground_pcd: Ground points.
        """
        points = np.asarray(dbscan_clusters_filtered_points.points)
        ground_points = np.asarray(filtered_ground_pcd.points)
        
        # Calculate heights
        heights = self.calculate_heights(points, ground_points)

        # Normalize heights to range [0, 1]
        norm = Normalize(vmin=np.min(heights), vmax=np.max(heights))
        normalized_heights = norm(heights)
        
        # Apply color gradient (viridis colormap)
        colormap = cm.get_cmap('viridis')
        colors = colormap(normalized_heights)[:, :3]  # Get RGB values
        
        # Create Open3D point cloud for clustered points
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        pcd.colors = o3d.utility.Vector3dVector(colors)
        
        # Create Open3D point cloud for ground points
        ground_pcd = o3d.geometry.PointCloud()
        ground_pcd.points = o3d.utility.Vector3dVector(ground_points)
        ground_pcd.paint_uniform_color([0.8, 0.8, 0.8])  # Set color for ground points
        
        # Combine clustered points and ground points
        combined_pcd = pcd + ground_pcd
        
        # Visualize the combined point cloud
        o3d.visualization.draw_geometries([combined_pcd])
    def calculate_oval_volume(self, cluster_points, ground_points):
        # Step 1: Find furthest XY points in the cluster
        furthest_points = self.find_furthest_xy_points(cluster_points)

        # Step 2: Calculate maximum height of the cluster
        highest_point = self.calculate_highest_point(cluster_points)
        closest_ground_point = self.find_closest_ground_point(highest_point, ground_points)
        max_height = self.calculate_height_difference(highest_point, closest_ground_point)

        # Step 3: Calculate semi-major and semi-minor axes lengths (a and b)
        a = np.linalg.norm(furthest_points[0] - furthest_points[1]) / 2.0
        b = np.linalg.norm(furthest_points[0] - furthest_points[2]) / 2.0

        # Step 4: Calculate volume of an ellipsoid (since oval is an extension in Z-direction)
        volume = (4/3) * np.pi * a * b * max_height
        
        return volume

    def find_furthest_xy_points(self, cluster_points):
        # Compute convex hull of the cluster points
        hull = ConvexHull(cluster_points[:, :2])

        # Initialize variables to store furthest points and maximum distance
        furthest_points = None
        max_distance = 0

        # Iterate through convex hull vertices to find maximum distance pair
        for i in range(len(hull.vertices)):
            for j in range(i + 1, len(hull.vertices)):
                # Calculate squared Euclidean distance between points
                distance = np.linalg.norm(cluster_points[hull.vertices[i], :2] - cluster_points[hull.vertices[j], :2]) ** 2
                if distance > max_distance:
                    max_distance = distance
                    furthest_points = (cluster_points[hull.vertices[i]], cluster_points[hull.vertices[j]])

        return furthest_points


    def calculate_volumes_for_clusters(self, dbscan_filtered_pcd, dbscan_filtered_labels, filtered_ground_pcd):
        volumes_dict = {}
        filtered_ground_points = np.asarray(filtered_ground_pcd.points)
        
        for label in np.unique(dbscan_filtered_labels):
            if label == -1:  # Skip noise points
                continue
            
            # Get points belonging to the current cluster
            cluster_indices = np.where(dbscan_filtered_labels == label)[0]
            cluster_points = np.asarray(dbscan_filtered_pcd.points)[cluster_indices]

            # Calculate volume for the current cluster
            volume = self.calculate_oval_volume(cluster_points, filtered_ground_points)
            
            # Store volume in dictionary with label as key
            volumes_dict[label] = volume
        
        return volumes_dict
    
class GUI:
    def __init__(self):
        pass