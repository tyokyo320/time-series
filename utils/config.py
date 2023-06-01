import os

# Program root dir(do not modify)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

#######################################################################################################################
# test data file
test_data_path = '../data/test.csv'

# CSV predict results file path
predict_results_path = "../output/original/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
cell_synapases_history_path = '../output/original/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'

# param
nTrial = 10
epoch = 414915

#######################################################################################################################
# start and end index -> WARNING: start index must be 0 not 1
# first day
# start = 0
# end = 95
# last day
start = 414819
end = 414914
error_abs_start = start+epoch+1
error_abs_end = end+epoch+1

# start = 411937 # last 1 month
cell_synapases_start = 0

#######################################################################################################################
# Case 2: inf
inf_predict_results_path = "../output/infinity/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
inf_cell_synapases_history_path = '../output/infinity/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'

# Case 3: 10%
tenpercent_predict_results_path = "../output/tenpercent/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
tenpercent_cell_synapases_history_path = '../output/tenpercent/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'

# Case 4: first year as min and max
firstyear_predict_results_path = "../output/firstyear/InputOutput_BUon_BOon_NY15min_cells32_n421_r13d08.csv"
firstyear_cell_synapases_history_path = '../output/firstyear/CellSynapasesHistory_BUon_BOon_NY15min_cells32_n421_r13d08.csv'
