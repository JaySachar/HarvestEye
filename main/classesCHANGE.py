import numpy as np
import pandas as pd
import cv2 
import subprocess
import os
import tempfile
from sklearn.linear_model import RANSACRegressor
import matplotlib.pyplot as plt
# ImageProcessor is responsible for housing general image processing functions
# This includes downsampling images, and any other edits we'd have to make to them 
class ImageProcessor:
    
    def __init__(self, img_directory):
        # directory [STRING]: "C:/Users/.../XXX"
        self.img_directory = img_directory
        self.imgs, self.img_type = self.file_extension_grabber(img_directory)

    def image_preprocessing(self):
        # Define any preprocessing we want. Could break this up to different functions as well, ie a image format changer format 
        # A downsampling function etc. 
        # A function for turning a .TIF to a .JPG to pass to the PointCloudGenerator 
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

class SegmentationAlgorithm:
    def __init__(self):
        pass
    
class CropAnalyzer:
    def __init__(self):
        pass

class GUI:
    def __init__(self):
        pass