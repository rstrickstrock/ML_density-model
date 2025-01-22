import matplotlib.pyplot as plt
import pandas as pd

import os
import glob


statisticsFile = 'StatisticsOfGPTrainingDiffKernels.csv'
predictionsFile = 'yPredictionsOfGPModelsDiffKernels_usingPrevOptParams.csv'

if not os.path.isfile(statisticsFile):
  print(f'Can not find and open \'{statisticsFile}\'. Exit.')
  exit()
else:
  dfStatistics = pd.read_csv(statisticsFile)
  #print(f'{dfStatistics}')
  try:
    dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])
  except:
    print(f'Something went wrong with\'dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])\'.')
  else:
    #print(f'{dfStatistics}')
    pass
    
if not os.path.isfile(predictionsFile):
  print(f'Can not find and open \'{predictionsFile}\'. Exit.')
  exit()
else:
  dfPredictions = pd.read_csv(predictionsFile)
  #print(f'{dfPredictions}')
  try:
    dfPredictions = dfPredictions.drop(columns=["Unnamed: 0"])
  except:
    print(f'Something went wrong with\'dfPredictions = dfPredictions.drop(columns=["Unnamed: 0"])\'.')
  else:
    #print(f'{dfPredictions}')
    pass
    
## filter based on following constraints
diffMax = 10
diffMin = -10
subsetDiff = dfPredictions[dfPredictions["diff"] <= diffMax]
#print(f'{len(subsetDiff)}')
subsetDiff = subsetDiff[subsetDiff["diff"] >= diffMin]
#print(f'{subsetDiff}')

rmseMax = 25
rmseMin = 0
subsetRMSE = dfStatistics[dfStatistics["rmse"] <= rmseMax]
#print(f'{len(subsetRMSE)}')
subsetRMSE = subsetRMSE[subsetRMSE["rmse"] >= rmseMin]
#print(f'{subsetRMSE}')

r2Max = 1.0
r2Min = 0.94
subsetR2 = dfStatistics[dfStatistics["r2"] <= r2Max]
#print(f'{len(subsetR2)}')
subsetR2 = subsetR2[subsetR2["r2"] >= r2Min]
#print(f'{subsetR2}')

## combined RMSE/R2 filter
subsetRMSER2 = subsetRMSE[subsetRMSE["r2"] <= r2Max]
subsetRMSER2 = subsetRMSER2[subsetRMSER2["r2"] >= r2Min]
#print(f'{subsetRMSER2}')
minRMSE = subsetRMSER2['rmse'].min()
minRMSE = minRMSE - 0.01*minRMSE
maxRMSE = subsetRMSER2['rmse'].max()
maxRMSE = maxRMSE + 0.01*maxRMSE
minR2 = subsetRMSER2['r2'].min()
minR2 = minR2 - 0.001*minR2
maxR2 = subsetRMSER2['r2'].max()
maxR2 = maxR2 + 0.001*maxR2

#print(f'Different Datasets: {subsetRMSER2["dataset"].unique()}')
#print(f'Different Kernels: {subsetRMSER2["kernel"].unique()}')
subsetRBF = subsetRMSER2[subsetRMSER2["kernel"] == "RBF"]
subsetMatern = subsetRMSER2[subsetRMSER2["kernel"] == "Matern"]
subsetRQ = subsetRMSER2[subsetRMSER2["kernel"] == "RQ"]
subsetESS = subsetRMSER2[subsetRMSER2["kernel"] == "ESS"]

subsetRBFSobol1 = subsetRBF[subsetRBF["dataset"] == "Sobol1"]
subsetRBFSobol2 = subsetRBF[subsetRBF["dataset"] == "Sobol2"]
subsetMaternSobol1 = subsetMatern[subsetMatern["dataset"] == "Sobol1"]
subsetMaternSobol2 = subsetMatern[subsetMatern["dataset"] == "Sobol2"]
subsetRQSobol1 = subsetRQ[subsetRQ["dataset"] == "Sobol1"]
subsetRQSobol2 = subsetRQ[subsetRQ["dataset"] == "Sobol2"]
subsetESSSobol1 = subsetESS[subsetESS["dataset"] == "Sobol1"]
subsetESSSobol2 = subsetESS[subsetESS["dataset"] == "Sobol2"]
## plots
gs_kw = dict(width_ratios=[2, 1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['AllInOne', 'RBF', 'RQ'], 
                               ['AllInOne', 'Matern', 'ESS']], 
                               gridspec_kw=gs_kw, figsize=(28.0, 14.0))
                               
