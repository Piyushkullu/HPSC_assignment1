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
-`calc_force :` takes in position, velocity vecto

