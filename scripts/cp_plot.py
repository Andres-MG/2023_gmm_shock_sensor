import pandas as pd
import matplotlib.pyplot as plt

ref_file = "../sims/Cylinder_viscous/NACA_report_Cp.csv"
ref_color = "grey"

sim_files = [
    "gmm_gradp_divv/RESULTS_avg/Cylinder.stats.0000400000_cp.csv",
    "integral_gradp/RESULTS_avg/Cylinder.stats.0000400000_cp.csv",
    "modal_rhop/RESULTS_avg/Cylinder.stats.0000400000_cp.csv",
]
sim_files = ["../sims/Cylinder_viscous/" + file for file in sim_files]

sim_labels = [
    "Modal",
    "Integral",
    "GMM",
]

sim_colors = [
    "blue",
    "green",
    "red",
]

ref_df = pd.read_csv(ref_file)
sim_dfs = [pd.read_csv(file).sort_values(by=["Angle"]) for file in sim_files]

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 28

plt.figure(figsize=(10, 8))
for df, label, color in zip(sim_dfs, sim_labels, sim_colors):
    plt.plot(
        abs(df["Angle"]),
        df["Cp"],
        linewidth=3,
        color=color,
        label=label,
    )
plt.scatter(
    ref_df["Angle"],
    ref_df["Cp"],
    marker="s",
    sizes=[150],
    color="grey",
    edgecolor="black",
    label="Experiment",
    zorder=10,
)
plt.xlabel("Angle (deg)")
plt.ylabel(r"$C_p$")
plt.xlim([-0, 180])
plt.ylim([-0.5, 2.0])
plt.xticks([0, 30, 60, 90, 120, 150, 180])
plt.grid()
plt.legend()

plt.gcf().tight_layout()
plt.savefig("cp.png", dpi=500)
plt.show()
