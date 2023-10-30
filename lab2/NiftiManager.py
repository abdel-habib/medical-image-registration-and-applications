import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

class NiftiManager:
    def __init__(self) -> None:
        pass

    def load_nifti(self, file_path):
        '''Loads the NIfTI image and access the image data as a Numpy array.'''
        nii_image = nib.load(file_path)
        data_array = nii_image.get_fdata()

        return data_array, nii_image

    def show_nifti(self, file_data, title, slice=25):
        '''Displays a single slice from the nifti volume (change the slice index as needed).'''
        plt.imshow(file_data[:, :, slice], cmap='gray')
        plt.title(title)
        plt.colorbar()
        plt.show()

    def show_label_seg_nifti(self, label, seg, subject_id, slice=25):
        '''Displays both segmentation and ground truth labels as passed to the function.'''
        plt.figure(figsize=(20, 7))
        
        plt.subplot(1, 2, 1)
        plt.imshow(label[:, :, slice], cmap='gray') 
        plt.title(f'Label Image (Subject ID={subject_id})')
        plt.colorbar()

        plt.subplot(1, 2, 2)
        plt.imshow(seg[:, :, slice], cmap='gray') 
        plt.title(f'Segmentation Image (Subject ID={subject_id})')
        plt.colorbar()
        plt.show()

    def normalize_nifti(self, volume):
        '''Performs Min-Max scaling normalization on nifti volumes.'''
        # Calculate the minimum and maximum values of the volume
        min_val = np.min(volume)
        max_val = np.max(volume)

        # Perform min-max scaling normalization
        normalized_volume = (volume - min_val) / (max_val - min_val)

        return normalized_volume

    def show_mean_volumes(self, mean_csf, mean_wm, mean_gm, slice=128):
        '''Displays the mean volumes for CSF, WM, and GM.'''
        plt.figure(figsize=(20, 7))

        plt.subplot(1, 3, 1)
        plt.imshow(mean_csf[:, :, slice], cmap='gray')
        plt.title('Mean CSF Volume')
        plt.colorbar()

        plt.subplot(1, 3, 2)
        plt.imshow(mean_wm[:, :, slice], cmap='gray')
        plt.title('Mean WM Volume')
        plt.colorbar()

        plt.subplot(1, 3, 3)
        plt.imshow(mean_gm[:, :, slice], cmap='gray')
        plt.title('Mean GM Volume')
        plt.colorbar()

        plt.show()

    def show_combined_mean_volumes(self, mean_csf, mean_wm, mean_gm, slice_to_display=128):
        # Stack the mean volumes along the fourth axis to create a single 4D array
        combined_mean_volumes = np.stack((mean_csf, mean_wm, mean_gm), axis=3)
    
        # Choose the channel you want to display (0 for CSF, 1 for WM, 2 for GM)
        channel_to_display = 0  # Adjust as needed
    
        # Display the selected channel
        plt.imshow(combined_mean_volumes[:, :, :, :][:, :, slice_to_display]) # [:, :, :, channel_to_display]
        plt.axis('off')  # Turn off axis labels
        plt.title(f'Mean Volume of Slice {slice_to_display}')  # Add a title
        plt.show()
