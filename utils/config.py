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
    0: '#1f77b4',
    1: '#ff7f0e',
    2: '#2ca02c',
    3: '#d62728',
    # 4: '#9467bd',
    # 5: '#8c564b',
    # 6: '#e377c2',
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
zoom_coords = ((414900, 414914), (50, 300))
#######################################################################################################################
error_abs_start = start+epoch+1
error_abs_end = end+epoch+1

# start = 411937 # last 1 month
cell_synapases_start = 0

#######################################################################################################################
# Case 1: Original
predict_results_path = "../output/original/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
cell_synapases_history_path = '../output/original/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'

# Case 2: inf
inf_predict_results_path = "../output/infinity/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
inf_cell_synapases_history_path = '../output/infinity/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'

# Case 3: 10%
tenpercent_predict_results_path = "../output/tenpercent/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
tenpercent_cell_synapases_history_path = '../output/tenpercent/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'

# Case 4: first year as min and max
firstyear_predict_results_path = "../output/firstyear/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
firstyear_cell_synapases_history_path = '../output/firstyear/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'
#######################################################################################################################
