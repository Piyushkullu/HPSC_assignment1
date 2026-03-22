output.txt : output_file_generator.exe
            ./output_file_generator.exe > output.txt
output_file_generator.exe : output_file_generator.o simulator.o cal_force.o updater_function.o constants.o
                            gfortran output_file_generator.o simulator.o cal_force.o updater_function.o constants.o -o output_file_generator.exe
output_file_generator.o : output_file_generator.f90
                            gfortran -c output_file_generator.f90
cal_force.o : cal_force.f90
            gfortran -c cal_force.f90
updater_function.o : updater_function.f90
            gfortran -c updater_function.f90
constants.o : constants.f90
                gfortran -c constants.f90