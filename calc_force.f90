subroutine cal_force(pos,vel,force)
        use constants
        implicit none
        real(kind = 8), dimension(3,N), intent(in) :: pos
        real(kind = 8), dimension(3,N), intent(in) :: vel
        real(kind = 8), dimension(3,N), intent(out) :: force
        real(kind = 8) :: dij,delta,spring_force_particle,spring_force_wall,rel_vel_to_wall,v_approach
        real(kind = 8), dimension(3) :: rij,rij_unit
        force(3,:) = -mass*g
        do particle = 1,N
            ! wall force computation
            do co_ord =1,3
                d = pos(co_ord,particle)
                rel_vel_to_wall = vel(co_ord,particle)
                if (d>=radius .and. d<=L(co_ord)-radius) then
                    cycle ! skip if the particle is not touching walls
                else if (d <= radius) then
                    spring_force_wall = spring_constant_wall*abs(d-radius)
            
                else if (d>= L(co_ord)-radius) then
                    spring_force_wall = -spring_constant_wall*abs(d-L(co_ord)+radius)
                end if
                damping_force_wall = -damping_wall*rel_vel_to_wall
                force(co_ord,particle) = force(co_ord,particle) +spring_force_wall + damping_force_wall
            end do
            do another_particle = particle+1,N:
                rij = pos(:,another_particle)-pos(:,particle)! position of J th wrt i th particle
                dij = norm2(rij)
                rij_unit = rij/dij
                delta = 2*radius - dij
                if (delta <0) then
                    cycle
                else
                    spring_force_particle = spring_constant_particle*delta
                end if 
                v_approach = dot_product(vel(:,particle),rij_unit)+dot_product(vel(:,another_particle),-rij_unit)
                damping_force_particle = damping_particle*v_approach
                net_force = spring_force_particle*(-rij_unit) +damping_force_particle*(-rij_unit) 
                force(:,particle) = force(:,particle)+ net_force
                force(:,another_particle) = force(:,another_particle)-net_force
        end do
end subroutine cal_force
