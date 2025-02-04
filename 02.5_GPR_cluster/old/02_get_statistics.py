import pandas as pd
import glob
import os

resultDir = f'trained_GPModels'
ratioDirs = glob.glob(os.path.join(resultDir, '*'))
#print(f'{ratioDirs}')

cwd = os.getcwd()
dfStatistics = pd.DataFrame({"ratio":[],
                             "index":[],
                             "dataset":[],
                             "time [hrs]":[],
                             "rmse":[],
                             "r2":[]})
#print(f'{dfStatistics}')

for ratioDir in ratioDirs:

  #print(f'{ratioDir}')
  try:
    thisRatio = float(os.path.basename(ratioDir))
  except:
    print(f'something went wrong with \'float(os.path.basename(ratioDir))\'. Exit.')
    exit()
  else:   
    #print(f'{thisRatio}')
    pass
    
  os.chdir(ratioDir)
  modelFiles = glob.glob(os.path.join(os.getcwd(),'trained_model*'))
  #print(f'{modelFiles}')  
  slurmFiles = glob.glob(os.path.join(os.getcwd(),'slurm-*'))
  #print(f'{slurmFiles}')
  numberOfRndInt = 1
  for slurmFile in slurmFiles:
    f = open(slurmFile, 'r')
    lines = f.readlines()
    f.close()
    #print(f'{slurmFile}')
    #print(f'{lines}')
    for i in range(0,len(lines)):
      if "time for Grid1296" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeGrid1296 = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid1296 = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeGrid1296}')
          pass
      elif "time for Grid2401" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeGrid2401 = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid2401 = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeGrid2401}')
          pass
      elif "time for Sobol1" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeSobol1 = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol1 = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeSobol1}')
          pass
      elif "time for Sobol2" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeSobol2 = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol2 = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeSobol2}')
          pass
        
      elif "Grid1296" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+2]}')
        #print(f'{lines[i+4]}')
        try:
          rmseGrid1296 = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid1296 = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{rmseGrid1296}')
          pass
          
        try:
          r2Grid1296 = float(lines[i+4].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid1296 = float(lines[i+4].split(\':\')[1])\'')
        else:
          #print(f'{r2Grid1296}')
          pass
      elif "Grid2401" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+2]}')
        #print(f'{lines[i+4]}')
        try:
          rmseGrid2401 = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid2401 = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{rmseGrid2401}')
          pass
          
        try:
          r2Grid2401 = float(lines[i+4].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid2401 = float(lines[i+4].split(\':\')[1])\'')
        else:
         # print(f'{r2Grid2401}')
          pass
      elif "Sobol1" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+2]}')
        #print(f'{lines[i+4]}')
        try:
          rmseSobol1 = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol1 = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{rmseSobol1}')
          pass
          
        try:
          r2Sobol1 = float(lines[i+4].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol1 = float(lines[i+4].split(\':\')[1])\'')
        else:
          #print(f'{r2Sobol1}')
          pass
      elif "Sobol2" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+2]}')
        #print(f'{lines[i+4]}')
        try:
          rmseSobol2 = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol2 = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{rmseSobol2}')
          pass
          
        try:
          r2Sobol2 = float(lines[i+4].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol2 = float(lines[i+4].split(\':\')[1])\'')
        else:
          #print(f'{r2Sobol2}')
          pass
          
    # fill data in dataframe
    try:
      newGrid1296Entry = pd.DataFrame({"ratio": [thisRatio], "index": [numberOfRndInt], "dataset": ['Grid1296'], "time [hrs]": [timeGrid1296], "rmse": [rmseGrid1296], "r2": [r2Grid1296]})
    except:
      print(f'something went wrong when assigning \'newGrid1296Entry\'')
    else:
      #print(f'{newGrid1296Entry}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid1296Entry], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid1296Entry\' twith \'dfStatistics\'.')
        
    try:
      newGrid2401Entry = pd.DataFrame({"ratio": [thisRatio], "index": [numberOfRndInt], "dataset": ['Grid2401'], "time [hrs]": [timeGrid2401], "rmse": [rmseGrid2401], "r2": [r2Grid2401]})
    except:
      print(f'something went wrong when assigning \'newGrid2401Entry\'')
    else:
      #print(f'{newGrid2401Entry}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid2401Entry], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid2401Entry\' twith \'dfStatistics\'.')
        
    try:
      newSobol1Entry = pd.DataFrame({"ratio": [thisRatio], "index": [numberOfRndInt], "dataset": ['Sobol1'], "time [hrs]": [timeSobol1], "rmse": [rmseSobol1], "r2": [r2Sobol1]})
    except:
      print(f'something went wrong when assigning \'newSobol1Entry\'')
    else:
      #print(f'{newSobol1Entry}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol1Entry], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol1Entry\' twith \'dfStatistics\'.')
        
    try:
      newSobol2Entry = pd.DataFrame({"ratio": [thisRatio], "index": [numberOfRndInt], "dataset": ['Sobol2'], "time [hrs]": [timeSobol2], "rmse": [rmseSobol2], "r2": [r2Sobol2]})
    except:
      print(f'something went wrong when assigning \'newSobol2Entry\'')
    else:
      #print(f'{newSobol2Entry}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol2Entry], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol2Entry\' twith \'dfStatistics\'.')
    
    #print(f'{dfStatistics}')      
    numberOfRndInt = numberOfRndInt + 1
    #break
  #print(f'{dfStatistics}')
  os.chdir(cwd)
  #break
  
statisticsFileName = 'StatisticsOfGPTraining.csv'
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
#print(f'{dfStatistics}')
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
