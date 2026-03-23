module constants
    implicit none
    integer, parameter :: wp = 4
    integer, parameter :: N = 25   ! number of particles
    real(kind=wp), parameter :: L_x = 10,L_y = 10,L_z = 10 ! the dimensions of the box
    real (kind = wp), dimension(3) :: L = (/L_x,L_y,L_z/)
    real(kind=wp), parameter :: max_velocity = 2
    real(kind=wp), parameter :: mass = 0.1
    real(kind=wp), parameter :: g = -9.81
    real(kind=wp), parameter :: radius = 0.1 !radius of the interacting particles
    real(kind=wp), parameter :: spring_constant_wall = 1000 !spring constant for the wall - particle interaction
    real(kind=wp), parameter :: spring_constant_particle = 1000 ! spring constant for the interaction between particles
    real(kind=wp), parameter :: damping_wall = 2 ! damping constant for the wall - particle interaction
    real(kind=wp), parameter :: damping_particle = 0.1 ! damping constant for the particle - particle interaction
    real(kind=wp), parameter :: dt = 0.001           ! timestep
    real(kind=wp), parameter :: simulation_time = 5 ! final t value
end module constants