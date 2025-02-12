import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/maxR2"
topValues = 3
diffType = "relTargSimDiff"

if diffType == "relTargSimDiff":
  cbarLabel = f'rel. diff Target vs. Simulation'
elif diffType == "absTargSimDiff":
  cbarLabel = f'abs. diff Target vs. Simulation'
elif diffType == "relPredSimDiff":
  cbarLabel = f'rel. diff Prediction vs. Simulation'
elif diffType == "absPredSimDiff":
  cbarLabel = f'abs. diff Prediction vs. Simulation'
else:
  print(f'diffType: {diffType} not valid. Must be one of "relTargSimDiff", "absTargSimDiff", "relPredSimDiff", "absPredSimDiff". Exit.')
  exit()


thisDir = os.path.basename(pwd)
#print(f'{thisDir}')

statsFile = os.path.join(pwd, "StatsDensity_withSimResults.csv")
stats = pd.read_csv(statsFile)
stats = stats.drop(stats.columns[0], axis=1)
#print(f'{stats}')

SigC = stats["SigC"].to_numpy()
#print(f'{SigC}')
SigH = stats["SigH"].to_numpy()
EpsC = stats["EpsC"].to_numpy()
EpsH = stats["EpsH"].to_numpy()

diff = stats[diffType].to_numpy()

sortedDiff = stats[diffType].abs().sort_values()
#print(f'{type(sortedDiff)}')
topSigC = []
topSigH = []
topEpsC = []
topEpsH = []
topDiff = []
for i in range(0, topValues):
  #print(f'{sortedDiff.iloc[i]}')
  thisDiff = sortedDiff.iloc[i]
  #print(f'{thisDiff}')
  thisIndex = sortedDiff[sortedDiff == thisDiff].index[0]
  #print(f'{thisIndex}')
  #print(f'{stats["SigC"][thisIndex]}')
  topSigC.append(stats["SigC"][thisIndex])
  topSigH.append(stats["SigH"][thisIndex])
  topEpsC.append(stats["EpsC"][thisIndex])
  topEpsH.append(stats["EpsH"][thisIndex])
  topDiff.append(stats[diffType][thisIndex])

gs_kw = dict(width_ratios=[1, 1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['SigCvsSigH', 'SigCvsEpsC', 'SigCvsEpsH'], 
                               ['SigHvsEpsC', 'SigHvsEpsH', 'EpsCvsEpsH']], 
                               gridspec_kw=gs_kw, figsize=(18.0, 12.0))

p1 = axd["SigCvsSigH"].scatter(SigC, SigH, c=diff, marker='o')#, edgecolor="#44AA99")
axd["SigCvsSigH"].set(xlabel=f'SigC', ylabel=f'SigH')
axd["SigCvsSigH"].set_title("SigC vs SigH", fontweight='bold')
fig.colorbar(p1, ax=axd["SigCvsSigH"], label=f'{cbarLabel}')
axd["SigCvsSigH"].scatter(topSigC, topSigH, label='top 3 results', marker='x', color="#FF0000")
axd["SigCvsSigH"].legend()

p2 = axd["SigCvsEpsC"].scatter(SigC, EpsC, c=diff, marker='o')#, edgecolor="#44AA99")
axd["SigCvsEpsC"].set(xlabel=f'SigC', ylabel=f'EpsC')
axd["SigCvsEpsC"].set_title("SigC vs EpsC", fontweight='bold')
fig.colorbar(p2, ax=axd["SigCvsEpsC"], label=f'{cbarLabel}')
axd["SigCvsEpsC"].scatter(topSigC, topEpsC, label='top 3 results', marker='x', color="#FF0000")
axd["SigCvsEpsC"].legend()

p3 = axd["SigCvsEpsH"].scatter(SigC, EpsH, c=diff, marker='o')#, edgecolor="#44AA99")
axd["SigCvsEpsH"].set(xlabel=f'SigC', ylabel=f'EpsH')
axd["SigCvsEpsH"].set_title("SigC vs EpsH", fontweight='bold')
fig.colorbar(p3, ax=axd["SigCvsEpsH"], label=f'{cbarLabel}')
axd["SigCvsEpsH"].scatter(topSigC, topEpsH, label='top 3 results', marker='x', color="#FF0000")
axd["SigCvsEpsH"].legend()

p4 = axd["SigHvsEpsC"].scatter(SigH, EpsC, c=diff, marker='o')#, edgecolor="#44AA99")
axd["SigHvsEpsC"].set(xlabel=f'SigH', ylabel=f'EpsC')
axd["SigHvsEpsC"].set_title("SigH vs EpsC", fontweight='bold')
fig.colorbar(p4, ax=axd["SigHvsEpsC"], label=f'{cbarLabel}')
axd["SigHvsEpsC"].scatter(topSigH, topEpsC, label='top 3 results', marker='x', color="#FF0000")
axd["SigHvsEpsC"].legend()

p5 = axd["SigHvsEpsH"].scatter(SigH, EpsH, c=diff, marker='o')#, edgecolor="#44AA99")
axd["SigHvsEpsH"].set(xlabel=f'SigH', ylabel=f'EpsH')
axd["SigHvsEpsH"].set_title("SigH vs EpsH", fontweight='bold')
fig.colorbar(p5, ax=axd["SigHvsEpsH"], label=f'{cbarLabel}')
axd["SigHvsEpsH"].scatter(topSigH, topEpsH, label='top 3 results', marker='x', color="#FF0000")
axd["SigHvsEpsH"].legend()

p6 = axd["EpsCvsEpsH"].scatter(EpsC, EpsH, c=diff, marker='o')#, edgecolor="#44AA99")
axd["EpsCvsEpsH"].set(xlabel=f'EpsC', ylabel=f'EpsH')
axd["EpsCvsEpsH"].set_title("EpsC vs EpsH", fontweight='bold')
fig.colorbar(p6, ax=axd["EpsCvsEpsH"], label=f'{cbarLabel}')
axd["EpsCvsEpsH"].scatter(topEpsC, topEpsH, label='top 3 results', marker='x', color="#FF0000")
axd["EpsCvsEpsH"].legend()

plt.tight_layout()
#plt.show()
plt.savefig(f'optParams-vs-{diffType}_{thisDir}.png', dpi=300, format='png')

#TODO:
# write top results in File







