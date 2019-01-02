import pandas as pd
import numpy as np
from scipy import linalg
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

properties_df = pd.read_csv("Properties.csv")
properties_df = properties_df.dropna()
properties_df_rank = properties_df.rank()
properties_df_num = properties_df_rank
# properties_df_num = np.nan_to_num(properties_df_rank)
# properties_df_num_scaled = scale(properties_df_num)
cmap = plt.cm.rainbow
print np.unique(properties_df['num_parking_spaces'].values)
print np.unique(properties_df_rank['num_parking_spaces'].values)
values = np.nan_to_num(properties_df_rank['num_parking_spaces'].values)
print np.unique(values)
print np.mean(values)
norm = matplotlib.colors.Normalize(vmin=np.amin(values), vmax=np.amax(values))
color = cmap(norm(values))
u, s, v = linalg.svd(properties_df_num)
s = s / np.sum(s)
T = np.matmul(properties_df_num, np.transpose(v[:2]))
fig, ax = plt.subplots()
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm)
ax.grid(True)
ax.scatter(T[:,[0]], T[:,[1]], color=color)
plt.show()