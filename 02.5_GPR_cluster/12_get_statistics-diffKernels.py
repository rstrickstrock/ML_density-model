import pandas as pd
import glob
import os

resultDir = f'diffKernels_trained_GPModels'
ratioDirs = glob.glob(os.path.join(resultDir, '*'))
#print(f'{ratioDirs}')

cwd = os.getcwd()
dfStatistics = pd.DataFrame({"ratio":[],
                             "rndint":[],
                             "dataset":[],
                             "kernel":[],
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
  #modelFiles = glob.glob(os.path.join(os.getcwd(),'trained_model*'))
  #print(f'{modelFiles}')  
  slurmFiles = glob.glob(os.path.join(os.getcwd(),'slurm-*'))
  #print(f'{slurmFiles}')
  for slurmFile in slurmFiles:
    f = open(slurmFile, 'r')
    lines = f.readlines()
    f.close()
    #print(f'{slurmFile}')
    #print(f'{lines}')
    for i in range(0,len(lines)):
      if "Training Models for Ratio" in lines[i]:
        try:
          thisRndInt = int(lines[i].split(',')[1].split(':')[1])
        except:
          print(f'something went wrong with \'thisRndInt = int(x.split(\',\')[1].split(\':\')[1])\'')
        else:
          #print(f'{thisRndInt}')
          pass
      elif "time for Grid1296, RBF" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeGrid1296RBF = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid1296RBF = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeGrid1296RBF}')
          pass
      elif "time for Grid1296, Matern" in lines[i]:
        try:
          timeGrid1296Matern = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid1296Matern = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Grid1296, RQ" in lines[i]:
        try:
          timeGrid1296RQ = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid1296RQ = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Grid1296, ESS" in lines[i]:
        try:
          timeGrid1296ESS = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid1296ESS = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Grid2401, RBF" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeGrid2401RBF = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid2401RBF = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeGrid2401RBF}')
          pass
      elif "time for Grid2401, Matern" in lines[i]:
        try:
          timeGrid2401Matern = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid2401Matern = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Grid2401, RQ" in lines[i]:
        try:
          timeGrid2401RQ = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid2401RQ = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Grid2401, ESS" in lines[i]:
        try:
          timeGrid2401ESS = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeGrid2401ESS = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Sobol1, RBF" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeSobol1RBF = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol1RBF = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeSobol1RBF}')
          pass
      elif "time for Sobol1, Matern" in lines[i]:
        try:
          timeSobol1Matern = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol1Matern = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Sobol1, RQ" in lines[i]:
        try:
          timeSobol1RQ = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol1RQ = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Sobol1, ESS" in lines[i]:
        try:
          timeSobol1ESS = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol1ESS = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Sobol2, RBF" in lines[i]:
        #print(f'{lines[i]}')
        try:
          timeSobol2RBF = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol2RBF = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          #print(f'{timeSobol2RBF}')
          pass
      elif "time for Sobol2, Matern" in lines[i]:
        try:
          timeSobol2Matern = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol2Matern = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Sobol2, RQ" in lines[i]:
        try:
          timeSobol2RQ = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol2RQ = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
      elif "time for Sobol2, ESS" in lines[i]:
        try:
          timeSobol2ESS = float(lines[i].split(':')[1].split('hrs')[0])
        except:
          print(f'something went wrong with \'timeSobol2ESS = float(lines[i].split(\':\')[1].split(\'hrs\')[0])\'')
        else:
          pass
        
      elif "Grid1296, RBF" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+1]}')
        #print(f'{lines[i+2]}')
        try:
          rmseGrid1296RBF = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid1296RBF = float(lines[i+1].split(\':\')[1])\'')
        else:
          #print(f'{rmseGrid1296RBF}')
          pass     
        try:
          r2Grid1296RBF = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid1296RBF = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{r2Grid1296RBF}')
          pass
      elif "Grid1296, Matern" in lines[i] and not "time for" in lines[i]:
        try:
          rmseGrid1296Matern = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid1296Matern = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Grid1296Matern = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid1296Matern = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Grid1296, RQ" in lines[i] and not "time for" in lines[i]:
        try:
          rmseGrid1296RQ = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid1296RQ = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Grid1296RQ = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid1296RQ = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Grid1296, ESS" in lines[i] and not "time for" in lines[i]:
        try:
          rmseGrid1296ESS = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid1296ESS = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Grid1296ESS = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid1296ESS = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Grid2401, RBF" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+1]}')
        #print(f'{lines[i+2]}')
        try:
          rmseGrid2401RBF = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid2401RBF = float(lines[i+1].split(\':\')[1])\'')
        else:
          #print(f'{rmseGrid2401RBF}')
          pass     
        try:
          r2Grid2401RBF = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid2401RBF = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{r2Grid2401RBF}')
          pass
      elif "Grid2401, Matern" in lines[i] and not "time for" in lines[i]:
        try:
          rmseGrid2401Matern = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid2401Matern = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Grid2401Matern = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid2401Matern = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Grid2401, RQ" in lines[i] and not "time for" in lines[i]:
        try:
          rmseGrid2401RQ = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid2401RQ = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Grid2401RQ = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid2401RQ = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Grid2401, ESS" in lines[i] and not "time for" in lines[i]:
        try:
          rmseGrid2401ESS = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseGrid2401ESS = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Grid2401ESS = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Grid2401ESS = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Sobol1, RBF" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+1]}')
        #print(f'{lines[i+2]}')
        try:
          rmseSobol1RBF = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol1RBF = float(lines[i+1].split(\':\')[1])\'')
        else:
          #print(f'{rmseSobol1RBF}')
          pass     
        try:
          r2Sobol1RBF = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol1RBF = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{r2Sobol1RBF}')
          pass
      elif "Sobol1, Matern" in lines[i] and not "time for" in lines[i]:
        try:
          rmseSobol1Matern = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol1Matern = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Sobol1Matern = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol1Matern = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Sobol1, RQ" in lines[i] and not "time for" in lines[i]:
        try:
          rmseSobol1RQ = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol1RQ = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Sobol1RQ = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol1RQ = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Sobol1, ESS" in lines[i] and not "time for" in lines[i]:
        try:
          rmseSobol1ESS = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol1ESS = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Sobol1ESS = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol1ESS = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Sobol2, RBF" in lines[i] and not "time for" in lines[i]:
        #print(f'{lines[i+1]}')
        #print(f'{lines[i+2]}')
        try:
          rmseSobol2RBF = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol2RBF = float(lines[i+1].split(\':\')[1])\'')
        else:
          #print(f'{rmseSobol2RBF}')
          pass     
        try:
          r2Sobol2RBF = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol2RBF = float(lines[i+2].split(\':\')[1])\'')
        else:
          #print(f'{r2Sobol2RBF}')
          pass
      elif "Sobol2, Matern" in lines[i] and not "time for" in lines[i]:
        try:
          rmseSobol2Matern = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol2Matern = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Sobol2Matern = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol2Matern = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Sobol2, RQ" in lines[i] and not "time for" in lines[i]:
        try:
          rmseSobol2RQ = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol2RQ = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Sobol2RQ = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol2RQ = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
      elif "Sobol2, ESS" in lines[i] and not "time for" in lines[i]:
        try:
          rmseSobol2ESS = float(lines[i+1].split(':')[1])
        except:
          print(f'something went wrong with \'rmseSobol2ESS = float(lines[i+1].split(\':\')[1])\'')
        else:
          pass     
        try:
          r2Sobol2ESS = float(lines[i+2].split(':')[1])
        except:
          print(f'something went wrong with \'r2Sobol2ESS = float(lines[i+2].split(\':\')[1])\'')
        else:
          pass
          
    # fill data in dataframe
    try:
      newGrid1296EntryRBF = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid1296'], "kernel": ['RBF'], "time [hrs]": [timeGrid1296RBF], "rmse": [rmseGrid1296RBF], "r2": [r2Grid1296RBF]})
    except:
      print(f'something went wrong when assigning \'newGrid1296EntryRBF\'')
    else:
      #print(f'{newGrid1296EntryRBF}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid1296EntryRBF], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid1296EntryRBF\' twith \'dfStatistics\'.')
    try:
      newGrid1296EntryMatern = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid1296'], "kernel": ['Matern'], "time [hrs]": [timeGrid1296Matern], "rmse": [rmseGrid1296Matern], "r2": [r2Grid1296Matern]})
    except:
      print(f'something went wrong when assigning \'newGrid1296EntryMatern\'')
    else:
      #print(f'{newGrid1296EntryMatern}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid1296EntryMatern], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid1296EntryMatern\' twith \'dfStatistics\'.')
    try:
      newGrid1296EntryRQ = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid1296'], "kernel": ['RQ'], "time [hrs]": [timeGrid1296RQ], "rmse": [rmseGrid1296RQ], "r2": [r2Grid1296RQ]})
    except:
      print(f'something went wrong when assigning \'newGrid1296EntryRQ\'')
    else:
      #print(f'{newGrid1296EntryRQ}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid1296EntryRQ], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid1296EntryRQ\' twith \'dfStatistics\'.')
    try:
      newGrid1296EntryESS = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid1296'], "kernel": ['ESS'], "time [hrs]": [timeGrid1296ESS], "rmse": [rmseGrid1296ESS], "r2": [r2Grid1296ESS]})
    except:
      print(f'something went wrong when assigning \'newGrid1296EntryESS\'')
    else:
      #print(f'{newGrid1296EntryESS}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid1296EntryESS], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid1296EntryESS\' twith \'dfStatistics\'.')
    
    try:
      newGrid2401EntryRBF = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid2401'], "kernel": ['RBF'], "time [hrs]": [timeGrid2401RBF], "rmse": [rmseGrid2401RBF], "r2": [r2Grid2401RBF]})
    except:
      print(f'something went wrong when assigning \'newGrid2401EntryRBF\'')
    else:
      #print(f'{newGrid2401EntryRBF}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid2401EntryRBF], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid2401EntryRBF\' twith \'dfStatistics\'.')
    try:
      newGrid2401EntryMatern = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid2401'], "kernel": ['Matern'], "time [hrs]": [timeGrid2401Matern], "rmse": [rmseGrid2401Matern], "r2": [r2Grid2401Matern]})
    except:
      print(f'something went wrong when assigning \'newGrid2401EntryMatern\'')
    else:
      #print(f'{newGrid2401EntryMatern}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid2401EntryMatern], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid2401EntryMatern\' twith \'dfStatistics\'.')
    try:
      newGrid2401EntryRQ = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid2401'], "kernel": ['RQ'], "time [hrs]": [timeGrid2401RQ], "rmse": [rmseGrid2401RQ], "r2": [r2Grid2401RQ]})
    except:
      print(f'something went wrong when assigning \'newGrid2401EntryRQ\'')
    else:
      #print(f'{newGrid2401EntryRQ}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid2401EntryRQ], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid2401EntryRQ\' twith \'dfStatistics\'.')
    try:
      newGrid2401EntryESS = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Grid2401'], "kernel": ['ESS'], "time [hrs]": [timeGrid2401ESS], "rmse": [rmseGrid2401ESS], "r2": [r2Grid2401ESS]})
    except:
      print(f'something went wrong when assigning \'newGrid2401EntryESS\'')
    else:
      #print(f'{newGrid2401EntryESS}')
      try:
        dfStatistics = pd.concat([dfStatistics, newGrid2401EntryESS], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newGrid2401EntryESS\' twith \'dfStatistics\'.')
    
    try:
      newSobol1EntryRBF = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol1'], "kernel": ['RBF'], "time [hrs]": [timeSobol1RBF], "rmse": [rmseSobol1RBF], "r2": [r2Sobol1RBF]})
    except:
      print(f'something went wrong when assigning \'newSobol1EntryRBF\'')
    else:
      #print(f'{newSobol1EntryRBF}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol1EntryRBF], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol1EntryRBF\' twith \'dfStatistics\'.')
    try:
      newSobol1EntryMatern = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol1'], "kernel": ['Matern'], "time [hrs]": [timeSobol1Matern], "rmse": [rmseSobol1Matern], "r2": [r2Sobol1Matern]})
    except:
      print(f'something went wrong when assigning \'newSobol1EntryMatern\'')
    else:
      #print(f'{newSobol1EntryMatern}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol1EntryMatern], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol1EntryMatern\' twith \'dfStatistics\'.')
    try:
      newSobol1EntryRQ = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol1'], "kernel": ['RQ'], "time [hrs]": [timeSobol1RQ], "rmse": [rmseSobol1RQ], "r2": [r2Sobol1RQ]})
    except:
      print(f'something went wrong when assigning \'newSobol1EntryRQ\'')
    else:
      #print(f'{newSobol1EntryRQ}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol1EntryRQ], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol1EntryRQ\' twith \'dfStatistics\'.')
    try:
      newSobol1EntryESS = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol1'], "kernel": ['ESS'], "time [hrs]": [timeSobol1ESS], "rmse": [rmseSobol1ESS], "r2": [r2Sobol1ESS]})
    except:
      print(f'something went wrong when assigning \'newSobol1EntryESS\'')
    else:
      #print(f'{newSobol1EntryESS}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol1EntryESS], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol1EntryESS\' twith \'dfStatistics\'.')
    
    try:
      newSobol2EntryRBF = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol2'], "kernel": ['RBF'], "time [hrs]": [timeSobol2RBF], "rmse": [rmseSobol2RBF], "r2": [r2Sobol2RBF]})
    except:
      print(f'something went wrong when assigning \'newSobol2EntryRBF\'')
    else:
      #print(f'{newSobol2EntryRBF}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol2EntryRBF], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol2EntryRBF\' twith \'dfStatistics\'.')
    try:
      newSobol2EntryMatern = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol2'], "kernel": ['Matern'], "time [hrs]": [timeSobol2Matern], "rmse": [rmseSobol2Matern], "r2": [r2Sobol2Matern]})
    except:
      print(f'something went wrong when assigning \'newSobol2EntryMatern\'')
    else:
      #print(f'{newSobol2EntryMatern}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol2EntryMatern], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol2EntryMatern\' twith \'dfStatistics\'.')
    try:
      newSobol2EntryRQ = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol2'], "kernel": ['RQ'], "time [hrs]": [timeSobol2RQ], "rmse": [rmseSobol2RQ], "r2": [r2Sobol2RQ]})
    except:
      print(f'something went wrong when assigning \'newSobol2EntryRQ\'')
    else:
      #print(f'{newSobol2EntryRQ}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol2EntryRQ], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol2EntryRQ\' twith \'dfStatistics\'.')
    try:
      newSobol2EntryESS = pd.DataFrame({"ratio": [thisRatio], "rndint": [thisRndInt], "dataset": ['Sobol2'], "kernel": ['ESS'], "time [hrs]": [timeSobol2ESS], "rmse": [rmseSobol2ESS], "r2": [r2Sobol2ESS]})
    except:
      print(f'something went wrong when assigning \'newSobol2EntryESS\'')
    else:
      #print(f'{newSobol2EntryESS}')
      try:
        dfStatistics = pd.concat([dfStatistics, newSobol2EntryESS], ignore_index=True)
      except:
        print(f'something went wrong when concating \'newSobol2EntryESS\' twith \'dfStatistics\'.')
    
    #print(f'{dfStatistics}')      
    #break
  #print(f'{dfStatistics}')
  os.chdir(cwd)
  #break
  
statisticsFileName = 'StatisticsOfGPTrainingDiffKernels.csv'
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStatistics}')
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
