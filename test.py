import nibabel as nib
from nilearn import datasets
from nibabel.viewers import OrthoSlicer3D
example_filename = './Haxby/sub-1/anat/sub-1_T1w.nii.gz'
fD_filename = './Haxby/sub-1/func/sub-1_task-objectviewing_run-01_bold.nii.gz'
#img = nib.load(example_filename)
#OrthoSlicer3D(img.dataobj).show()
from nilearn import plotting
#plotting.plot_glass_brain(example_filename)
plotting.plot_roi(example_filename,
                 cmap='Paired')
#plotting.show()
"""
利用 nilearn.input_data.NiftiMasker来提取mask上的fMRI数据，
并将其转换为数据序列
"""

from nilearn.masking import compute_epi_mask
mask_img = compute_epi_mask(example_filename)
from nilearn.image.image import mean_img
# Compute the mean EPI: we do the mean along the axis 3, which is time
mean_haxby = mean_img(example_filename)
from nilearn.plotting import plot_epi, show
plot_epi(mean_haxby, colorbar=True, cbar_tick_format="%i")
# Visualize it as an ROI
from nilearn.plotting import plot_roi
plot_roi(mask_img, mean_haxby)
from nilearn.masking import apply_mask
masked_data = apply_mask(example_filename, mask_img)

# And now plot a few of these
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 5))
plt.plot(masked_data[:150])
plt.xlabel('Time [TRs]', fontsize=16)
plt.ylabel('Intensity', fontsize=16)
plt.xlim(0, 150)
plt.subplots_adjust(bottom=.12, top=.95, right=.95, left=.12)

show()

from nilearn.input_data import NiftiMasker
masker = NiftiMasker(mask_img=mask_img, standardize=True)
fmri_masked = masker.fit_transform(example_filename)

# 打印frmi_masked
print(fmri_masked)

