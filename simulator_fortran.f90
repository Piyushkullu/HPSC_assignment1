program simulator_fortran
    use constants
    implicit none 
    !Variable defining 
    integer ::  total_steps
    real(kind = wp), dimension(3,N) :: positions
    real(kind = wp), dimension(3,N):: velocity
    real(kind = wp), dimension(3,N) :: force
    integer :: i,step
    total_steps = ceiling(simulation_time/dt)
    ! Initializing the problem
    call random_seed()
    call random_number(positions)
    call random_number(velocity)
    do i = 1,3
       positions(i,:) = (L(i)-2*radius)*positions(i,:) + radius
    end do
    velocity = (velocity-0.5_wp)*max_velocity*2_wp
    ! Calculate the initial force
    call calc_force(positions,velocity,force)
    ! simulating for various time t
    call output_file_generator(positions, 0.0_wp)
    do step = 2,total_steps
       call updater_function(positions,velocity,force)
       if (MOD(step,no_of_frames_to_skip)==0) then
          call output_file_generator(positions,step*dt)
        end if
    end do
end program simulator_fortran