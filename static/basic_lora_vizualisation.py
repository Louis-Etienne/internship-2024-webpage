from html4vision import Col, imagetable
import os

#parent_folder_name = os.path.dirname(os.path.dirname(__file__))
path_to_results = os.path.join('static')
path_to_results = ""
methods_list = [
    '2024-08-12_10-05-24-car-terior_2.0--rank_1-PointCloud',
    '2024-08-12_10-20-32-car-terior_2.0--rank_4-PointCloud',
    '2024-08-12_10-37-42-car-terior_2.0--rank_16-PointCloud',
    '2024-08-12_10-54-48-car-terior_2.0--rank_64-PointCloud',
    '2024-08-12_11-35-38-car-terior_2.0--rank_controlnet-PointCloud',
    '2024-08-12_12-00-42-car-terior_2.0--rank_ZEROCOMP-PointCloud',
]

cols = [
    Col('id1', 'ID'),
    Col('img', 'GT', os.path.join(path_to_results, methods_list[0], '*_dst_comp.png')),
    Col('img', 'lora rank-1', os.path.join(path_to_results, methods_list[0], '*_pred_seed_1_comp.png')),
    Col('img', 'lora rank-4', os.path.join(path_to_results, methods_list[1], '*_pred_seed_1_comp.png')),
    Col('img', 'lora rank-16', os.path.join(path_to_results, methods_list[2], '*_pred_seed_1_comp.png')),
    Col('img', 'lora rank-64', os.path.join(path_to_results, methods_list[3], '*_pred_seed_1_comp.png')),
    Col('img', 'ControlNet finetuned', os.path.join(path_to_results, methods_list[4], '*_pred_seed_1_comp.png')),
    Col('img', 'ZeroComp untouched', os.path.join(path_to_results, methods_list[5], '*_pred_seed_1_comp.png')),
     Col('img', 'Diffuse', os.path.join(path_to_results, methods_list[0], '*_comp_diffuse.png')),
    Col('img', 'Normals', os.path.join(path_to_results, methods_list[0], '*_comp_normal.png')),
    Col('img', 'Depth', os.path.join(path_to_results, methods_list[0], '*_comp_depth.png')),
    Col('img', 'Mask', os.path.join(path_to_results, methods_list[0], '*_comp_mask.png')),
    Col('img', 'Shading', os.path.join(path_to_results, methods_list[0], '*_comp_shading.png')),
    Col('img', 'Metallic', os.path.join(path_to_results, methods_list[0], '*_comp_metallic.png')),
    Col('img', 'Roughness', os.path.join(path_to_results, methods_list[0], '*_comp_roughness.png')),
]

imagetable(cols=cols, sticky_header=True, overlay_toggle=True,
           out_file='car_test_set.html',
           imsize=1,
           imscale=0.5,
           style='''img {border: 1px solid black;-webkit-box-shadow: 2px 2px 1px #ccc; box-shadow: 2px 2px 1px #ccc;}
                    thead {background-color: #EEEEEE; border: 1px solid black;-webkit-box-shadow: 2px 2px 1px #ccc; box-shadow: 2px 2px 1px #ccc;}'''
)