axd["AllInOne"].scatter(subsetMaternSobol1["rmse"], subsetMaternSobol1["r2"], label="Matern, Sobol1", c="#332288", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetMaternSobol2["rmse"], subsetMaternSobol2["r2"], label="Matern, Sobol2", c="#332288", marker='P', edgecolor="#AA4499")
axd["AllInOne"].scatter(subsetRQSobol1["rmse"], subsetRQSobol1["r2"], label="RQ, Sobol1", c="#88CCEE", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetRQSobol2["rmse"], subsetRQSobol2["r2"], label="RQ, Sobol2", c="#88CCEE", marker='P', edgecolor="#AA4499")
axd["AllInOne"].scatter(subsetESSSobol1["rmse"], subsetESSSobol1["r2"], label="ESS,Sobol1", c="#DDCC77", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetESSSobol2["rmse"], subsetESSSobol2["r2"], label="ESS, Sobol2", c="#DDCC77", marker='P', edgecolor="#AA4499")
axd["AllInOne"].scatter(subsetRBFSobol1["rmse"], subsetRBFSobol1["r2"], label="RBF, Sobol1", c="#117733", marker='o', edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetRBFSobol2["rmse"], subsetRBFSobol2["r2"], label="RBF, Sobol2", c="#117733", marker='P', edgecolor="#AA4499")
axd["AllInOne"].legend()
axd["AllInOne"].set(xlabel="RMSE", ylabel="R2")
axd["AllInOne"].set_title("All In One (Kernels + Datasets)", fontweight='bold')
axd["AllInOne"].set_xlim([minRMSE, maxRMSE])
axd["AllInOne"].set_ylim([minR2, maxR2])

axd["RBF"].scatter(subsetRBFSobol1["rmse"], subsetRBFSobol1["r2"], label="Sobol1", c="#117733", marker='o', edgecolor="#44AA99", s=175)
axd["RBF"].scatter(subsetRBFSobol2["rmse"], subsetRBFSobol2["r2"], label="Sobol2", c="#117733", marker='P', edgecolor="#AA4499", s=175)
axd["RBF"].legend()
axd["RBF"].set(xlabel="RMSE", ylabel="R2")
axd["RBF"].set_title("Kernel: RBF", fontweight='bold')
axd["RBF"].set_xlim([minRMSE, maxRMSE])
axd["RBF"].set_ylim([minR2, maxR2])

axd["Matern"].scatter(subsetMaternSobol1["rmse"], subsetMaternSobol1["r2"], label="Sobol1", c="#332288", marker='.', edgecolor="#44AA99", s=175)
axd["Matern"].scatter(subsetMaternSobol2["rmse"], subsetMaternSobol2["r2"], label="Sobol2", c="#332288", marker='P', edgecolor="#AA4499", s=175)
axd["Matern"].legend()
axd["Matern"].set(xlabel="RMSE", ylabel="R2")
axd["Matern"].set_title("Kernel: Matern", fontweight='bold')
axd["Matern"].set_xlim([minRMSE, maxRMSE])
axd["Matern"].set_ylim([minR2, maxR2])

axd["RQ"].scatter(subsetRQSobol1["rmse"], subsetRQSobol1["r2"], label="Sobol1", c="#88CCEE", marker='.', edgecolor="#44AA99", s=175)
axd["RQ"].scatter(subsetRQSobol2["rmse"], subsetRQSobol2["r2"], label="Sobol2", c="#88CCEE", marker='P', edgecolor="#AA4499", s=175)
axd["RQ"].legend()
axd["RQ"].set(xlabel="RMSE", ylabel="R2")
axd["RQ"].set_title("Kernel: RQ", fontweight='bold')
axd["RQ"].set_xlim([minRMSE, maxRMSE])
axd["RQ"].set_ylim([minR2, maxR2])

axd["ESS"].scatter(subsetESSSobol1["rmse"], subsetESSSobol1["r2"], label="Sobol1", c="#DDCC77", marker='.', edgecolor="#44AA99", s=175)
axd["ESS"].scatter(subsetESSSobol2["rmse"], subsetESSSobol2["r2"], label="Sobol2", c="#DDCC77", marker='P', edgecolor="#AA4499", s=175)
axd["ESS"].legend()
axd["ESS"].set(xlabel="RMSE", ylabel="R2")
axd["ESS"].set_title("Kernel: ESS", fontweight='bold')
axd["ESS"].set_xlim([minRMSE, maxRMSE])
axd["ESS"].set_ylim([minR2, maxR2])

plt.tight_layout()
plt.show()

exit()

