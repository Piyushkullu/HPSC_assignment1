import numpy as np
import matplotlib.pyplot as plt 
with open('constants.f90','r') as g:
     lines_constants = g.readlines()
dt = float(lines_constants[4].split('dt = ')[1].split()[0])
time = float(lines_constants[5].split('simulation_time = ')[1].split()[0])
no_of_frames_to_skip = int(lines_constants[6].split('no_of_frames_to_skip = ')[1].split()[0])
N = int(lines_constants[7].split('N = ')[1].split()[0])
# code to compute length of time array
time_length = 1
total_steps = int(np.ceil(time/dt))
for k in range(1,total_steps+1):
     if k%no_of_frames_to_skip == 0:
          time_length+=1
time_array = np.linspace(0,time,time_length)
with open('kinetic.txt','r') as f:
    lines = f.readlines()
kinetic_energy_array = [float(i) for i in lines]
plt.figure(figsize=(8, 6))
plt.plot(time_array, kinetic_energy_array, 'b-', linewidth=2)
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Kinetic eneergy', fontsize=12)
plt.title(f'Multi particle kinetic energy for N = {N}', fontsize=14)
plt.grid(True)
# # Save the plot instead of showing it (better for WSL/Makefiles)
plt.savefig('kinetic_energy.png')
