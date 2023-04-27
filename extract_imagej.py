import os
import pathlib
import numpy as np
from suite2p import extraction, detection
from roifile import ImagejRoi
from zipfile import ZipFile

def load_rois_from_imagej(folder):
    rois = []
    for file in os.listdir(folder):
        if file.endswith('.roi'):
            roi = ImagejRoi.fromfile(plane_path/'vip'/file)
            rois.append(roi)
    return rois

# Define suite2p path
for n in range(4):
    #path_to_suite2p = pathlib.Path('D:\\48E_red\suite2p\\')
    path_to_suite2p = pathlib.Path('Y:\public\projects\SaEl_20220201_VIP\\2pdata\\ACCsilencing\se048\E\suite2p')

    #path_to_suite2p = pathlib.Path('Z:\mrsic_flogel\public\projects\SaEl_20220201_VIP\\2pdata\\ACCsilencing\se048\E\suite2p')
    plane = 'plane' + str(n)
    print(plane)
    plane_path = path_to_suite2p / plane
    path_to_roizip_folder = plane_path/'vip.zip'
    with ZipFile(path_to_roizip_folder,'r') as zObject:
        zObject.extractall(path=plane_path/'vip')
    zObject.close()
    ops= np.load(os.path.join(plane_path,'ops.npy'),allow_pickle=True).item()
    ops['reg_file'] = os.path.join(plane_path,'data.bin')
    ops['reg_file_chan2'] = os.path.join(plane_path,'data_chan2.bin')
    ops['ops_path'] = os.path.join(plane_path,'ops.npy')
    ops['save_path'] = plane_path
    rois=load_rois_from_imagej(plane_path/'vip')
    stat_manual=[]
    # stat_all=np.load(os.path.join(plane_path,'stat.npy'),allow_pickle=True)
    for roi in rois:
        roi=roi.coordinates()
        xpix=roi[:,0]
        ypix=roi[:,1]
        lam=np.ones(ypix.shape, np.float16) # initiate array of weights for each pixel 
        lam /= lam.sum() #normalize weights
        stat_manual.append({'ypix':ypix.astype(int), 'xpix':xpix.astype(int) ,'lam':lam ,'npix': ypix.shape})# put everything into dictionary

    stat_manual=detection.stats.roi_stats(stat_manual,ops['Ly'],ops['Lx'],aspect=ops.get('aspect', None), diameter=ops['diameter'])
    manual_cell_masks= [
        extraction.masks.create_cell_mask(stat, Ly=ops['Ly'], Lx=ops['Lx'], allow_overlap=ops['allow_overlap']) for stat in stat_manual
        ]

    cell_pix = extraction.masks.create_cell_pix(stat_manual,Ly=ops['Ly'], Lx=ops['Lx'])
    manual_neuropil_masks=extraction.masks.create_neuropil_masks(
        ypixs=[stat['ypix'] for stat in stat_manual],
        xpixs=[stat['xpix'] for stat in stat_manual],
        cell_pix=cell_pix,
        inner_neuropil_radius=ops['inner_neuropil_radius'],
        min_neuropil_pixels=ops['min_neuropil_pixels'],
        )

    F, Fneu = extraction.extract.extract_traces_from_masks(ops, 
                                                        manual_cell_masks, 
                                                        manual_neuropil_masks)

    np.save(os.path.join(plane_path, 'F_red'), F)
    np.save(os.path.join(plane_path, 'F_red_neu'), Fneu)