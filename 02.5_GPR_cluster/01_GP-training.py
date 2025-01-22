import os
import shutil
import pandas as pd

testmode = True
random_ints = [678, 147, 561, 237, 588, 951, 490, 395, 877, 297, 721, 711, 985, 171, 75, 16, 669, 530, 999, 794, 936, 111, 816, 968, 48, 986, 829, 996, 272, 759, 390, 930, 633, 928, 854, 554, 562, 78, 222, 294, 725, 582, 731, 249, 791, 35, 180, 510, 593, 634]

testsizes = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

cwd = os.getcwd()
datasetfiles = [os.path.join(cwd, 'CLEANED_gridsearch_1296.csv'), os.path.join(cwd, 'CLEANED_gridsearch_2401.csv'), os.path.join(cwd, 'CLEANED_sobolsampling-2048.csv'), os.path.join(cwd, 'CLEANED_sobolsampling-2048-2.csv')]

### create current working directory ###
cwd = os.path.join(cwd, "trained_GPModels")
#print(f'{cwd}')
if os.path.exists(cwd):
  if testmode:
    shutil.rmtree(cwd)
  else:
    print(f'\nPATH \'{cwd}\' already exists. \n\nExiting without starting or changing anything.\n')
    exit()

os.mkdir(cwd)


### read datasets ###
## grid sampling 1296
data1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
data1296 = data1296.drop(data1296.columns[0], axis=1)
X_1296 = data1296.drop('density', axis=1)
Y_1296 = data1296['density']
## grid sampling 2401
data2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
data2401 = data2401.drop(data2401.columns[0], axis=1)
X_2401 = data2401.drop('density', axis=1)
Y_2401 = data2401['density']
## sobol2 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']
## sobol2 sampling
data_sobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
data_sobol2 = data_sobol2.drop(data_sobol2.columns[0], axis=1)
X_sobol2 = data_sobol2.drop('density', axis=1)
Y_sobol2 = data_sobol2['density']


def create_batch_file(tmp_cwd, rnd_int, ratio, thisPythonFile):
  fileName = f'batch_start_training_{rnd_int}.sh'
  batchFile = os.path.join(tmp_cwd, fileName)
  
  if os.path.exists(batchFile):
    os.remove(batchFile)
  
  f = open(batchFile, 'w')
  f.write(f'#!/bin/bash\n')
  f.write(f'#SBATCH --partition=hpc,hpc1,hpc3\n')
  f.write(f'#SBATCH --nodes=1\n')
  f.write(f'#SBATCH --mem 10G\n')
  f.write(f'#SBATCH --time=15:00:00\n')
  f.write(f'#SBATCH --job-name={ratio}-{rnd_int}\n')
  f.write(f'\n')
  f.write(f'python {thisPythonFile}\n')
  f.close()
  
  return os.path.basename(batchFile)


def copy_datasetfiles(tmp_cwd, datasetfiles):
  tmp_datasetfiles = []
  for datasetfile in datasetfiles:
    tmp_datasetfile = os.path.join(tmp_cwd, os.path.basename(datasetfile))
    #print(f'{tmp_datasetfile}')
    if os.path.exists(tmp_datasetfile):
      os.remove(tmp_datasetfile)
    shutil.copy(datasetfile, tmp_datasetfile)
    tmp_datasetfiles.append(os.path.basename(tmp_datasetfile))

  return tmp_datasetfiles


