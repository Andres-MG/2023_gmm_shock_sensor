# Simulations

In this folder we include the configuration files to run the simulations of the results secion (VI)
and appendix C.

The code of the solver is in the branch
[research/2023_andres_gmm](https://github.com/loganoz/horses3d/tree/research/2023_andres_gmm) of
the software HORESES3D.

To perform the simulations, move to the directory of the specific case to be computed, copy or
create a link to the folder `MESH/`, and create a folder to store the results. The name of this
folder is specified in the control file of each simulation (solution file name).

---

The file `postprocess.control` contains the commands to run `horses2plt` and obtain the files
required for post-processing with the scripts of the folder `scripts/`. Depending on the task,
uncomment the indicated lines and execute `horses2plt` with this file as an argument.
