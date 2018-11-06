import subprocess
import numpy as np
import copy
import pandas as pd
import pickle

optimization_levels = ['-O0 ', '-O1', '-O2', '-O3', '-Os']
data_types =['uint_fast16_t', 'uint16_t', 'uint32_t', 'unsigned short', 'unsigned int', 'unsigned long']
output = []

for data_type in data_types:

    result_sample = {}
    result_sample['data_type'] = data_type

    print data_type
    print "----------------------------------------------------"

    with open('datatypeEvaluation.c', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('<type>', data_type)

    # Write the file out again
    with open('datatypeEvaluation_gen.c', 'w') as file:
        file.write(filedata)


    for optimization in optimization_levels:

        result_sample['optimization'] = optimization

        compiler_options = 'gcc -Wpedantic ' + optimization + \
                        ' datatypeEvaluation_gen.c' + ' -o program.out'

        print compiler_options

        compilation_return = subprocess.check_output(compiler_options, shell=True)

        durations = np.zeros(20, dtype=float)

        for i in range(0,len(durations)):
            time_return = subprocess.check_output(["time", "./program.out"], stderr=subprocess.STDOUT)

            # erwartete Rueckgabe
            #1024
            #1.64user 0.00system 0:01.64elapsed 99%CPU (0avgtext+0avgdata 1376maxresident)k

            durations[i] =  float(time_return.split('user')[0].split('\n')[1])

        print durations.mean()
        result_sample['duration_mean'] = durations.mean()
        result_sample['duration_var'] = durations.var()

        output.append(copy.copy(result_sample))

df = pd.DataFrame(output)
pickle.dump( df, open( "save_run_time.p", "wb" ) )

print df.drop('duration_var', axis=1).groupby(['data_type', 'optimization']).mean().unstack()
