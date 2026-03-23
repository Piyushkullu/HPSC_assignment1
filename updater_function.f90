!Updater function definition ####

subroutine updater_function(pos,vel,force)
    use constants
    implicit none
    real(kind = wp), dimension(3,N), intent(inout) :: pos, vel, force
    pos = pos + vel*dt
    vel = vel + (force/mass)*dt
    !### updating force ###
    call calc_force(pos,vel,force)
end subroutine updater_function