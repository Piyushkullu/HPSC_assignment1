subroutine output_file_generator(pos, t)
    use constants
    implicit none
    
    real(kind=wp), dimension(3, N), intent(in) :: pos
    real(kind=wp), intent(in) :: t
    integer :: i
    
    ! 1. Open the file on Unit 10. 
    ! 'position="append"' ensures we add new frames to the bottom of the file
    open(unit=10, file="simulation.xyz", position="append", status="unknown")
    
    ! 2. Line 1: Number of atoms
    write(10, *) N
    
    ! 3. Line 2: Comment line (Time step)
   ! Write the Extended XYZ comment line using your dynamic box dimensions
    write(10, *) 'Lattice="', L(1), ' 0.0 0.0 0.0 ', L(2), ' 0.0 0.0 0.0 ', L(3), '" Time=', t
    
    ! 4. Lines 3 to N+2: Atom type and coordinates
    do i = 1, N
        ! We write "C" just to give it a generic atom name for OVITO
        write(10, *) "C", pos(1, i), pos(2, i), pos(3, i)
    end do
    
    ! 5. Close the file so the OS can save it safely
    close(10)

end subroutine output_file_generator