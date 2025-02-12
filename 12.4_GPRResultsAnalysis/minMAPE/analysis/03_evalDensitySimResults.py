import os
import glob
import shutil
import subprocess

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/minMAPE"

simDirs = glob.glob(os.path.join(pwd, "evalOptParams_DensitySims", "run-*"))
#print(f'{simDirs}')

thisCWD = os.getcwd()
for simDir in simDirs:
  #print(f'{simDir}')
  evalFileSRC = os.path.join(pwd, "analysis", "02_density", "batch_slurm_eval_PhysProp.sh")
  #print(f'{evalFileSRC}')
  evalFileDST = os.path.join(simDir, "batch_slum_eval_density.sh")
  #print(f'{evalFileDST}')
  shutil.copy(evalFileSRC, evalFileDST)

  os.chdir(simDir)
  thisCommand = f'sbatch batch_slum_eval_density.sh'
  p = subprocess.Popen(thisCommand, stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()
  p_status = p.wait()
  os.chdir(thisCWD)

