import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

#######################################################################################################################
# test data file
# test_data_path = '../data/syntheic/sin_wave_nonoise.csv'
# test_data_path = '../data/syntheic/trend_sin_nonoise.csv'
# test_data_path = '../data/syntheic/change_sin_nonoise.csv'
test_data_path = '../data/syntheic/change2_sin_nonoise.csv'

# param
nTrial = 10
period = 100
# epoch = 19999           # sin_wave_nonoise.csv / trend_sin_nonoise.csv
# epoch = 39999         # change_sin_nonoise.csv
epoch = 59999         # change2_sin_nonoise.csv
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
# All observation (sin_wave_nonoise)
# start = 19900
# end = 20000
# zoom_coords_max = ((19918, 19930), (0.94, 1.02))
# zoom_coords_min = ((19968, 19980), (-0.05, 0.1))
#######################################################################################################################
# All observation (trend_sin_nonoise)
# start = 19900
# end = 20000
# zoom_coords_max = ((19918, 19930), (1.92, 2.02))
# zoom_coords_min = ((19968, 19980), (0.97, 1.05))
# zoom_coords_max = ((19918, 19930), (1.92, 2.05))    # All cases
# zoom_coords_min = ((19968, 19980), (0.90, 1.06))    # All cases
#######################################################################################################################
# All observation (change_sin_nonoise)
# start = 39900
# end = 40000
# zoom_coords_max = ((39918, 39930), (2.94, 3.02))
# zoom_coords_min = ((39968, 39980), (1.97, 2.07))
#######################################################################################################################
# All observation (change2_sin_nonoise)
start = 59900
end = 60000
zoom_coords_max = ((59918, 59930), (0.94, 1.02))
zoom_coords_min = ((59968, 59980), (-0.05, 0.1))
#######################################################################################################################
error_abs_start = start+epoch+1
error_abs_end = end+epoch+1

# start = 411937 # last 1 month
# cell_synapases_start = 0

#######################################################################################################################
# NEED TO FIX predict_results_path LIKE THAT: df_proposed = load_csv_data(config.proposed_predict_results_path)
#######################################################################################################################
###################################################### Case1 #######################################################
# sin_wave_nonoise
# case1_predict_results_path = f"../output/syntheic/case1/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
# case1_predict_results_path = f"../output/syntheic/case1/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case1_predict_results_path = f"../output/syntheic/case1/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
case1_predict_results_path = f"../output/syntheic/case1/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case2 #######################################################
# sin_wave_nonoise
# case2_predict_results_path = f"../output/syntheic/case2/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
# case2_predict_results_path = f"../output/syntheic/case2/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case2_predict_results_path = f"../output/syntheic/case2/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
case2_predict_results_path = f"../output/syntheic/case2/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case3 #######################################################
# sin_wave_nonoise
# case3_predict_results_path = f"../output/syntheic/case3/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
# case3_predict_results_path = f"../output/syntheic/case3/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case3_predict_results_path = f"../output/syntheic/case3/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
case3_predict_results_path = f"../output/syntheic/case3/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case4 #######################################################
# sin_wave_nonoise
# case4_predict_results_path = f"../output/syntheic/case4/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
# case4_predict_results_path = f"../output/syntheic/case4/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case4_predict_results_path = f"../output/syntheic/case4/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
case4_predict_results_path = f"../output/syntheic/case4/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################