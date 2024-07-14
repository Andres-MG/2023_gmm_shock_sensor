# Scripts

These files generate the plots of figure 10 (Cp), figures 15&ndash;17 (BIC and feature spaces),
tables 4 (AIC and BIC) and 5 (performance), and figure 18 (computational cost):

* cp_plot.py

* statistics.py

* benchmark.py

The auxiliary file `cp.pvsm` can be opened from ParaView to generate the data of the Cp plot as a
CSV file. `cp_plot.py` uses this CSV file to create the plot.
Files with extension `.pwin` contain ParaView layouts, and `view.pvcvbc` includes camera settings.
These are the parameters used to export the figures shown in the article.
