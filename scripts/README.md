# Scripts

These files generate the plots of figure 9 (Cp), figures 13&ndash;15 (BIC and feature spaces),
table IV (AIC and BIC), and figure 16 (computational cost):

* cp_plot.py

* statistics.py

* benchmark.py

The auxiliary file `cp.pvsm` can be opened from ParaView to generate the data of the Cp plot as a
CSV file. `cp_plot.py` uses this CSV file to create the plot.
Files with extension `.pwin` contain ParaView layouts, and `view.pvcvbc` includes camera settings.
These are the parameters used to export the figures shown in the article.
