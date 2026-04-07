## Overview
This project aims at simulating particles in a box using string dashpot model and damping in collisions that is proportional to 
the relative velocity between surfaces. The implementation is done both serially and parallely, for parallel implementation use 
of open mp shared memory parallelism is used.
respectivelly. 
## Structure
Two seperate directories are create for serial, parallel implementation respectively. To run simulations using any of the two, the user
needs to be in that specific directory.

- `parallel/` → OpenMP implementation  
- `serial/` → Serial implementation 

To specify the parameters of the system the user needs to change the values of constants defined in the `constants.f90` file.
For running the simulation run the following command :

``` bash
make simulation.xyz
```

that will create simulation.xyz file which has positions of each particle at various time stamps in well formatted manner.
The .xyz can then be opened in simulation softwares such as OVITO which shall do the rendering using the positions specified in that file.

Using `make free_fall` creates a simple free fall simulation of a single particle (whose paremeters can be defined in `free_fall_constants.f90` file) 
and saves the results in simulation.xyz again. Rendering can then be done in the same way as for the multi - particle system.
It is advised to use `make clean` for each new try to delete the .o , .exe files so that random results don't show up.

## Subroutine Definitions
-`calc_force `: takes in position, velocity array that consists of position/velocity of each particle in their columns respectively and returns a force array that is calculated base on interaction with other particles and walls. The force array has the same dimension as that of position and velocity.

-`updater_function`: takes in positions, velocity and force arrays and updates them their values at `t + dt`, if `t` is the current time. The updation is done using semi - implicit euler method.

-`ouput_file_generator`: takes in position array at a time `t` and adds the data to `simulation.xyz` file in well formatted manner.

-`kinetic_energy_sub`: takes in velocity array at a time `t` and returns the kinetic energy of the system at that time.
 ## Main Body
 `simulator_fortran` is the main body of the simulation, that runs the simulation. It starts with random velocity and positions arrays
 and then updates them for each time step by calling  `updater_function` and writing the resulting position array to simulation.xyz using `outfile_file_generator` subroutine. `Updater function` itself calls `calc_force` to calculate the force array at a given time that would then be used for updating velocity array which shall further be used for updating position array.

 ## Parallel Implementation
 The parallel implementation was done in two phases, one where there is fork - join overhead and one in which I have tried to eliminate it. The one with fork - join overhead is currently in the main branch of the code and the improved one is in the changing_parallel_imp... branch. 
 
 For parallel implementation open directive such as `!$omp parallel do ` was used in the `calc_force` subroutine that parallelised the force calculation process from the position and velocity arrays. But this approach had more fork-join overhead as threads were being created every time `calc_force ` was being called, and believe me it is called a lot of times. To be precise it is called total_time/time_step_size number of times which is huge.

 The improved version fixed this problem by having the threads initialised before the main body loop and then use them once parallel work is encountered. Correspondigly the `!$omp parallel do` statement in `calc_force` is changed to `!$omp do`.

 Other subroutines and parts of the code have negligible time consumptions as compared to the `calc_force` subroutine thus focus was only placed on optimising it.
 ## Note
 In order to run free fall simulations the user needs to have python3 environment named simulator in the home directory. The path can be changed by editing the make file line
 ```bash
PYTHON = ../simulator/bin/python3
```


