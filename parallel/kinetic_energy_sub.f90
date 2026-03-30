subroutine kinetic_energy(vel,KE)
    use constants
    implicit none
    real (kind = wp), dimension(3,N), intent(in) :: vel
    real (kind = wp), intent(out) :: KE
    KE = sum(vel**2)*0.5_wp*mass
end subroutine kinetic_energy