axd["RMSEvsDiff"].set(xlabel="RMSE", ylabel="Diff")
axd["RMSEvsDiff"].set_title("RMSE vs Diff", fontweight='bold')
axd["RMSEvsDiff"].plot([0, 0], [diffMin, diffMax], ls='-', color='red', label='Zoom Range')
axd["RMSEvsDiff"].legend()
axd["ZoomRMSEvsDiff"].scatter(subsetDiff["rmse"], subsetDiff["diff"], label="RMSE vs Diff", c="#377eb8")
axd["ZoomRMSEvsDiff"].legend()
axd["ZoomRMSEvsDiff"].set(xlabel="RMSE", ylabel="Diff")
axd["ZoomRMSEvsDiff"].set_title("Zoomed RMSE vs Diff", fontweight='bold')
axd["DiffFiltered"].scatter(subsetDiff["rmse"], subsetDiff["r2"], label=f'{diffMin} <= diff <= {diffMax}', c="#377eb8")
axd["DiffFiltered"].legend()
axd["DiffFiltered"].set(xlabel="RMSE", ylabel="R2")
axd["DiffFiltered"].set_title(f'RMSE vs R2 filtered by {diffMin}<=diff<={diffMax}', fontweight='bold')

axd["R2vsDiff"].scatter(dfCombinedData["r2"], dfCombinedData["diff"], label="R2 vs Diff", c="#4daf4a")
axd["R2vsDiff"].set(xlabel="R2", ylabel="Diff")
axd["R2vsDiff"].set_title("R2 vs Diff", fontweight='bold')
axd["R2vsDiff"].plot([0, 0], [diffMin, diffMax], ls='-', color='red', label='Zoom Range')
axd["R2vsDiff"].legend()
axd["ZoomR2vsDiff"].scatter(subsetDiff["r2"], subsetDiff["diff"], label="R2 vs Diff", c="#4daf4a")
axd["ZoomR2vsDiff"].legend()
axd["ZoomR2vsDiff"].set(xlabel="R2", ylabel="Diff")
axd["ZoomR2vsDiff"].set_title("Zoomed R2 vs Diff", fontweight='bold')
axd["ZoomR2vsDiff"].set_xlim([0, 1.0])
#axd["ZoomR2vsDiff"].set_ylim([diffMin, diffMax])
axd["RMSEFiltered"].scatter(subsetRMSE["r2"], subsetRMSE["diff"], label=f'{rmseMin} <= rmse <= {rmseMax}', c="#4daf4a")
axd["RMSEFiltered"].legend()
axd["RMSEFiltered"].set(xlabel="R2", ylabel="Diff")
axd["RMSEFiltered"].set_title(f'R2 vs Diff filtered by rmse<={rmseMax}', fontweight='bold')

axd["RMSEvsR2"].scatter(dfCombinedData["rmse"], dfCombinedData["r2"], label="RMSE vs R2", c="#852E02")
axd["RMSEvsR2"].set(xlabel="RMSE", ylabel="R2")
axd["RMSEvsR2"].set_title("RMSE vs R2", fontweight='bold')
thisXMin = 15
thisXMax = 50
thisYMin = 0.7
thisYMax = 1.0
axd["RMSEvsR2"].plot([rmseMin, rmseMax], [0, 0], ls='-', color='red', label='Zoom Range')
axd["RMSEvsR2"].legend()
axd["ZoomRMSEvsR2"].scatter(subsetRMSE["rmse"], subsetRMSE["r2"], label="RMSE vs R2", c="#852E02")
axd["ZoomRMSEvsR2"].legend()
axd["ZoomRMSEvsR2"].set(xlabel="RMSE", ylabel="R2")
axd["ZoomRMSEvsR2"].set_title("Zoomed RMSE vs R2", fontweight='bold')
axd["R2Filtered"].scatter(subsetR2["rmse"], subsetR2["diff"], label=f'{r2Min} <= r2 <= {r2Max}', c="#852E02")
axd["R2Filtered"].legend()
axd["R2Filtered"].set(xlabel="RMSE", ylabel="Diff")
axd["R2Filtered"].set_title(f'RMSE vs Diff filtered by {r2Min}<=r2<={r2Max}', fontweight='bold')

X = subsetRMSER2["rmse"]
Y = subsetRMSER2["r2"]
Z = subsetRMSER2["diff"]
cm = plt.cm.get_cmap('Accent')
#scatter = axd["RMSER2Filtered"].scatter(X, Y, c=Z.to_numpy(), cmap=cm, vmin=-max(np.sqrt(np.power(Z.min(),2)), np.sqrt(np.power(Z.max(), 2))), vmax=max(np.sqrt(np.power(Z.min(),2)), np.sqrt(np.power(Z.max(), 2))))
scatter = axd["RMSER2Filtered"].scatter(X, Y, c=Z.to_numpy(), cmap=cm, vmin=2*diffMin, vmax=diffMax)
axd["RMSER2Filtered"].set(xlabel="RMSE", ylabel="R2")
axd["RMSER2Filtered"].set_title(f'RMSE vs R2 filtered by {r2Min}<=r2<={r2Max} AND rmse<={rmseMax}, colorcoded by Diff ', fontweight='bold')
cbar = fig.colorbar(scatter, ax=axd["RMSER2Filtered"], orientation='vertical')
cbar.set_label("Diff")

plt.tight_layout()
plt.show()
