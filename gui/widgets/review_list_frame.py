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
def height_and_analysis_script(pcd_file_path, voxel_size = 0.25):
        pcd = o3d.io.read_point_cloud(pcd_file_path)
        
        pcd_functions = PointCloudGenerator(os.path.dirname(__file__))
        unsup_segmentation = UnsupervisedSegmentationAlgorithm()
        pcd_filtering = PointCloudFiltering()
        analyzer = CropAnalyzer()

        # Downsample the point cloud
        # Voxel size was normally 0.25 for meters
        
        downsampled_pcd = pcd_functions.downsamples_pointcloud(pcd, voxel_size)

        # Normalize the point cloud
        xyzrgb_normalized = pcd_functions.pcd_array_normalized(downsampled_pcd)

        # Define weights and number of clusters for KMeans
        weights = [5, 5, 500, 1, 550, 1]
        num_clusters = 2
        kmeans_labels, kmeans = unsup_segmentation.normalized_and_weighted_kmeans(weights, xyzrgb_normalized, num_clusters)

        # Prepare cluster colors array
        cluster_colors = np.zeros_like(xyzrgb_normalized[:, :3])  # Use only the XYZ part for colors

        # Define colors for clusters
        colors = {
            "green": [0, 150/255, 0],  # Green color
            "brown": [0.647, 0.165, 0.165]  # Brown color
        }

        # Identify the larger cluster
        larger_cluster_label = np.argmax(np.bincount(kmeans_labels))

        # Assign colors based on cluster sizes
        for i in range(num_clusters):
            color = colors["brown"] if i == larger_cluster_label else colors["green"]
            cluster_colors[kmeans_labels == i] = color

        seg_pcd = downsampled_pcd
        seg_pcd.colors = o3d.utility.Vector3dVector(cluster_colors)
        ground_points = np.asarray(seg_pcd.points)[kmeans_labels == larger_cluster_label]
        crop_points = np.asarray(seg_pcd.points)[kmeans_labels != larger_cluster_label]
        x_min, x_max = np.min(ground_points[:, 0]), np.max(ground_points[:, 0])
        x_range = x_max - x_min
        grid_resolution = x_range / 2

        # Filter the Ground Points list
        #filtered_ground_points = pcd_filtering.filter_ground_points(ground_points, 3, grid_resolution, 0.15)
        filtered_ground_points = pcd_filtering.filter_ground_points(ground_points, 1, 7, 0.001)
        filtered_ground_pcd = o3d.geometry.PointCloud()
        filtered_ground_pcd.points = o3d.utility.Vector3dVector(filtered_ground_points)
        filtered_crop_points = pcd_filtering.filter_points_by_grid(crop_points, 0.75, 0.5, 5)
        filtered_crop_pcd = o3d.geometry.PointCloud()
        filtered_crop_pcd.points = o3d.utility.Vector3dVector(filtered_crop_points)
        # Filter points based on DBSCAN clustering
        eps = 0.28  # epsilon value for DBSCAN
        dbscan_labels, clustered_points_xyz = unsup_segmentation.crop_clustering_dbscan(eps, filtered_crop_points)


        import random
        #Convert clustered_tree_points to an Open3D point cloud
        dbscan_clusters_pcd = o3d.geometry.PointCloud()
        dbscan_clusters_pcd.points = o3d.utility.Vector3dVector(clustered_points_xyz)

        dbscan_clusters_filtered_points, filtered_labels = pcd_filtering.dbscan_cluster_filtering(dbscan_clusters_pcd, 20, 10000, dbscan_labels)
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
            heights, labels = analyzer.calculate_heights_and_labels(filtered_labels, dbscan_clusters_filtered_points, filtered_ground_pcd)

        # Calculate cluster centers
        cluster_centers = analyzer.calculate_cluster_centers(filtered_labels, np.asarray(dbscan_clusters_filtered_points.points))

        # Visualize the heights and point cloud data
        analyzer.visualize_the_metrics_and_pcd(heights, dbscan_clusters_filtered_points, cluster_centers, metric = "Height", units = "m")
        analyzer.visualize_height_gradient(dbscan_clusters_filtered_points, filtered_ground_pcd)
        volume_dicts = analyzer.calculate_volumes_for_clusters(dbscan_clusters_filtered_points, filtered_labels, filtered_ground_pcd)
        analyzer.visualize_the_metrics_and_pcd(volume_dicts, dbscan_clusters_filtered_points, cluster_centers, metric = "Volume", units = "m^3")

class ReviewListFrame(tk.Frame):
    def __init__(self, parent, controller):
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

        review_button = ttk.Button(frame, text="Review", command=lambda: self.review_file(file_date))
        review_button.pack(side=tk.RIGHT, padx=10)

        frame.pack(fill='x', expand=True, pady=5)

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
        try:
            height_and_analysis_script(ply_file_path, voxel_size=0.25)
        except Exception as e:
            print(f"Error running analysis script: {e}")