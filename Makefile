simulation.xyz : simulator_fortran.exe 
	./simulator_fortran.exe

simulator_fortran.exe : constants.o output_file_generator.o calc_force.o updater_function.o simulator_fortran.o
	gfortran constants.o output_file_generator.o calc_force.o updater_function.o simulator_fortran.o -o simulator_fortran.exe

constants.o : constants.f90
	gfortran -c constants.f90

output_file_generator.o : output_file_generator.f90
	gfortran -c output_file_generator.f90

calc_force.o : calc_force.f90
	gfortran -c calc_force.f90

updater_function.o : updater_function.f90
	gfortran -c updater_function.f90

simulator_fortran.o : simulator_fortran.f90
	gfortran -c simulator_fortran.f90

clean :
	rm -f *.o *.mod simulator_fortran.exe simulation.xyz

PYTHON = ./simulator/bin/python3
free_fall:
	@echo "--- Swapping to Free Fall Constants ---"
	cp free_fall_constants.f90 constants.f90
	@echo "--- Recompiling ---"
	$(MAKE) clean
	$(MAKE) simulation.xyz
	@echo "--- Generating Plot ---"
	$(PYTHON) plot_free_fall.py
	@echo "--- Done! Check free_fall_plot.png ---"

