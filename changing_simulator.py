import sys
print("I am running from:", sys.executable)
import numpy as np
import matplotlib.pyplot as plt
######### Parameters of the Problem ############
N = 25   # number of particles
L_x,L_y,L_z = 10,10,10 # the dimensions of the box
L = [L_x,L_y,L_z]
max_velocity = 0
mass = 0.1
g = -9.81
radius = 0.1 # radius of the interacting particles
spring_constant_wall = 1000 # spring constant for the wall - particle interaction
spring_constant_particle = 1000 # spring constant for the interaction between particles
damping_wall = 2 # damping constant for the wall - particle interaction
damping_particle = 0.1 # damping constant for the particle - particle interaction
dt = 0.001           # timestep
simulation_time = 5 # final t value
##################################################
### Variable defining ###
time = np.arange(0,simulation_time,dt)
#### Function Definitions ###
def calc_force(pos,vel):
    force = np.zeros((N,3))
    force[:,2] = mass*g
    for particle in range(N):
        ### wall_force ###
        for co_ord in range(3):
            d = pos[particle,co_ord]
            rel_vel_to_wall = vel[particle,co_ord]
            if d>=radius and d<=L[co_ord]-radius:
                continue
            if d <= radius:
                spring_force_wall = spring_constant_wall*np.abs(d-radius)
        
            elif d>= L[co_ord]-radius:
                spring_force_wall = -spring_constant_wall*np.abs(d-L[co_ord]+radius)
            
            damping_force_wall = -damping_wall*rel_vel_to_wall
            force[particle,co_ord] += spring_force_wall + damping_force_wall
        for another_particle in range(particle+1,N):
            rij = pos[another_particle,:]-pos[particle,:] ## position of J th wrt i th particle
            dij = np.linalg.norm(rij)
            rij_unit = rij/dij
            delta = 2*radius - dij
            if delta <0:
                continue
            else:
                spring_force_particle = spring_constant_particle*delta
            v_approach = np.dot(vel[particle,:],rij_unit)+np.dot(vel[another_particle,:],-rij_unit)
            damping_force_particle = damping_particle*v_approach
            net_force = spring_force_particle*(-rij_unit) +damping_force_particle*(-rij_unit) 
            force[particle,:] += net_force
            force[another_particle,:] += -net_force
    return force

#### Updater function definition ####
def updater_function(pos,vel,force,dt,mass):
    ### updating postion ###
    np.add(pos,vel*dt,out=pos)
    ### updating velocity ###
    np.add(vel,(force/mass)*dt,out=vel)
    ### updating force ###
    force[:] = calc_force(pos,vel)

####  Initializing the state of the system ####
positions_matrix = np.random.uniform([radius,radius,radius],[L_x-radius,L_y-radius,L_z-radius],(N,3))
velocity_matrix = np.random.rand(N,3)*max_velocity
force_matrix = calc_force(positions_matrix,velocity_matrix)
# ... (Keep all your existing parameters, initializations, and functions above this) ...

print("Starting simulation and exporting data...")

# Open a new text file in "write" mode
with open("trajectory.xyz", "w") as file:
    
    # Loop through the time array
    for step, current_time in enumerate(time[1:]):
        
        # 1. Run the Physics engine
        updater_function(positions_matrix, velocity_matrix, force_matrix, dt, mass)
        
        # 2. Export the data
        # We use a modulo operator (%) to only save every 10th step.
        # Saving every 0.001s creates massive files. Saving every 0.01s is plenty for smooth video.
        if step % 10 == 0:
            
            # Write Line 1: Number of particles
            file.write(f"{N}\n")
            
            # Write Line 2: Comment line (We will put the current time here)
            file.write(f'Lattice="{L_x} 0.0 0.0 0.0 {L_y} 0.0 0.0 0.0 {L_z}" Time={current_time:.4f}\n')
            
            # Write Lines 3 to N+2: The particle coordinates
            for i in range(N):
                x = positions_matrix[i, 0]
                y = positions_matrix[i, 1]
                z = positions_matrix[i, 2]
                
                # "P" is just a dummy name for "Particle". 
                # The formatting forces it to keep 5 decimal places so the columns line up nicely.
                file.write(f"P {x:.5f} {y:.5f} {z:.5f}\n")

print("Simulation complete! 'trajectory.xyz' has been generated.")