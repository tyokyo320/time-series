import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

#######################################################################################################################
# test data file
test_data_path = '../data/test.csv'

# param
nTrial = 10
epoch = 414915
sampling_interval = 1

# color dict
color_dict = {
    1: '#1f77b4',
    2: '#ff7f0e',
    3: '#2ca02c',
    4: '#d62728',
    5: '#9467bd',
    # 6: '#8c564b',
    # 7: '#e377c2',
}

# for CLA lebel
label_color_map = {
    'CLA(Fit)': color_dict[1],
    'CLA(Wide)': color_dict[2],
    'CLA(Narrow)': color_dict[3],
    'CLA-DR': color_dict[4],
}

#######################################################################################################################
# start and end index -> WARNING: start index must be 0 not 1
# index
# predict: 0 - 414914 -> total 414915
# error  : 414916 -> 829830 -> total 414915
# zoom_coords = ((zoom_xmin, zoom_xmax), (zoom_ymin, zoom_ymax))
#######################################################################################################################
# All observation
# start = 0
# end = 414914
#######################################################################################################################
# first day
# start = 0
# end = 95
# zoom_coords = ((80, 95), (0, 200))
#######################################################################################################################
# last day
start = 414819
end = 414914
# zoom_coords_max = ((414860, 414900), (6450, 6800))
# zoom_coords_min = ((414820, 414850), (4750, 5000))
# zoom_coords = ((414900, 414914), (50, 300))
#######################################################################################################################
error_abs_start = start+epoch+1
error_abs_end = end+epoch+1

# start = 411937 # last 1 month
cell_synapases_start = 0

#######################################################################################################################
###################################################### Case1 #######################################################
# Case 1: Original
case1_predict_results_path = "../output/electric-consumption/case1/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case2 #######################################################
# Case 2
case2_predict_results_path = "../output/electric-consumption/case2/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case3 #######################################################
# Case 3
case3_predict_results_path = "../output/electric-consumption/case3/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case4 #######################################################
# Case 4: Proposed
case4_predict_results_path = "../output/electric-consumption/case4/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
