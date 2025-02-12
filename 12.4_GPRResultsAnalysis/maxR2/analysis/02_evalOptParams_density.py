import pandas as pd
import os
import glob
import shutil
import subprocess

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/maxR2"



evalSimDir = os.path.join(pwd, "evalOptParams_DensitySims")
if os.path.exists(evalSimDir):
  shutil.rmtree(evalSimDir)
os.mkdir(evalSimDir)

statsFile = os.path.join(pwd, "StatsDensity.csv")
stats = pd.read_csv(statsFile)
stats = stats.drop(stats.columns[0], axis=1)
#print(f'{stats}')
#print(f'{len(stats)}')
for i in range(0, len(stats)):
  #print(f'{stats.iloc[i]}')
  thisNumber = int(stats.iloc[i]["#"])
  #print(f'{thisNumber}')
  thisSimDir = os.path.join(evalSimDir, f'run-{thisNumber}/')
  #print(f'{thisSimDir}')
  
  thisSigC = stats.iloc[i]["SigC"]
  #print(f'{thisSigC}')
  thisSigH = stats.iloc[i]["SigH"]
  #print(f'{thisSigH}')
  thisEpsC = stats.iloc[i]["EpsC"]
  #print(f'{thisEpsC}')
  thisEpsH = stats.iloc[i]["EpsH"]
  #print(f'{thisEpsH}')
  
  thisCommand = f'sh {os.path.join(os.getcwd(), "02_density", "physprop_setup.sh")} {thisSimDir} {thisSigC} {thisSigH} {thisEpsC} {thisEpsH}'
  #print(f'{thisCommand}')
  p = subprocess.Popen(thisCommand, stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()
  #print(f'test')
  p_status = p.wait()
  #print(f'Command output: {output}')

