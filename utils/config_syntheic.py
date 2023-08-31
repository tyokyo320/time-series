import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

#######################################################################################################################
# test data file
# test_data_path = '../data/syntheic/sin_wave_nonoise.csv'
test_data_path = '../data/syntheic/trend_sin_nonoise.csv'

# param
nTrial = 10
epoch = 19999
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
# All observation (sin_wave_nonoise)
start = 19899
end = 19998
# zoom_coords = ((19920, 19930), (0, 1))
#######################################################################################################################
error_abs_start = start+epoch+1
error_abs_end = end+epoch+1

# start = 411937 # last 1 month
cell_synapases_start = 0

#######################################################################################################################
# sin_wave_nonoise
# predict_results_path = "../output/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
predict_results_path = "../output/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"
