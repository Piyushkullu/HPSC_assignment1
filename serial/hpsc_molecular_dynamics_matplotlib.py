import numpy as np
import matplotlib.pyplot as plt
######### Parameters of the Problem ############
N = 20    # number of particles
L_x,L_y,L_z = 10,10,1 # the dimensions of the box
L = [L_x,L_y,L_z]
max_velocity = 5
mass = 1
g = -9.81
radius = 0.1 # radius of the interacting particles
spring_constant_wall = 1000 # spring constant for the wall - particle interaction
spring_constant_particle = 1000 # spring constant for the interaction between particles
damping_wall = 2 # damping constant for the wall - particle interaction
damping_particle = 0.1 # damping constant for the particle - particle interaction
dt = 0.001           # timestep
simulation_time = 2 # final t value
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
            rij = positions_matrix[another_particle,:]-positions_matrix[particle,:] ## position of J th wrt i th particle
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
#### Simulating body of the code ####
# plt.ion()
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.set_xlim(0, L_x)
# ax.set_ylim(0, L_y)
# ax.set_zlim(0, L_z)
# scat = ax.scatter(positions_matrix[:,0], positions_matrix[:,1], positions_matrix[:,2])
# for i in time[1:]:
#     updater_function(positions_matrix,velocity_matrix,force_matrix,dt,mass)
#     scat._offsets3d = (positions_matrix[:,0], positions_matrix[:,1], positions_matrix[:,2])  # update only
#     plt.pause(0.001)
# plt.ioff()
# plt.show()
from matplotlib.animation import FuncAnimation

####  Initializing the Plot ####
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(0, L_x)
ax.set_ylim(0, L_y)
ax.set_zlim(0, L_z)

# The scatter object we will update
scat = ax.scatter(positions_matrix[:,0], positions_matrix[:,1], positions_matrix[:,2])

def update(frame):
    """ This function runs for every 'frame' of the animation """
    # Run multiple physics steps per frame for a smoother 'real-time' feel
    steps_per_frame = 4
    for _ in range(steps_per_frame):
        updater_function(positions_matrix, velocity_matrix, force_matrix, dt, mass)
    
    # Update the 3D positions of the dots
    scat._offsets3d = (positions_matrix[:,0], positions_matrix[:,1], positions_matrix[:,2])
    return scat,

# interval=20 means roughly 50 frames per second
ani = FuncAnimation(fig, update, frames=len(time)//4, interval=20, blit=False)

plt.show()