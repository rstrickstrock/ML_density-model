import os
import glob
import pandas as pd
import numpy as np

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/maxR2"
thisDir = os.path.basename(pwd)
propTargetFile = os.path.join(pwd, f'{thisDir}-0', "energies", "bindir", "00_qm_opt", "target.txt")
#print(f'{propTargetFile}')
statisticsFileName = os.path.join(pwd, "StatsEnergies.csv")
avgRMSEFileName = os.path.join(pwd, "AvgRMSEEnergies.csv")

f = open(propTargetFile, "r")
lines = f.readlines()
f.close()
#print(f'{lines}')
dfTargets = pd.DataFrame({"target": []})
for line in lines:
  #print(f'{float(line)}')
  dfThisTarget = pd.DataFrame({"target": [float(line)]})
  dfTargets = pd.concat([dfTargets, dfThisTarget], ignore_index=True)
  
#print(f'{dfTargets}')
dfStats = dfTargets

optDirs = glob.glob(os.path.join(pwd, f'{thisDir}-*'))
#print(f'{optDirs}')

dfAvgRelRMSE = pd.DataFrame({"Avg. RMSE": []})

for optDir in optDirs:
  #print(f'{optDir}')
  optRun = os.path.basename(optDir).split("-")[1]
  #print(f'{optRun}')
  dfThisEnergies = pd.DataFrame({f'{thisDir}-{optRun}': []})
  
  ## get last optimization step
  energyPropDirs = glob.glob(os.path.join(optDir, "QMMM", "g.*"))
  #print(f'{energyPropDirs}')
  lastDir = 0
  for energyPropDir in energyPropDirs:
    #print(f'{energyPropDir}')
    iteration = int(os.path.basename(energyPropDir).split(".")[1])
    #print(f'{iteration}')
    if lastDir < iteration:
      lastDir = iteration
      #print(f'{lastDir}')
  lastDir = os.path.join(os.path.dirname(energyPropDir), f'g.{lastDir}.0')
  #print(f'{lastDir}')

  ## get optimized energies
  thisEnergiesFile = os.path.join(lastDir, "output", "Energy.rel.extrm.txt")
  #print(f'{thisEnergiesFile}')
  f = open(thisEnergiesFile, "r")
  lines = f.readlines()
  f.close()
  #print(f'{lines}')
  for line in lines:
    line = float(line.split(" ")[1])
    #print(f'{line}')
    dfThisEnergy = pd.DataFrame({f'{thisDir}-{optRun}': [line]})
    dfThisEnergies = pd.concat([dfThisEnergies, dfThisEnergy], ignore_index=True)
  #print(f'{dfThisEnergies}')
  dfStats = pd.concat([dfStats, dfThisEnergies], axis=1)
  #print(f'{dfStats}')
  
  ## calculate diff to targets
  dfThisAbsDiffs = pd.DataFrame({f'AbsDiffs-{optRun}': []})
  dfThisRelDiffs = pd.DataFrame({f'RelDiffs-{optRun}': []})
  avgRelRMSE = 0.0
  for i in range(0, len(dfTargets)):
    thisTarget = dfTargets.iloc[i][0]
    #print(f'{thisTarget}')
    thisEnergy = dfThisEnergies.iloc[i][0]
    #print(f'{thisEnergy}')
    thisAbsDiff = float(thisEnergy) - float(thisTarget)
    #print(f'{thisAbsDiff}')
    if int(thisTarget) == 0:
      thisRelDiff = 0
    else:
      thisRelDiff = thisAbsDiff/thisTarget 
    #print(f'{thisRelDiff}')
    avgRelRMSE = avgRelRMSE + np.sqrt(thisRelDiff*thisRelDiff)
    dfThisAbsDiff = pd.DataFrame({f'AbsDiffs-{optRun}': [thisAbsDiff]})
    #print(f'{dfThisAbsDiff}')
    dfThisRelDiff = pd.DataFrame({f'RelDiffs-{optRun}': [thisRelDiff]})
    #print(f'{dfThisRelDiff}')
    dfThisAbsDiffs = pd.concat([dfThisAbsDiffs, dfThisAbsDiff], ignore_index=True)
    dfThisRelDiffs = pd.concat([dfThisRelDiffs, dfThisRelDiff], ignore_index=True)
  #print(f'{dfThisAbsDiffs}')
  #print(f'{dfThisRelDiffs}')
  dfStats = pd.concat([dfStats, dfThisAbsDiffs, dfThisRelDiffs], axis=1)
  #print(f'{dfStats}')
  avgRelRMSE = avgRelRMSE/len(dfTargets)
  dfThisAvgRelRMSE = pd.DataFrame({"Avg. RMSE": [avgRelRMSE]})
  dfAvgRelRMSE = pd.concat([dfAvgRelRMSE, dfThisAvgRelRMSE], ignore_index=True)
  #print(f'{avgRelRMSE}')
#print(f'{dfStats}')
#print(f'{dfAvgRelRMSE}')

if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStats.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStats}')

if os.path.exists(avgRMSEFileName):
  os.remove(avgRMSEFileName)
  print(f'Removed existing statistics file: \'{avgRMSEFileName}\'.')
dfAvgRelRMSE.to_csv(avgRMSEFileName)
print(f'Wrote statistics to file: \'{avgRMSEFileName}\'.')
print(f'{dfAvgRelRMSE}')






















