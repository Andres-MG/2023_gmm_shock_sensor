# Simulations

In this folder we include the configuration files to run the simulations of the results secion (VI)
and appendix C.

To perform the simulations, move to the directory of the specific case to be computed, copy or
create a link to the folder `MESH/`, and create a new folder to store the results. Its name is
specified in the control file of each simulation (solution file name). The double Mach reflection
and Sedov blast tests require custom initial and boundary conditions, specified in `SETUP`. Refer
to the instructions of HORSES3D in
[research/2023_andres_gmm](https://github.com/loganoz/horses3d/tree/research/2023_andres_gmm) for
more information.

The file `postprocess.control` contains the commands to run `horses2plt` and obtain the files
required for post-processing with the scripts of the folder `scripts/`. Depending on the task,
uncomment the indicated lines and execute `horses2plt` with this file as an argument.
