import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os
import sys
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib as plt
from matplotlib.colors import Normalize
import matplotlib.cm as cm
from scipy.spatial import ConvexHull
import threading
from scipy.spatial import distance_matrix
# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate one folder up
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Navigate to the 'main' folder
target_dir = os.path.join(parent_dir, 'main')

# Add the 'main' folder to the Python path
sys.path.append(target_dir)

# Now you can import the target file
from classesCHANGE import PointCloudGenerator, UnsupervisedSegmentationAlgorithm, PointCloudFiltering, CropAnalyzer

def height_and_analysis_script(pcd_file_path, voxel_size, crop_type, mode):

        # Function to create a convex hull in the XY plane
        def create_convex_hull(cluster_points, plot=False):
            points_xy = cluster_points[:, :2]  # Extract XY coordinates
            hull = ConvexHull(points_xy)

            return hull

        pcd = o3d.io.read_point_cloud(pcd_file_path)
        
        pcd_functions = PointCloudGenerator(os.path.dirname(__file__))
        unsup_segmentation = UnsupervisedSegmentationAlgorithm()
        pcd_filtering = PointCloudFiltering()
        analyzer = CropAnalyzer()

        # Downsample the point cloud
        # Voxel size was normally 0.25 for meters
        print("downsampling")
        downsampled_pcd = pcd_functions.downsamples_pointcloud(pcd, voxel_size)
        print("downsampled")
        # Normalize the point cloud
        xyzrgb_normalized = pcd_functions.pcd_array_normalized(downsampled_pcd)
        print("norm")

        # Define weights and number of clusters for KMeans
        print("check crop type")

        if crop_type == "avocado":
            weights = [4, 4, 25, 8, 17, 8]
        # If Hazelnuts weights = [ ]
        elif crop_type == "hazelnut":
            weights = [8, 8, 11, 4, 8, 4]
        else:
            weights = [2, 2, 5, 1, 3, 1]

        num_clusters = 2
        kmeans_labels, kmeans = unsup_segmentation.normalized_and_weighted_kmeans(weights, xyzrgb_normalized, num_clusters)
        print("kmeans good")

        # Prepare cluster colors array
        cluster_colors = np.zeros_like(xyzrgb_normalized[:, :3])  # Use only the XYZ part for colors

        # Define colors for clusters
        colors = {
            "green": [0, 150/255, 0],  # Green color
            "brown": [0.647, 0.165, 0.165]  # Brown color
        }

       # Determine the ground cluster based on the lower average z value
        print("finding grouind cluster")

        average_z = []
        for i in range(num_clusters):
            cluster_points = np.asarray(downsampled_pcd.points)[kmeans_labels == i]
            avg_z = cluster_points[:, 2].mean()
            average_z.append(avg_z)
        ground_cluster_label = np.argmin(average_z)
        print("ground cluster found good")

        # Assign colors based on cluster sizes
        for i in range(num_clusters):
            color = colors["brown"] if i == ground_cluster_label else colors["green"]
            cluster_colors[kmeans_labels == i] = color

        seg_pcd = downsampled_pcd
        seg_pcd.colors = o3d.utility.Vector3dVector(cluster_colors)
        
        ground_points = np.asarray(seg_pcd.points)[kmeans_labels == ground_cluster_label]
        crop_points = np.asarray(seg_pcd.points)[kmeans_labels != ground_cluster_label]

        # Filter the Ground Points list
        #filtered_ground_points = pcd_filtering.filter_ground_points(ground_points, 3, grid_resolution, 0.15)
        filtered_ground_points = pcd_filtering.filter_ground_points(ground_points, 1, 3, 0.8)
        filtered_ground_pcd = o3d.geometry.PointCloud()
        filtered_ground_pcd.points = o3d.utility.Vector3dVector(filtered_ground_points)
        filtered_crop_points = crop_points#pcd_filtering.filter_points_by_grid(crop_points, 0.75, 0.5, 5)
        filtered_crop_pcd = o3d.geometry.PointCloud()
        filtered_crop_pcd.points = o3d.utility.Vector3dVector(filtered_crop_points)
        # Filter points based on DBSCAN clustering
        # Decide on the eps value based on the crop type
        if crop_type == "avocado":
            eps = 0.26
        elif crop_type == "hazelnut":
            eps = 0.18
        else: eps = 0.3
        
        dbscan_labels, clustered_points_xyz = unsup_segmentation.crop_clustering_dbscan(eps, filtered_crop_points)
        print("DBSCAN DONE")
        import random
        #Convert clustered_tree_points to an Open3D point cloud
        dbscan_clusters_pcd = o3d.geometry.PointCloud()
        dbscan_clusters_pcd.points = o3d.utility.Vector3dVector(clustered_points_xyz)

        dbscan_clusters_filtered_points, filtered_labels = pcd_filtering.dbscan_cluster_filtering(dbscan_clusters_pcd, 15, 10000, dbscan_labels)
        # Ensure dbscan_clusters_filtered_points is a PointCloud object
        if isinstance(dbscan_clusters_filtered_points, o3d.geometry.PointCloud):
            # Assign random colors to each cluster
            cluster_colors = {}
            for label in np.unique(filtered_labels):
                if label == -1:  # Skip noise points
                    continue
                color = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]  # Generate a random RGB color
                cluster_colors[label] = color

            # Assign colors to each point based on its cluster
            point_colors = []
            for label in filtered_labels:
                if label == -1:  # Noise points
                    point_colors.append([0.5, 0.5, 0.5])  # Gray color
                else:
                    point_colors.append(cluster_colors[label])

            # Set colors for the clustered tree points
            dbscan_clusters_filtered_points.colors = o3d.utility.Vector3dVector(point_colors)
        # Do DBSCAN Post Processing, Separating Wrongly Adjoined Trees
        # Convert clustered points to an Open3D point cloud
        dbscan_clusters_pcd = o3d.geometry.PointCloud()
        dbscan_clusters_pcd.points = o3d.utility.Vector3dVector(clustered_points_xyz)

        # Assuming dbscan_clusters_filtered_points and filtered_labels are already defined

        cluster_labels = np.unique(filtered_labels)
        new_cluster_labels = {}
        current_label = 0
        print("DBSCAN pt 2 start")
        for label in cluster_labels:
            if label == -1:  # Skip noise points
                continue
            print("Label 1")
            cluster_points = np.asarray(dbscan_clusters_filtered_points.points)[filtered_labels == label]
            hull = analyzer.create_convex_hull(cluster_points)
            hull_points = cluster_points[hull.vertices]

            # Calculate longest distance within the hull
            dist_matrix = distance_matrix(hull_points, hull_points)
            length = np.max(dist_matrix)

            longest_pair_indices = np.unravel_index(np.argmax(dist_matrix, axis=None), dist_matrix.shape)
            longest_vector = hull_points[longest_pair_indices[0]] - hull_points[longest_pair_indices[1]]
            
            # Calculate the unit vector of the longest distance
            longest_unit_vector = longest_vector / np.linalg.norm(longest_vector)
            perpendicular_vector = np.array([-longest_unit_vector[1], longest_unit_vector[0], 0])  # 90 degrees rotation in 2D
            
            # Project hull points onto the perpendicular vector
            perpendicular_projections = np.dot(hull_points, perpendicular_vector)
            width = np.max(perpendicular_projections) - np.min(perpendicular_projections)

            ratio = np.round(length/width) if width != 0 else 0
            if width < 0.95:
                ratio = 1
            if ratio >= 1.7:
                ratio = round(ratio)
            else:
                ratio = 1

            projections = np.dot(cluster_points, longest_vector)
            increments = np.linspace(np.min(projections), np.max(projections), int(ratio) + 1)

            #print(f"Length: {length}\nWidth: {width}\nRatio: {ratio}\n")
            # Split points into new clusters based on increments
            for i in range(len(increments) - 1):
                lower_bound = increments[i]
                upper_bound = increments[i + 1]
                
                # Select points within the current increment range
                new_cluster_points = cluster_points[(projections >= lower_bound) & (projections < upper_bound)]

                # Store new clusters with unique labels
                new_cluster_labels[current_label] = new_cluster_points
                current_label += 1

        # Convert new clusters to Open3D point clouds and visualize
        final_pcd = o3d.geometry.PointCloud()
        for label, points in new_cluster_labels.items():
            # Ensure points are in the correct shape
            if points.shape[1] != 3:
                print(f"Error: Points for label {label} must be 2D array with shape (N, 3), got shape {points.shape}")
                continue  # Skip this cluster if the shape is incorrect

            cluster_pcd = o3d.geometry.PointCloud()
            cluster_pcd.points = o3d.utility.Vector3dVector(points)

            # Generate a random color
            color = np.random.rand(3)  # Random color in RGB
            cluster_pcd.paint_uniform_color(color)  # Assign the same color to all points in the cluster
            
            final_pcd += cluster_pcd

        print("final cluster made")
        # Calculate cluster centers
        # new_cluster_labels = {key: value for key, value in new_cluster_labels.items() if not np.all(value == 0)}
        # new_cluster_labels = {key: value[~np.isnan(value)] for key, value in new_cluster_labels.items()}

        # Visualize the heights and point cloud data
        if mode == "height":
            heights, labels = analyzer.calculate_heights_and_labels(new_cluster_labels, filtered_ground_pcd)

            # Calculate cluster centers
            cluster_centers = analyzer.calculate_cluster_centers(new_cluster_labels)

            # Visualize the heights and point cloud data
            analyzer.visualize_the_metrics_and_pcd(heights, final_pcd, cluster_centers, "Height", "m")

        elif mode == "volume":
            volume_dicts = analyzer.calculate_volumes_for_clusters(new_cluster_labels, filtered_ground_pcd)

            # Calculate cluster centers
            cluster_centers = analyzer.calculate_cluster_centers(new_cluster_labels)

            analyzer.visualize_the_metrics_and_pcd(volume_dicts, final_pcd, cluster_centers, metric = "Volume", units = "m^3")


