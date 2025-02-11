import pandas as pd
import os
import glob

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/minMAPE"

optDirs = glob.glob(os.path.join(pwd, "minMAPE-*"))
#print(f'{optDirs}')


for optDir in optDirs:
  #print(f'{optDir}')
  optRun = os.path.basename(optDir).split("-")[1]
  #print(f'{optRun}')
  statisticsFileName = os.path.join(pwd, f'OptPath-{optRun}.csv')
  #print(f'{statisticsFileName}')
  
  dfStatistics = pd.DataFrame({"iteration": [],
                               "SigC": [],
                               "SigH": [],
                               "EpsC": [],
                               "EpsH": [],
                               "prediction": []})
  
  
  physPropDirs = glob.glob(os.path.join(optDir, "PhysProp", "g.*"))
  #print(f'{physPropDirs}')

  for physPropDir in physPropDirs:
    #print(f'{physPropDir}')
    iteration = int(os.path.basename(physPropDir).split(".")[2])
    #print(f'{iteration}')
    if iteration == 0:
      #print(f'{physPropDir}')
      thisParameterFile = os.path.join(physPropDir, "this_parameters.csv")
      #print(f'{thisParameterFile}')
      thisPredictionFile = os.path.join(physPropDir, "this_prediction.csv")
      #print(f'{thisPredictionFile}')
      thisIteration = int(os.path.basename(physPropDir).split(".")[1])
      #print(f'{thisIteration}')
      
      thisParameters = pd.read_csv(thisParameterFile)
      #print(f'{thisParameters}')
  
      thisPrediction = pd.read_csv(thisPredictionFile)
      thisPrediction = thisPrediction.drop(thisPrediction.columns[0], axis=1)
      #print(f'{thisPrediction}')
  
      thisStats = pd.DataFrame({"iteration": [thisIteration],
                                "SigC": [thisParameters["SigC"].to_numpy()[0]],
                                "SigH": [thisParameters["SigH"].to_numpy()[0]],
                                "EpsC": [thisParameters["EpsC"].to_numpy()[0]],
                                "EpsH": [thisParameters["EpsH"].to_numpy()[0]],
                                "prediction": [thisPrediction["prediction"].to_numpy()[0]]})
      #print(f'{thisStats}')
      dfStatistics = pd.concat([dfStatistics, thisStats], ignore_index=True)

  #print(f'{dfStatistics}')
  if os.path.exists(statisticsFileName):
    os.remove(statisticsFileName)
    print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
  dfStatistics.to_csv(statisticsFileName)
  print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
  print(f'{dfStatistics}')
