import open3d as o3d

# Load voxel data and convert to Open3D VoxelGrid
voxel_data = o3d.io.read_point_cloud("filtered.ply")

voxel_size = 0.008
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(voxel_data, voxel_size)

o3d.visualization.draw_geometries([voxel_grid])