def create_python_file(tmp_cwd, rnd_int, ratio, tmp_datasetfiles):
  fileName = f'train_{ratio}_{rnd_int}.py'
  thisPythonFile = os.path.join(tmp_cwd, fileName)
  
  if os.path.exists(thisPythonFile):
    os.remove(thisPythonFile)
  
  f = open(thisPythonFile, 'w')
  f.write(f'### imports ###\n')
  f.write(f'from sklearn.gaussian_process import GaussianProcessRegressor\n')
  f.write(f'from sklearn.gaussian_process.kernels import RBF\n')
  f.write(f'from sklearn.model_selection import train_test_split\n')
  f.write(f'from sklearn.metrics import mean_squared_error, r2_score\n')
  f.write(f'import pandas as pd\n')
  f.write(f'import numpy as np\n')
  f.write(f'from scipy import stats\n')
  f.write(f'from matplotlib import pyplot as plt\n')
  f.write(f'import time\n')
  f.write(f'import pickle\n')
  f.write(f'\n')
  f.write(f'\n')
  f.write(f'### read datasets ###\n')
  f.write(f'data1296 = pd.read_csv(\'CLEANED_gridsearch_1296.csv\')\n')
  f.write(f'data1296 = data1296.drop(data1296.columns[0], axis=1)\n')
  f.write(f'X_1296 = data1296.drop(\'density\', axis=1)\n')
  f.write(f'Y_1296 = data1296[\'density\']\n')
  f.write(f'\n')
  f.write(f'data2401 = pd.read_csv(\'CLEANED_gridsearch_2401.csv\')\n')
  f.write(f'data2401 = data2401.drop(data2401.columns[0], axis=1)\n')
  f.write(f'X_2401 = data2401.drop(\'density\', axis=1)\n')
  f.write(f'Y_2401 = data2401[\'density\']\n')
  f.write(f'\n')
  f.write(f'dataSobol1 = pd.read_csv(\'CLEANED_sobolsampling-2048.csv\')\n')
  f.write(f'dataSobol1 = dataSobol1.drop(dataSobol1.columns[0], axis=1)\n')
  f.write(f'X_Sobol1 = dataSobol1.drop(\'density\', axis=1)\n')
  f.write(f'Y_Sobol1 = dataSobol1[\'density\']\n')
  f.write(f'\n')
  f.write(f'dataSobol2 = pd.read_csv(\'CLEANED_sobolsampling-2048-2.csv\')\n')
  f.write(f'dataSobol2 = dataSobol2.drop(dataSobol2.columns[0], axis=1)\n')
  f.write(f'X_Sobol2 = dataSobol2.drop(\'density\', axis=1)\n')
  f.write(f'Y_Sobol2 = dataSobol2[\'density\']\n')
  f.write(f'\n')
  f.write(f'\n')
  f.write(f'### prepare training and testdata ###\n')
  f.write(f'X_train_1296, X_test_1296, Y_train_1296, Y_test_1296 = train_test_split(X_1296, Y_1296, test_size={ratio}, random_state={rnd_int})\n')
  f.write(f'X_test_1296 = pd.concat([X_test_1296, X_2401, X_Sobol1, X_Sobol2], ignore_index=True)\n')
  f.write(f'Y_test_1296 = pd.concat([Y_test_1296, Y_2401, Y_Sobol1, Y_Sobol2], ignore_index=True)\n')
  f.write(f'\n')
  f.write(f'X_train_2401, X_test_2401, Y_train_2401, Y_test_2401 = train_test_split(X_2401, Y_2401, test_size={ratio}, random_state={rnd_int})\n')
  f.write(f'X_test_2401 = pd.concat([X_test_2401, X_1296, X_Sobol1, X_Sobol2], ignore_index=True)\n')
  f.write(f'Y_test_2401 = pd.concat([Y_test_2401, Y_1296, Y_Sobol1, Y_Sobol2], ignore_index=True)\n')
  f.write(f'\n')
  f.write(f'X_train_Sobol1, X_test_Sobol1, Y_train_Sobol1, Y_test_Sobol1 = train_test_split(X_Sobol1, Y_Sobol1, test_size={ratio}, random_state={rnd_int})\n')
  f.write(f'X_test_Sobol1 = pd.concat([X_test_Sobol1, X_1296, X_2401, X_Sobol2], ignore_index=True)\n')
  f.write(f'Y_test_Sobol1 = pd.concat([Y_test_Sobol1, Y_1296, Y_2401, Y_Sobol2], ignore_index=True)\n')
  f.write(f'\n')
  f.write(f'X_train_Sobol2, X_test_Sobol2, Y_train_Sobol2, Y_test_Sobol2 = train_test_split(X_Sobol2, Y_Sobol2, test_size={ratio}, random_state={rnd_int})\n')
  f.write(f'X_test_Sobol2 = pd.concat([X_test_Sobol2, X_1296, X_2401, X_Sobol1], ignore_index=True)\n')
  f.write(f'Y_test_Sobol2 = pd.concat([Y_test_Sobol2, Y_1296, Y_2401, Y_Sobol1], ignore_index=True)\n')
  f.write(f'\n')
  f.write(f'\n')
  f.write(f'### train models ###\n')
  f.write(f'n_restarts = 9\n')
  f.write(f'kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))\n')
  f.write(f'model1296 = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=n_restarts, random_state={rnd_int})\n')
  f.write(f't1_1296 = time.time()\n')
  f.write(f'model1296.fit(X_train_1296, Y_train_1296)\n')
  f.write(f'dt_1296 = time.time() - t1_1296\n')
  f.write(f'print(f\'time for Grid1296: ')
  f.write('{dt_1296')
  f.write('/3600}hrs\')\n')
  f.write(f'\n')
  f.write(f'kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))\n')
  f.write(f'model2401 = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=n_restarts, random_state={rnd_int})\n')
  f.write(f't1_2401 = time.time()\n')
  f.write(f'model2401.fit(X_train_2401, Y_train_2401)\n')
  f.write(f'dt_2401 = time.time() - t1_2401\n')
  f.write(f'print(f\'time for Grid2401: ')
  f.write('{dt_2401')
  f.write('/3600}hrs\')\n')
  f.write(f'\n')
  f.write(f'kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))\n')
  f.write(f'modelSobol1 = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=n_restarts, random_state={rnd_int})\n')
  f.write(f't1_Sobol1 = time.time()\n')
  f.write(f'modelSobol1.fit(X_train_Sobol1, Y_train_Sobol1)\n')
  f.write(f'dt_Sobol1 = time.time() - t1_Sobol1\n')
  f.write(f'print(f\'time for Sobol1: ')
  f.write('{dt_Sobol1')
  f.write('/3600}hrs\')\n')
  f.write(f'\n')
  f.write(f'kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))\n')
  f.write(f'modelSobol2 = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=n_restarts, random_state={rnd_int})\n')
  f.write(f't1_Sobol2 = time.time()\n')
  f.write(f'modelSobol2.fit(X_train_Sobol2, Y_train_Sobol2)\n')
  f.write(f'dt_Sobol2 = time.time() - t1_Sobol2\n')
  f.write(f'print(f\'time for Sobol2: ')
  f.write('{dt_Sobol2')
  f.write('/3600}hrs\')\n')
  f.write(f'\n')
  f.write(f'\n')
  f.write(f'### evaluate models ###\n')
  f.write(f'Y_prediction1296_mean, Y_prediction1296_std = model1296.predict(X_test_1296, return_std=True)\n')
  f.write(f'rmse1296 = np.sqrt(mean_squared_error(Y_test_1296, Y_prediction1296_mean))\n')
  f.write(f'r21296 = r2_score(Y_test_1296, Y_prediction1296_mean)\n')
  f.write(f'print(f\'Grid1296\\n\')\n')
  f.write(f'print(f\'RMSE:') 
  f.write('{rmse1296}\\n\')\n')
  f.write(f'print(f\'R2: ')
  f.write('{r21296}\\n\')\n')
  f.write(f'print(f\'\\n\')\n')
  f.write(f'\n')
  f.write(f'Y_prediction2401_mean, Y_prediction2401_std = model2401.predict(X_test_2401, return_std=True)\n')
  f.write(f'rmse2401 = np.sqrt(mean_squared_error(Y_test_2401, Y_prediction2401_mean))\n')
  f.write(f'r22401 = r2_score(Y_test_2401, Y_prediction2401_mean)\n')
  f.write(f'print(f\'Grid2401\\n\')\n')
  f.write(f'print(f\'RMSE:') 
  f.write('{rmse2401}\\n\')\n')
  f.write(f'print(f\'R2: ')
  f.write('{r22401}\\n\')\n')
  f.write(f'print(f\'\\n\')\n')
  f.write(f'\n')
  f.write(f'Y_predictionSobol1_mean, Y_predictionSobol1_std = modelSobol1.predict(X_test_Sobol1, return_std=True)\n')
  f.write(f'rmseSobol1 = np.sqrt(mean_squared_error(Y_test_Sobol1, Y_predictionSobol1_mean))\n')
  f.write(f'r2Sobol1 = r2_score(Y_test_Sobol1, Y_predictionSobol1_mean)\n')
  f.write(f'print(f\'Sobol1\\n\')\n')
  f.write(f'print(f\'RMSE:') 
  f.write('{rmseSobol1}\\n\')\n')
  f.write(f'print(f\'R2: ')
  f.write('{r2Sobol1}\\n\')\n')
  f.write(f'print(f\'\\n\')\n')
  f.write(f'\n')
  f.write(f'Y_predictionSobol2_mean, Y_predictionSobol2_std = modelSobol2.predict(X_test_Sobol2, return_std=True)\n')
  f.write(f'rmseSobol2 = np.sqrt(mean_squared_error(Y_test_Sobol2, Y_predictionSobol2_mean))\n')
  f.write(f'r2Sobol2 = r2_score(Y_test_Sobol2, Y_predictionSobol2_mean)\n')
  f.write(f'print(f\'Sobol2\\n\')\n')
  f.write(f'print(f\'RMSE:') 
  f.write('{rmseSobol2}\\n\')\n')
  f.write(f'print(f\'R2: ')
  f.write('{r2Sobol2}\\n\')\n')
  f.write(f'print(f\'\\n\')\n')
  f.write(f'\n')
  f.write(f'\n')
  f.write(f'### save models ###\n')
  f.write(f'pickle.dump(model1296, open(\'trained_model1296_{ratio}_{rnd_int}.sav\', \'wb\'))\n')
  f.write(f'pickle.dump(model2401, open(\'trained_model2401_{ratio}_{rnd_int}.sav\', \'wb\'))\n')
  f.write(f'pickle.dump(modelSobol1, open(\'trained_modelSobol1_{ratio}_{rnd_int}.sav\', \'wb\'))\n')
  f.write(f'pickle.dump(modelSobol2, open(\'trained_modelSobol2_{ratio}_{rnd_int}.sav\', \'wb\'))\n')
  f.close()
  
  return os.path.basename(thisPythonFile)
  
  
