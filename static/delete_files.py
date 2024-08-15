import os
import glob


path = os.path.join('eval', 'controlnet_eval')
keep = '_pred_seed_1_comp.png'
path_all = os.path.join(path, '*')
path_keep = os.path.join(path, f'*{keep}')

all_files = glob.glob(path_all)
keep_files = glob.glob(path_keep)
print('# all files :', len(all_files), 'example of all_files :', all_files[0])
print('# files to keep :', len(keep_files), 'example of file :', keep_files[0])

total = 0
for file in all_files:
    if file not in keep_files:
        os.remove(file)
        total += 1
        
print('total files removed : ', total)