#############################################################
#############################################################
#################### GUI PART STARTS HERE ################### 
#############################################################
#############################################################

class ReviewListFrame(tk.Frame):
    def __init__(self, parent, controller):#, mode):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        folder_path = "./review_saved_data/" + self.controller.crop + "/"  # Set this to the path of your folder
        self.folder_path = folder_path

        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.configure(bg="white")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.configure(bg="#FFFFFF")
        self.scrollable_frame.bind(
                "<Configure>",
                self.on_frame_configure
        )
 
 
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_resized)
        self.update_list()
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame,
                                  anchor="nw")
 

    def on_canvas_resized(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
        self.scrollable_frame.config(width=canvas_width)

        
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Run the update scroll after all the elements loaded in
        self.after(100, self.update_scroll_region)


    def update_scroll_region(self):
        # Adjust the scrollregion dynamically
        content_height = self.scrollable_frame.winfo_height() 
        canvas_height = self.canvas.winfo_height()
        if content_height < canvas_height:
            #print(f" self.scrollable_frame.winfo_height()  + self.canvas.winfo_height() ")
            #print(f"{self.scrollable_frame.winfo_height()}  + {self.canvas.winfo_height()} ")
            #print("Adjusting scrollable_frame dynamically")
            self.canvas.configure(scrollregion=(0, 0, self.canvas.winfo_width(), canvas_height))
            #print(f"0, 0, {self.canvas.winfo_width()}, {canvas_height}")
        else:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))



    def update_list(self, *args):
        # Clear previous contents
        self.folder_path = "./review_saved_data/" + self.controller.crop + "/"  # Set this to the path of your folder
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Get list of files
        files = os.listdir(self.folder_path)
        if not files:
            no_data_label = ttk.Label(self.scrollable_frame, text="No Data Found")
            no_data_label.pack(fill="x", pady=10)
        else:
            for file in files:
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    self.add_file_row(file_date)

    def add_file_row(self, file_date):
        frame = tk.Frame(self.scrollable_frame, bg="#EFEFEF")

        date_label = ttk.Label(frame, text=file_date)
        date_label.pack(side=tk.LEFT, padx=10)

        btn_result_gradient = ttk.Button(frame, text="View Result Gradient",
                                         command=lambda: self.view_result_gradient(file_date))
        btn_result_gradient.pack(side=tk.RIGHT, padx=10)

        btn_result_map = ttk.Button(frame, text="View Result Map",
                                    command=lambda: self.view_result_map(file_date))
        btn_result_map.pack(side=tk.RIGHT, padx=10)

        btn_export_csv = ttk.Button(frame, text="Export to CSV",
                                    command=lambda: self.export_to_csv(file_date))
        btn_export_csv.pack(side=tk.RIGHT, padx=10)

        review_button = ttk.Button(frame, text="Review", command=lambda: self.review_file(file_date))
        review_button.pack(side=tk.RIGHT, padx=10)

        frame.pack(fill='x', expand=True, pady=5)

    def view_result_gradient(self, file_date):
            print(f"Viewing Result Gradient from : {file_date}")

    def view_result_map(self, file_date):
            print(f"Viewing Result Map from : {file_date}")

    def export_to_csv(self, file_date):
            print(f"Exporting to CSV: {file_date}")

    # Currently has no use after Review btn removal and adding 3 buttons,
    # but it has good code that can be recycled
    def review_file(self, file_date):
            print(f"Reviewing file from date: {file_date}")
            files = os.listdir(self.folder_path)
            
            for file in files:
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_modification_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    
                    if file_modification_date == file_date:
                        try:
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                                if len(lines) >= 4:
                                    fourth_line = lines[3].strip()  # Assuming the fourth line index is 3 (0-based index)
                                    print("Fourth line:", fourth_line)
                                    
                                    # Find the .ply file in the directory specified in fourth_line
                                    ply_files = [f for f in os.listdir(fourth_line) if f.endswith('.ply')]
                                    if len(ply_files) == 1:
                                        ply_file_path = os.path.join(fourth_line, ply_files[0])
                                        ply_file_path = ply_file_path.replace("\\", "/")
                                        print("Found .ply file:", ply_file_path)
                                        
                                        # Run height and analysis script in a separate thread
                                        threading.Thread(target=self.run_analysis_script, args=(ply_file_path,)).start()
                                    else:
                                        print("Error: No .ply file found in directory.")

                                else:
                                    print("File does not have at least 4 lines.")
                        except FileNotFoundError:
                            print(f"File {file_path} not found.")

    def run_analysis_script(self, ply_file_path):
        crop_type = self.controller.crop
        mode = self.controller.mode
        voxel_size = 0.2
        try:
            height_and_analysis_script(ply_file_path, voxel_size, crop_type, mode)
        except Exception as e:
            print(f"Error running analysis script: {e}")
    


#self.controller.show_frame("FinalReviewScreen")
