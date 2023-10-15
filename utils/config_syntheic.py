import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

#######################################################################################################################
# test data file
# test_data_path = '../data/syntheic/sin_wave_nonoise.csv'
test_data_path = '../data/syntheic/trend_sin_nonoise.csv'
# test_data_path = '../data/syntheic/change_sin_nonoise.csv'
# test_data_path = '../data/syntheic/change2_sin_nonoise.csv'

# param
nTrial = 10
epoch = 19999   # sin_wave_nonoise.csv / trend_sin_nonoise.csv
# epoch = 39999   # change_sin_nonoise.csv
# epoch = 59999   # change2_sin_nonoise.csv
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
# start = 19900
# end = 20000
# zoom_coords = ((19970, 19980), (0.0, 0.1))
#######################################################################################################################
# All observation (trend_sin_nonoise)
start = 0
end = 20000
zoom_coords = ((19970, 19980), (0.0, 0.1))
#######################################################################################################################
# All observation (change_sin_nonoise)
# start = 39900
# end = 40000
# zoom_coords = ((39900, 40000), (0.0, 0.1))
#######################################################################################################################
# All observation (change2_sin_nonoise)

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
case1_predict_results_path = f"../output/syntheic/case1/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case1_predict_results_path = f"../output/syntheic/case1/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case1_predict_results_path = f"../output/syntheic/case1/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case2 #######################################################
# sin_wave_nonoise
# case2_predict_results_path = f"../output/syntheic/case2/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case2_predict_results_path = f"../output/syntheic/case2/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case2_predict_results_path = f"../output/syntheic/case2/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case2_predict_results_path = f"../output/syntheic/case2/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case3 #######################################################
# sin_wave_nonoise
# case3_predict_results_path = f"../output/syntheic/case3/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case3_predict_results_path = f"../output/syntheic/case3/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case3_predict_results_path = f"../output/syntheic/case3/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case3_predict_results_path = f"../output/syntheic/case3/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case4 #######################################################
# sin_wave_nonoise
# case4_predict_results_path = f"../output/syntheic/case4/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case4_predict_results_path = f"../output/syntheic/case4/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case4_predict_results_path = f"../output/syntheic/case4/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case4_predict_results_path = f"../output/syntheic/case4/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
#######################################################################################################################
###################################################### Case5 #######################################################
# sin_wave_nonoise
# case5_predict_results_path = f"../output/syntheic/case5/sin_wave_nonoise/InputOutput_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case5_predict_results_path = f"../output/syntheic/case5/trend_sin_nonoise/InputOutput_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case5_predict_results_path = f"../output/syntheic/case5/change_sin_nonoise/InputOutput_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case5_predict_results_path = f"../output/syntheic/case5/change2_sin_nonoise/InputOutput_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################