import matplotlib.pyplot as plt
import numpy as np
## getting the time out
with open('free_fall_constants.f90','r') as g:
     lines_constants = g.readlines()
dt = float(lines_constants[4].split('dt = ')[1].split()[0])
time = float(lines_constants[5].split('simulation_time = ')[1].split()[0])
no_of_frames_to_skip = int(lines_constants[6].split('no_of_frames_to_skip = ')[1].split()[0])
print(dt,time)
time_length = 1
total_steps = int(np.ceil(time/dt))
for k in range(1,total_steps+1):
     if k%no_of_frames_to_skip == 0:
          time_length+=1
time_array = np.linspace(0,time,time_length)
z_positions = np.zeros(len(time_array))
i = 0
with open('simulation.xyz','r') as f:
     lines = f.readlines()
# print(len(lines))
# print(len(time_array))
while i < len(lines):    
    # Extract Z position from the data line
    # Data looks like: C  x_val  y_val  z_val
    data = lines[i+2].split()

    z_positions[int(i/3)]= float(data[3])  # Index 3 is the Z coordinate
    
    i += 3# Jump to  next frame
# Creating the theroetical plot
dummy = []
for i in z_positions:
     if i >= 0.1:
          dummy += [i]
     else:
          break         
z_positions = np.array(dummy,dtype = float)
z_positions_theo = np.zeros(len(z_positions))
time_array_theo = time_array[0:len(z_positions)]
z_positions_theo = z_positions[0] - 0.5*9.81*time_array_theo**2
print(z_positions_theo)
# Create the simulation plot
plt.figure(figsize=(8, 6))
plt.plot(time_array_theo, z_positions, 'b-', linewidth=2,label = 'Simulation')
plt.plot(time_array_theo,z_positions_theo,'r-',linewidth =2,label = 'Theoretical')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Z Position', fontsize=12)
plt.title('Free Fall of a Single Particle', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('free_fall_plot.png')
# Creating error plot
error = np.sqrt(np.sum((z_positions- z_positions_theo)**2)/len(z_positions_theo))
print("RMS error is ", error)
plt.figure(figsize=(8, 6))
plt.plot(time_array_theo,np.abs(z_positions_theo-z_positions),label = 'Mod of error plot')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Mod error', fontsize=12)
plt.title(f'Error plot RMS error = {error}', fontsize=14)
plt.legend()
plt.grid(True)
# # Save the plot instead of showing it (better for WSL/Makefiles)
plt.savefig('free_fall_error_plot.png')
## Calculating Root mean square error ##
######################################

# creating Kinetic energy plot 
with open("kinetic.txt",'r') as f:
     lines = f.readlines()
KE = [float(i) for i in lines]
plt.figure(figsize=(8, 6))
plt.plot(time_array,KE , 'b-', linewidth=2)
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Kinetic energy', fontsize=12)
plt.title('Free Fall of a Single Particle', fontsize=14)
plt.grid(True)
# # Save the plot instead of showing it (better for WSL/Makefiles)
plt.savefig('Kinetic_energy_free_fall.png')