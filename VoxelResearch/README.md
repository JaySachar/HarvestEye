# Instructions on using Voxel Research folder

1. Place you colorized.ply into this directory.
2. IMPORTANT: Run cut_below_12656.py to get filtered.ply
3. Run any of the other python or C++ scripts.
{Note: You can use .bat scripts to automate the compile of the program and running it.}

To compile C++, use: g++ color_to_voxel.cpp -o color_to_voxel.exe

Folder voxelization contains code to voxelize "filtered.ply" via Open3D.
So, to run it, place a generated filtered.ply from cut_below_12656.py code output into that
folder too.

(cut_to_voxel.cpp - cuts the data to a specified box. Output: final.ply)
(color_to_voxel.cpp - colors the data to a specified box. Output: final.ply)
(voxelize folder - has a script that takes any .ply file and voxelizes it depending on voxel size
specified in the code)

# info on colorized.ply

## (Error filter) Cutting error points MANUALLY
### Above the Ground Level
Recentering on point [-0.576001 -0.546050 0.520090] [658,368]

### Cut of below this point
Recentering on point [0.156378 -1.173403 1.265624] [749,485]

### A point even lower than the one that we need to cut down from
Recentering on point [-0.100464 -0.800503 1.359845] [457,506]

#### Result:
Worked like a charm.
Had to remember that there are headers for the first 10 lines
and that the 3rd line has a total # of points that had to be updated
after I removed a bunch of them.

## (Boundaries) Find the boundaries of the 3d point cloud map

### Max and Min values in X
### Max and Min values in Y
#### Result:

total length is :443675
current length is:441238
Min_X: 2.118051019181991
Max_X: -2.549141111825613

Min_Y: 2.7519144888374116
Max_Y: -1.688193550476225

Min_Z: 7.307491222631943
Max_Z: -0.0995793167136918


## (Try for voxel size) 

### Take a point 0,0,0 and see how much of a block of 0.2 (ex: -0.1->0.1)

#### RESULT:

I tried 2, 1.5, 1, 0.5, 0.25, 0.125, 0.0375, 0.01875 
Yes, after 0.125 i stopped dividing by 2, I got distracted by removing Z axis out of bounding box if statement
and wrote the number wrong, because I don't know where it came from.

## How to render 3D result of Voxelization, when I actually attempt making Voxels?

Apparently, Open3D has a very easy function to call for loading the point_cloud_data
as well as voxelizing it and visualizing it.
The code is in voxelization/ folder