### loop over ratios for testdata splits ###
for ratio in testsizes:
  #print(f'Ratio for Testdata Split: {ratio}')
  tmp_cwd = os.path.join(cwd, str(ratio))
  os.mkdir(tmp_cwd)
  os.chdir(tmp_cwd)
  #print(f'{os.getcwd()}')
  tmp_datasetfiles = copy_datasetfiles(tmp_cwd, datasetfiles)
  #print(f'{tmp_datasetfiles}')
  
  ## start a batch job for every rnd_int
  batchFiles = []
  for rnd_int in random_ints:
    #print(f'\trnd int: {rnd_int}')
    thisPythonFile = create_python_file(tmp_cwd, rnd_int, ratio, tmp_datasetfiles)
    thisBatchFile = create_batch_file(tmp_cwd, rnd_int, ratio, thisPythonFile)
    #print(f'{thisBatchFile}')
    batchFiles.append(thisBatchFile)
#    break

  executeScriptFile = 'put_everything_here_in_queue.sh'
  if os.path.exists(os.path.join(tmp_cwd, executeScriptFile)):
   os.remove(os.path.join(tmp_cwd, executeScriptFile))
  f = open(os.path.join(tmp_cwd, executeScriptFile), 'w')
  for batchFile in batchFiles:
    f.write(f'sbatch {batchFile}\n')
  f.close()
  
  os.popen(f'chmod +x {executeScriptFile}')
  print(f'Starting squeue for Testsplit ratio: {ratio}')
  os.popen(f'sh {executeScriptFile}')
#  break
