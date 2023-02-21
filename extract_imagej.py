import os
import pathlib
import numpy as np
from suite2p import extraction
from roifile import ImagejRoi

def load_rois_from_imagej(folder):
    rois = []
    for file in os.listdir(folder):
        if file.endswith('.roi'):
            roi = ImagejRoi.fromfile(file)
            rois.append(roi)
    return rois

# Define suite2p path
for n in range(4):
    path_to_suite2p = pathlib.Path('Z:\mrsic_flogel\public\projects\SaEl_20220201_VIP\2pdata\RSCsilencing\se031\D\suite2p')
    plane = 'plane' + str(n)
    print(plane)
    plane_path = path_to_suite2p / plane
    path_to_roi_folder = plane_path/"manual_red"
    np.load()
    rois=load_rois_from_imagej(path_to_roi_folder)
    stat_manual=[]
    stat_all=np.load(os.path.join(plane_path,'stat.npy',allow_pickle=True))
    for roi in rois:
        xpix=roi[:,0]
        ypix=roi[:,1]
        lam=np.ones(ypix.shape, np.float32) # initiate array of weights for each pixel normalize weights?
        stat_manual.append('ypix':ypix.,'xpix':xpix.,'lam':lam)

    stat_manual=detection.stats.roi_stats(stat_manual,)
    manual_cell_masks= [
        extraction.masks.create_cell_mask(stat,) for stat in stat_manual
    ]

    cell_pix = extraction.masks.create_cell_pix(stat_manual,Ly=xpix['ly'],lx=ypix['lx'])
    manual_neuropil_masks=extraction.masks.create_neuropil_masks[
        


    ]

# define function for loading ROIs from ImageJ

#path_to_roi_folder = '/home/rois'
#rois = load_rois_from_imagej(path_to_roi_folder)
#rois_array = rois_to_array(rois)

#F = np.load('F.npy', allow_pickle=True)
#Fneu = np.load('Fneu.npy', allow_pickle=True)
#spks = np.load('spks.npy', allow_pickle=True)
stat = np.load('stat.npy', allow_pickle=True)
print(stat)
#ops =  np.load('ops.npy', allow_pickle=True)
#ops = ops.item()
#iscell = np.load('iscell.npy', allow_pickle=True)

 
#extraction.extract.create_masks_and_extract(ops, stat, cell_masks=None, neuropil_masks=None)