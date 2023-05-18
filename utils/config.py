import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# CSV predict results file path
predict_results_path = "../output/original/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"

# param
nTrial = 10
epoch = 414915

# start and end index
start = 414819  # last day
error_abs_end = epoch * 2
error_abs_start = error_abs_end - 24*4
# start = 411937 # last 1 month

# inf
predict_inf_results_path = "../output/infinity/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08_infinity.csv"

# 100
predict_100_results_path = "../output/100/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08_100.csv"
