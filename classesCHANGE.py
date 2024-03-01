import numpy as np
import pandas as pd
import os

# ImageProcessor is responsible for housing general image processing functions
# This includes downsampling images, and any other edits we'd have to make to them 
class ImageProcessor:
    
    def __init__(self, img_directory):
        # directory [STRING]: "C:/Users/.../XXX"
        self.imgs, self.img_type = self.file_extension_grabber(img_directory)

    def image_preprocessing(self):
        # Define any preprocessing we want. Could break this up to different functions as well, ie a image format changer format 
        # A downsampling function etc. 
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
                
        return image_files, ext # Return all the image files in the directory and the extensions of them                

    
# Create PointCloudGenerator as a child to ImageProcessor so we can encapsulate
# All image preprocessing functions
class PointCloudGenerator(ImageProcessor):
    def __init__(self, img_directory):
        super().__init__(img_directory) # Calls initializer for the ImageProcessor class
                                        # Takes the img_directory, and initializes the imgs and img_type attributes
                                        # The imgs attribute is a list of file names in the img_directory that are image files (based on the specified image_extensions)
                                        # The img_type attribute is the file extension of the first image file found in the img_directory (or None if no image files are found)
        
        self.point_cloud_data = self.generatePointCloud()

    def generatePointCloud(self):
        pointcloudfile = 1
        return pointcloudfile
    
# A class dedicated to stitching the images taken on the drone together. This can then be used for NDVI analysis    
class ImageStitcher(ImageProcessor):
    def __init__(self, img_directory):
        super().__init__(img_directory)
        self.stitched_img = self.stitch(self.imgs) # Pass the list that holds the directories to each image




class SegmentationAlgorithm:
    def __init__(self):
        pass
    
class CropAnalyzer:
    def __init__(self):
        pass

class GUI:
    def __init__(self):
        pass
    
