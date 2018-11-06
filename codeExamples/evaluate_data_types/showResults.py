import pandas as pd
import pickle

df = pickle.load( open( "m32_save_run_time.p", "rb" ) )

print df.drop('duration_var', axis=1).groupby(['data_type', 'optimization']).mean().unstack()

df = pickle.load( open( "m64_save_run_time.p", "rb" ) )

print df.drop('duration_var', axis=1).groupby(['data_type', 'optimization']).mean().unstack()
