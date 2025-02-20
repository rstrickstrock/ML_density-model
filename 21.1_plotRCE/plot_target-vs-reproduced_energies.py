import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

plt.style.use('tableau-colorblind10')

savename = 'test.png'


cm = 1/2.54 # cm in inches
mm = cm*0.1

tick_size = 18
label_size = 18
title_size = 22
legend_size = 14 
dots_per_inch = 300

line_width = 2.5
marker_edge_width = 1.5
marker_size = 6
grid_line_width = 0.5

figure_width = 315    #mm
figure_heigth = 220   #mm



def read_energy_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    
    return np.array(lines, dtype=float)
    

target_energy_file = 'target_energies_sorted.txt'
good_energy_file = 'thisOpt_energies_sorted.txt'

num_energies = np.linspace(1, 96, 96)
target_energies = read_energy_file(target_energy_file)
#print(f'{target_energies}')
good_energies = read_energy_file(good_energy_file)

plt.figure(figsize=(figure_width*mm, figure_heigth*mm), dpi=dots_per_inch)
plt.plot(num_energies, target_energies, ':x', color='#006BA4', label='Target RCE', zorder=1, linewidth=line_width, ms=marker_size, mew=marker_edge_width)
plt.plot(num_energies, good_energies, '-.o', color='#FF800E', label='RCE using the optimized parameter set', zorder=2, linewidth=line_width, ms=marker_size, mew=marker_edge_width)

plt.fill_between(x=num_energies, y1=target_energies-0.289, y2=target_energies+0.289, color='#006BA4', alpha=0.2, label='Expected Avg. Error Range (10%)')
plt.grid(color='gray', linestyle='dashed', linewidth=grid_line_width)

plt.ylabel('Relative Conformational Energy [kcal/mol]', size=label_size, fontweight='bold')
plt.xlabel('Energy State $i$ [-]', size=label_size, fontweight='bold')
plt.xticks(fontsize=tick_size)
plt.yticks(fontsize=tick_size)

plt.title('Target and Reproduced RCE', size=title_size, fontweight='bold')
plt.legend(fontsize=legend_size, loc='upper left')

    
plt.savefig(savename)    
#plt.show()





