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
! subroutine updater_function(pos,vel,force)
!     use constants
!     implicit none
!     real(kind = wp), dimension(3,N), intent(inout) :: pos, vel, force
!     integer :: i
!     !$omp do
!     do i = 1, N
!         pos(:, i) = pos(:, i) + vel(:, i) * dt
!         vel(:, i) = vel(:, i) + (force(:, i) / mass) * dt
!     end do
!     !$omp end do 
!     call calc_force(pos,vel,force)

! end subroutine updater_function