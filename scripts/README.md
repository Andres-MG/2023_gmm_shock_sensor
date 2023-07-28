# Scripts

These files generate the plots of figure 6 (Cp), figures 10-13 (BIC, feature space and nodal
sensor) and figure 14 (computational cost):

* cp_plot.py

* statistics.py

* benchmark.py

The auxiliary files for ParaView:

* cp.pvsm

* cp.pwin

generate the data to make the Cp plot. Open `cp.pvsm` with ParaView and save the spreadsheet as a
CSV file. `cp_plot.py` uses these CSV files to create the plot.

The files:

* sims.pwin

* view.pvcvbc

can be read from ParaView to replicate the window layout and camera setup that generate the
flow-field and sensor plots that we include in sections VI A and VI B.
