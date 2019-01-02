import pandas as pd
import numpy as np
from scipy import linalg
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

properties_df = pd.read_csv("Properties.csv")
property_to_account_df = pd.read_csv("Accounts_properties.csv")
property_account_join = property_to_account_df.join(properties_df.set_index('id_props'), on='id_props', rsuffix='_prop')
property_account_join = property_account_join.dropna()
acc_props = property_account_join.loc[property_account_join['id_accs'].isin(['0012A000023XldlQAC', '0012A000023XqaxQAC'])]
properties_df_rank = acc_props.rank()
cmap = plt.cm.rainbow
print np.unique(properties_df['num_parking_spaces'].values)
print np.unique(properties_df_rank['num_parking_spaces'].values)
values = np.nan_to_num(properties_df_rank['num_parking_spaces'].values)
print np.unique(values)
print np.mean(values)
norm = matplotlib.colors.Normalize(vmin=np.amin(values), vmax=np.amax(values))
color = cmap(norm(values))
u, s, v = linalg.svd(properties_df_rank)
s = s / np.sum(s)
T = np.matmul(properties_df_rank, np.transpose(v[:2]))
fig, ax = plt.subplots()
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm)
ax.grid(True)
ax.scatter(T[:,[0]], T[:,[1]], color=color)
plt.show()