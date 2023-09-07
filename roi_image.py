import numpy as np
import tifffile

# Specify the paths to the TIFF files
tif_file_1 = "Y:\public\projects\SaEl_20220201_VIP\\2pdata\\RSCaxonimaging\se062\F\\raw_data\\file_00001_00005.tif"

# Load the TIFF files
z_stack = tifffile.imread(tif_file_1)
z_stack_average = np.mean(z_stack, axis=0)

# Combine the data from the two TIFF files into a Z-stack

# Save the Z-stack as a TIFF file
tifffile.imwrite("Y:\public\projects\SaEl_20220201_VIP\\2pdata\\RSCaxonimaging\se062\F\z_stack.tif", z_stack_average)


# import numpy as np
# from skimage.io import imsave
# import pickle

# # Load the registered binary file
# registered_data = np.fromfile('Y:\public\projects\SaEl_20220201_VIP\\2pdata\\RSCaxonimaging\se043\F\suite2p\plane0\data.bin', dtype=np.float32)
# ops = np.load('Y:\public\projects\SaEl_20220201_VIP\\2pdata\\RSCaxonimaging\se043\F\suite2p\plane0\ops.npy',allow_pickle=True)
# ops = ops.item()
# # Determine the dimensions of the data (number of planes, height, width)
# number_of_frames = ops['nframes'] # Replace with the actual number of planes
# height = ops['Ly']  # Replace with the actual height
# width = ops['Lx']  # Replace with the actual width
# number_of_planes = ops['nplanes'] # Replace with the actual number of planes
# registered_data = registered_data.reshape(number_of_frames, number_of_planes, height, width)

# # Initialize an empty array for the Z-stack
# z_stack = np.empty((number_of_frames, number_of_planes, height, width), dtype=np.float32)
# # # Load the data for each plane
# for plane_idx in range(number_of_planes):
#     file_path = f'Y:\public\projects\SaEl_20220201_VIP\\2pdata\\RSCaxonimaging\se043\F\suite2p\plane{plane_idx}\data.bin'  # Replace with the actual file paths
#     plane_data = np.fromfile(file_path, dtype=np.float32)
#     plane_data = plane_data.reshape((number_of_frames, height, width))
#     z_stack[:, plane_idx, :, :] = plane_data

# Save the Z-stack as a TIFF file
# imsave('path_to_save_z_stack.tif', z_stack)
# Reshape the data to the dimensions: (number of planes, height, width)
# registered_data = registered_data.reshape(number_of_frames, height, width)

# Save the Z-stack as a TIFF file
# imsave('Y:\public\projects\SaEl_20220201_VIP\\2pdata\\RSCaxonimaging\se043\F\suite2p\plane0\z_stack.tif', z_stack)
# import matplotlib.pyplot as pltf
# import pickle

# data = np.fromfile('Y:\public\projects\SaEl_20220201_VIP\\2pdata\RSCaxonimaging\se043\F\suite2p\plane0\data.bin',dtype=np.float32)
# ops = np.load('Y:\public\projects\SaEl_20220201_VIP\\2pdata\RSCaxonimaging\se043\F\suite2p\plane0\ops.npy',allow_pickle=True)
# ops = ops.item()
# num_frames = ops['nframes']
# width = ops['Lx']
# height = ops['Ly']
# frame_rate=ops['fs']
# num_planes = ops['nplanes']___
# print(ops['nframes'])
# #data = data.reshape(num_planes,num_frames,height,width)

# roi_index = 31  # Index of the ROI of interest
# roi_coords = ops['stat'][roi_index]['med']  # Median coordinates of the ROI
# x_start, y_start, width_roi, height_roi = roi_coords[0], roi_coords[1], roi_coords[2], roi_coords[3]
# start_frame = 6500  # Starting frame index for averaging
# end_frame = 6600  # Ending frame index for averaging

# average_image = np.mean(data[:, start_frame:end_frame, y_start:y_start+height_roi, x_start:x_start+width_roi], axis=1)
# plt.imshow(average_image, cmap='gray')
# plt.axis('off')
# plt.show()
