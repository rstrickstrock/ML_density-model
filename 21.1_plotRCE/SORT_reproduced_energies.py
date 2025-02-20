import os

energies_to_sort_file = "thisOpt_energies_UNsorted.txt"
###
sorted_energies_file = "thisOpt_energies_sorted.txt"
sort_indices = "SRTED_index.txt"
###
if not os.path.isfile(sort_indices):
  print(f'Indexfile \"{sort_indices}\" not found.')
  exit()

if not os.path.isfile(energies_to_sort_file):
  print(f'File containing energies to be sorted \"{energies_to_sort_file}\" not found.')
  exit()

if os.path.isfile(sorted_energies_file):
  os.remove(sorted_energies_file)

## get sort indices
indices = []
with open(sort_indices, 'r') as my_file:
  lines = my_file.readlines()
for index in lines:
  indices.append(int(index))
#print(f'{indices}')

## get energies to be sorted
energies = []
with open(energies_to_sort_file, 'r') as my_file:
  lines = my_file.readlines()
for energy in lines:
  if energy.startswith("molec"):
    energy = energy.split(" ")[1]
  energies.append(float(energy))
#print(f'{energies}')


## write new file with sorted energies
with open(sorted_energies_file, 'w') as my_file:
  for index in indices:
    my_file.write(f'{energies[index-1]}\n')
    #print(f'{energies[index-1]}')
