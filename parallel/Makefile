
FC = gfortran
# -O3 : Max optimization (Crucial for profiling real performance)
# -g  : Debug symbols (Lets gprof see your subroutine names)
# -pg : Enables profiling
# -fopenmp : Enables parallel threads
FCFLAGS = -O3 -fopenmp 

simulation.xyz : simulator_fortran.exe 
	./simulator_fortran.exe

simulator_fortran.exe : constants.o output_file_generator.o calc_force.o updater_function.o kinetic_energy_sub.o simulator_fortran.o
	$(FC) $(FCFLAGS) constants.o output_file_generator.o calc_force.o updater_function.o kinetic_energy_sub.o simulator_fortran.o -o simulator_fortran.exe

constants.o : constants.f90
	$(FC) $(FCFLAGS) -c constants.f90

output_file_generator.o : output_file_generator.f90
	$(FC) $(FCFLAGS) -c output_file_generator.f90

calc_force.o : calc_force.f90
	$(FC) $(FCFLAGS) -c calc_force.f90

updater_function.o : updater_function.f90
	$(FC) $(FCFLAGS) -c updater_function.f90

kinetic_energy_sub.o : kinetic_energy_sub.f90
	$(FC) $(FCFLAGS) -c kinetic_energy_sub.f90

simulator_fortran.o : simulator_fortran.f90
	$(FC) $(FCFLAGS) -c simulator_fortran.f90

clean :
	rm -f *.o *.png *.mod simulator_fortran.exe simulation.xyz kinetic.txt gmon.out profile_results.txt

PYTHON = ../simulator/bin/python3
kinetic:
	$(PYTHON) kinetic_energy.py
	@echo "--- Done plotting kinetic kinetic_energy ---"

free_fall:
	@echo "--- Swapping to Free Fall Constants ---"
	cp free_fall_constants.f90 constants.f90
	@echo "--- Recompiling ---"
	$(MAKE) clean
	$(MAKE) simulation.xyz
	@echo "--- Generating Plot ---"
	$(PYTHON) plot_free_fall.py
	@echo "--- Done! Check free_fall_plot.png ---"