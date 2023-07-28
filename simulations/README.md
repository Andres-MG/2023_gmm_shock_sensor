# Simulations

In this folder we include the configuration files to run the simulations of section VI A and VI B,
together with the final results that we used in the article.
The files named `Cylinder.control` run the cases during 300,000 iterations, and the ones with
name `Cylinder_avg.control` restart from the solution at step 300,000 to compute the average field
over another 100,000 iterations.

The code of the solver is in the branch
[research/2023_andres_gmm](https://github.com/loganoz/horses3d/tree/research/2023_andres_gmm) of
the software HORESES3D.

To perform the simulations, move to the directory of the specific case to be computed, copy or
create a link to the folder `MESH/`, and run the HORSES3D executable including the control file.

---

The file `postprocess.control` contains the commands to run `horses2plt` and obtain the files
required for postprocessing with the scripts of the folder `scripts/`. Depending on the task,
uncomment the indicated lines and execute `horses2plt` with this file as an argument.