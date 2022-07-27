from nilearn import datasets
#haxby_dataset = datasets.fetch_openneuro_dataset('/Users/zhangxiaoheng/nilearn_data')
# print basic information on the dataset
print("dataset position:",datasets.get_data_dirs())
from nilearn.datasets import MNI152_FILE_PATH
# 注：变量mni152_file_path只是nifti文件的路径
print('Path to MNI152 template: %r' % MNI152_FILE_PATH)

motor_im=datasets.fetch_neurovault_motor_task()
#print(motor_im.images[0])

file_name=motor_im.images[0]

from nilearn import plotting
plotting.plot_img(MNI152_FILE_PATH)

from nilearn import image
smooth_anat_img = image.smooth_img(MNI152_FILE_PATH, fwhm=3)

# 打印平滑
print(smooth_anat_img)
plotting.plot_stat_map(smooth_anat_img)
#rsn=datasets.fetch_atlas_smith_2009()['rsn10']
#print(rsn)
#first_image=image.index_img(rsn,0)
#plotting.plot_img(first_image)
plotting.show()

