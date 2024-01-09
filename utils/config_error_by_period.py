import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# param
nTrial = 10
period = 31
epoch = 414915

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
# All observation
start = 0
end = 414914
#######################################################################################################################

error_abs_start = start+epoch+1
error_abs_end = end+epoch+1

#######################################################################################################################
###################################################### Case1 #######################################################
# Case 1: Original
case1_error_by_period_path = f"../output/electric-consumption/case1/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case2 #######################################################
# Case 2
case2_error_by_period_path = f"../output/electric-consumption/case2/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case3 #######################################################
# Case 3
case3_error_by_period_path = f"../output/electric-consumption/case3/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
###################################################### Case4 #######################################################
# Case 4: Proposed
case4_error_by_period_path = f"../output/electric-consumption/case4/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
#######################################################################################################################
