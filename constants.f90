module constants
    implicit none
    integer, parameter :: N = 25   ! number of particles
    real(kind=8), parameter :: L_x,L_y,L_z = 10,10,10 ! the dimensions of the box
    real (kind = 8), dimension(3) :: L = (/L_x,L_y,L_z/)
    real(kind=8), parameter :: max_velocity = 0
    real(kind=8), parameter :: mass = 0.1
    real(kind=8), parameter :: g = -9.81
    real(kind=8), parameter :: radius = 0.1 !radius of the interacting particles
    real(kind=8), parameter :: spring_constant_wall = 1000 !spring constant for the wall - particle interaction
    real(kind=8), parameter :: spring_constant_particle = 1000 ! spring constant for the interaction between particles
    real(kind=8), parameter :: damping_wall = 2 ! damping constant for the wall - particle interaction
    real(kind=8), parameter :: damping_particle = 0.1 ! damping constant for the particle - particle interaction
    real(kind=8), parameter :: dt = 0.001           ! timestep
    real(kind=8), parameter :: simulation_time = 5 ! final t value
end module constants