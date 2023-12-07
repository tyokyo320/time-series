import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# param
nTrial = 10
period = 100
epoch = 20000   # sin_wave_nonoise.csv / trend_sin_nonoise.csv
# epoch = 40000   # change_sin_nonoise.csv
# epoch = 60000   # change2_sin_nonoise.csv

# color dict
color_dict = {
    1: '#1f77b4',
    2: '#ff7f0e',
    3: '#2ca02c',
    4: '#d62728',
    # 5: '#9467bd',
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
# start = 0
# end = 20000
#######################################################################################################################
# All observation (trend_sin_nonoise)
start = 0
end = 20000
#######################################################################################################################
# All observation (change_sin_nonoise)
# start = 0
# end = 40000
#######################################################################################################################
# All observation (change2_sin_nonoise)
# start = 0
# end = 60000
#######################################################################################################################

#######################################################################################################################
###################################################### Case1 #######################################################
# sin_wave_nonoise
# case1_error_by_period_path = f"../output/syntheic/case1/sin_wave_nonoise/error_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case1_error_by_period_path = f"../output/syntheic/case1/trend_sin_nonoise/error_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case1_error_by_period_path = f"../output/syntheic/case1/change_sin_nonoise/error_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case1_error_by_period_path = f"../output/syntheic/case1/change2_sin_nonoise/error_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case2 #######################################################
# sin_wave_nonoise
# case2_error_by_period_path = f"../output/syntheic/case2/sin_wave_nonoise/error_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case2_error_by_period_path = f"../output/syntheic/case2/trend_sin_nonoise/error_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case2_error_by_period_path = f"../output/syntheic/case2/change_sin_nonoise/error_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case2_error_by_period_path = f"../output/syntheic/case2/change2_sin_nonoise/error_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case3 #######################################################
# sin_wave_nonoise
# case3_error_by_period_path = f"../output/syntheic/case1/sin_wave_nonoise/error_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case3_error_by_period_path = f"../output/syntheic/case3/trend_sin_nonoise/error_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case3_error_by_period_path = f"../output/syntheic/case3/change_sin_nonoise/error_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case3_error_by_period_path = f"../output/syntheic/case3/change2_sin_nonoise/error_change2_sin_nonoise_cells32_n421_r13d08.csv"
###################################################### Case4 #######################################################
# sin_wave_nonoise
# case4_error_by_period_path = f"../output/syntheic/case4/sin_wave_nonoise/error_sin_wave_nonoise_cells32_n421_r13d08.csv"

# trend_sin_nonoise
case4_error_by_period_path = f"../output/syntheic/case4/trend_sin_nonoise/error_trend_sin_nonoise_cells32_n421_r13d08.csv"

# change_sin_nonoise
# case4_error_by_period_path = f"../output/syntheic/case4/change_sin_nonoise/error_change_sin_nonoise_cells32_n421_r13d08.csv"

# change2_sin_nonoise
# case4_error_by_period_path = f"../output/syntheic/case4/change2_sin_nonoise/error_change2_sin_nonoise_cells32_n421_r13d08.csv"
#######################################################################################################################
