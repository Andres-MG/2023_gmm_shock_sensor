import json
import seaborn as sns
from matplotlib import pyplot as plt

# Process data
# ------------
with open("benchmark.json") as file:
    data = json.load(file)

timings = {}
for model in data:
    procs = []
    threads = []
    cost = []

    for bench in data[model]:
        procs.append(bench["procs"])
        threads.append(bench["threads"])
        cost.append(bench["sensor"] / bench["iteration"] * 100.0)

        timings[model] = {
            "procs": procs,
            "threads": threads,
            "cost": cost,
        }

# Plot GMM sensor performance
# ---------------------------
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 30

plt.figure(figsize=(10, 8))
sns.barplot(
    data=timings['GMM'],
    x="procs",
    y="cost",
    hue="threads",
    palette=['lightgray', 'darkgray', 'gray'] * 3,
)
plt.legend().remove()
plt.xlabel("Number of processes")
plt.ylabel("Relative cost of the sensor (\\%)")

plt.gcf().tight_layout()
plt.savefig("benchmark.png", dpi=500)
plt.show()

# Table of relative costs
# -----------------------
with open("benchmark.tex", "w") as file:
    file.write("\\documentclass{standalone}\n\n")
    file.write("\\begin{document}\n\n")

    file.write("\\begin{tabular}{lccc|ccc|ccc}\n")
    file.write(
        "     & " +
        "\\multicolumn{3}{c|}{1 process} & " +
        "\\multicolumn{3}{c|}{10 processes} & " +
        "\\multicolumn{3}{c}{20 processes} \\\\\n"
    )
    file.write("    \\cline{2-10}\n")
    file.write(
        "     & " +
        "1 thread & 2 threads & 4 threads & " +
        "1 thread & 2 threads & 4 threads & " +
        "1 thread & 2 threads & 4 threads \\\\\n"
    )
    file.write("    \\hline\n")
    for model in timings:
        file.write(
            "    " + model + " & " +
            " & ".join([f"{cost:.2f}" for cost in timings[model]['cost']]) +
            " \\\\\n"
        )
    file.write("\\end{tabular}\n\n")
    file.write("\\end{document}\n")
