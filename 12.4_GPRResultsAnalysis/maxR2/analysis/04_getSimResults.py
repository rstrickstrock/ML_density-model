import os
import glob
import pandas as pd

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/maxR2"
propTarget = 700.0



statisticsFileName = os.path.join(pwd, "Stats_withSimResults.csv")

simDirs = glob.glob(os.path.join(pwd, "evalOptParams_sims", "run-*"))
#print(f'{simDirs}')

dfSimResults = pd.DataFrame({"#": [],
                             "simulation": [],
                             "simErr": []})

for simDir in simDirs:
  #print(f'{simDir}')
  thisIndex = int(os.path.basename(simDir).split("-")[1])
  #print(f'{thisIndex}')
  
  slurmFiles = glob.glob(os.path.join(simDir, "slurm-*"))
  lastSlurmFileID = None
  lastSlurmFile = None
  for slurmFile in slurmFiles:
    #print(f'{slurmFile}')
    thisSlurmFileID = int(os.path.basename(slurmFile).split(".")[0].split("-")[1])
    #print(f'{thisSlurmFileID}')
    if lastSlurmFile is None:
      lastSlurmFileID = thisSlurmFileID
      lastSlurmFile = slurmFile
    elif lastSlurmFileID < thisSlurmFileID:
      lastSlurmFileID = thisSlurmFileID
      lastSlurmFile = slurmFile
  #print(f'lastSlurmFile: {lastSlurmFile}')
  
  f = open(lastSlurmFile, "r")
  lines = f.readlines()
  f.close()
  
  for line in lines:
    if line.startswith("Density"):
      #print(f'{line}')
      line = line.split(" ")
      #print(f'{line}')
      thisLine = []
      for item in line:
        if len(item) > 1:
          thisLine.append(item)
      density = thisLine[1]
      err = thisLine[2]
      #print(f'density: {density}')
      #print(f'err: {err}')
      break
  dfThisResult = pd.DataFrame({"#": [thisIndex],
                               "simulation": [density],
                               "simErr": [err]})
  dfSimResults = pd.concat([dfSimResults, dfThisResult], ignore_index=True)

#print(f'{dfSimResults}')

statsFile = os.path.join(pwd, "Stats.csv")
stats = pd.read_csv(statsFile)
stats = stats.drop(stats.columns[0], axis=1)
#print(f'{stats}')
dfSimResults = dfSimResults.drop(dfSimResults.columns[0], axis=1)
#print(f'{dfSimResults}')

stats = pd.concat([stats, dfSimResults], axis=1)
#print(f'{stats}')

dfDiff = pd.DataFrame({"absPredSimDiff": [],
                       "relPredSimDiff": [],
                       "absTargSimDiff": [],
                       "relTargSimDiff": []})

for i in range(0, len(stats)):
  thisPred = float(stats.iloc[i]["prediction"])
  #print(f'thisPred: {thisPred}')
  thisSim = float(stats.iloc[i]["simulation"])
  #print(f'thisSim: {thisSim}')
  thisAbsPredSimDiff = thisPred - thisSim
  #print(f'abs diff: {thisAbsPredSimDiff}')
  thisRelPredSimDiff = thisAbsPredSimDiff/thisSim
  #print(f'rel diff: {thisRelPredSimDiff}')
  thisAbsTargSimDiff = thisSim - propTarget
  thisRelTargSimDiff = thisAbsTargSimDiff/propTarget
  
  dfThisDiff = pd.DataFrame({"absPredSimDiff": [thisAbsPredSimDiff],
                             "relPredSimDiff": [thisRelPredSimDiff],
                             "absTargSimDiff": [thisAbsTargSimDiff],
                             "relTargSimDiff": [thisRelTargSimDiff]})
  dfDiff = pd.concat([dfDiff, dfThisDiff], ignore_index=True)
  
#print(f'{dfDiff}')

stats = pd.concat([stats, dfDiff], axis=1)
#print(f'{stats}')

if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
stats.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{stats}')


























