import numpy as np
import pandas as pd

# Read data ([SET] the correct file name)
# ---------------------------------------
data_set = pd.read_csv('Viscous_divv.tec', delimiter='\s+',skiprows=3)
data_set = pd.DataFrame(data_set)
data_set.columns = [
    'x', 'y', 'z', 'divV', 'u', 'v', 'p_x', 'p_y', 'rho', 'p', 'eID'
]

# Delete 'ZONES'
data_set = data_set[~data_set['x'].str.contains('zone', case=False)]
data_set = data_set.astype('float64')

# Feature Space
# -------------
divv2 = data_set['divV']**2
grad2_p = data_set['p_x']**2 + data_set['p_y']**2
grad_p_mag = np.sqrt(grad2_p)
np_x = data_set['p_x'] / grad_p_mag
np_y = data_set['p_y'] / grad_p_mag

a = np.sqrt(1.4 * data_set['p'] / data_set['rho'])
m_n = (data_set['u'] * np_x + data_set['v'] * np_y) / a

mach_1 = np.sqrt(data_set['u']**2 + data_set['v']**2) / a - 1
supersonic = np.maximum(0, mach_1)

# [SET] the variables to be used in the feature space
data = pd.DataFrame({
    'divv2': divv2,
    'grad2_p': grad2_p,
    # 'm_n': m_n,
    # 'supersonic': supersonic,
})

# Data normalization
# ------------------
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data.values)
normalized_data = pd.DataFrame(normalized_data, columns=data.columns)

# Gaussian mixture
# ----------------
from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(
    n_components=6,     # [SET] the number of clusters
    tol=0.001,
    reg_covar=1e-6,
    max_iter=100,
    verbose=True,
    init_params='kmeans',
).fit(normalized_data)

clusters = gmm.predict(normalized_data)

# Sort clusters
cluster_map = np.argsort(np.sum(gmm.means_**2, axis=1))

# New idea!! ------------------------------------------------------------------
# centroids = np.zeros((gmm.n_components, 2))
# for i in range(gmm.n_components):
#     mask = clusters == i
#     npts = data.loc[mask, :].shape[0]
#     centroids[i, :] = data.loc[mask, :].sum() / npts
# cluster_map = np.argsort(np.sum(centroids**2, axis=1))
# New idea!! ------------------------------------------------------------------

clusters = np.array(list(map(lambda i: cluster_map[i], clusters)))

# Plot feature space in each cluster
# ----------------------------------
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 24

# List of colors for each cluster
colors = ['#2D003C', '#FFC0CB', '#87CEEB', '#FF69B4', '#C934C3', 'b']
plt.figure(figsize=(10, 8))

# Plot data points for each cluster with different colors
for i in range(gmm.n_components):
    subset = data.loc[clusters == i, :]
    plt.scatter(
        subset['grad2_p'],  # [SET] the variables of the feature space
        subset['divv2'],
        label=f'Cluster {i + 1}',
        color=colors[i],
    )

plt.ticklabel_format(style='sci', scilimits=(-3,4))

# [SET] the x label
plt.xlabel(r'$\lVert\nabla p\rVert^2$')     # |grad p|^2
# plt.xlabel(r'$\vec{v}\cdot \vec n_p / a$')  # v * np / a
# plt.xlabel(r'$\max(0, M-1)$')                # max(0, M - 1)
# plt.xlabel(r'$(\nabla \cdot \vec v)^{2}$')  # div v

plt.ylabel(r'$(\nabla\cdot\vec{v})^2$')     # div v
plt.legend()

plt.gcf().tight_layout()
plt.savefig('features.png', dpi=300)

# Plot performance metrics
# ------------------------
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 22

# Initialize lists to store the values of the performance metrics for each value of k
aic_values = []
bic_values = []

# Iterate over k in [1, 6] clusters
for k in range(1, 7):
    gmm = GaussianMixture(
        n_components=k,
        tol=0.001,
        reg_covar=1e-6,
        max_iter=100,
        verbose=True,
        init_params='kmeans',
    )
    gmm.fit(normalized_data)

    # Compute the performance metrics (AIC and BIC)
    aic_values.append(gmm.aic(normalized_data))
    bic_values.append(gmm.bic(normalized_data))

# Plot BIC
plt.figure(figsize=(10, 8))
plt.plot(range(1, 7), bic_values,'black', linewidth=2.5)
plt.xlabel(r'Number of clusters')
plt.ylabel(r'BIC Performance Metric')

plt.gcf().tight_layout()
plt.savefig('bic_6.png', bbox_inches='tight', dpi=300, pad_inches = 0)

# AIC and BID table
# -----------------
df = pd.DataFrame({
    '\# of clusters': range(1, 7),
    'AIC': aic_values,
    'BIC': bic_values,
})

# Convert the DataFrame to LaTeX format
table_latex = df.style.hide(axis='index').to_latex()

# Write the LaTeX code to a .tex file
with open('table.tex', 'w') as f:
    f.write(table_latex)