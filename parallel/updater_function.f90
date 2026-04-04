!Updater function definition ####
subroutine updater_function(pos,vel,force)
    use constants
    implicit none
    real(kind = wp), dimension(3,N), intent(inout) :: pos, vel, force
    vel = vel + (force/mass)*dt ! for semi - implicit vel must be updated first
    pos = pos + vel*dt ! pos updated using the updated velocity
    !### updating force ###
    call calc_force(pos,vel,force)
end subroutine updater_function


!! For parallelising the pos and velocity updation negligible difference.

! subroutine updater_function(pos,vel,force)
!     use omp_lib
!     use constants
!     implicit none
!     real(kind = wp), dimension(3,N), intent(inout) :: pos, vel, force
!     integer :: i
!     !$omp parallel do private(i)
!     do i = 1, N
!         vel(:, i) = vel(:, i) + (force(:, i) / mass) * dt
!         pos(:, i) = pos(:, i) + vel(:, i) * dt
!     end do
!     !$omp end parallel do 
!     call calc_force(pos,vel,force)
! end subroutine updater_function