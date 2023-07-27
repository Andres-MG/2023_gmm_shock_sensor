import json
import seaborn as sns
from matplotlib import pyplot as plt

bench_file = "../simulations/viscous/gmm_gradp_divv/benchmark.json"
with open(bench_file) as file:
    data = json.load(file)

timings = {
    "procs": [],
    "threads": [],
    "cost": [],
}
for bench in data["Benchmarks"]:
    timings["procs"].append(bench["procs"])
    timings["threads"].append(bench["threads"])
    timings["cost"].append(
        bench["sensor"] / bench["iteration"] * 100.0
    )

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 30

plt.figure(figsize=(10, 8))
sns.barplot(
    data=timings,
    x="procs",
    y="cost",
    hue="threads",
)
plt.legend().remove()
plt.xlabel("Number of processes")
plt.ylabel("Relative cost of the sensor (\\%)")

plt.gcf().tight_layout()
plt.savefig("benchmark.png", dpi=500)
plt.show()
