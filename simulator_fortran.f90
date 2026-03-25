program simulator_fortran
    use constants
    implicit none 
    !Variable defining 
    integer ::  total_steps
    real(kind = wp), dimension(3,N) :: positions
    real(kind = wp), dimension(3,N):: velocity
    real(kind = wp), dimension(3,N) :: force
    integer :: i,step
    real(kind = wp) :: KE
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
    ! Calculating the initial kinetic energy
    call kinetic_energy(velocity,KE)
    open(unit=kinetic_unit_position, file="kinetic.txt", position="append", status="unknown")
    write(kinetic_unit_position, *) KE
    ! writing out the initial config to .xyz file
    ! open the simulation.xyz file
    open(unit=output_unit_position, file="simulation.xyz", position="append", status="unknown")
    call output_file_generator(positions, 0.0_wp)
     ! simulating for various time t
    do step = 1,total_steps
       call updater_function(positions,velocity,force)
       ! skiping 'no_of_frames_to_skip' number of iterations  to write the output 
       if (MOD(step,no_of_frames_to_skip)==0) then
         call output_file_generator(positions,step*dt)
         call kinetic_energy(velocity,KE)
         write(kinetic_unit_position, *) KE
        end if

    end do
   close(output_unit_position)
   close(kinetic_unit_position)


end program simulator_fortran