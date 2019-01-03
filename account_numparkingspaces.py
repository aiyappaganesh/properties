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
accs = np.unique(property_account_join['id_accs'].values)
accs_data = []
for acc in accs:
	acc_props = property_account_join.loc[property_account_join['id_accs'].isin([acc])]
	average = np.average(acc_props['num_parking_spaces'])
	accs_data.append({'id': acc, 'num_parking_spaces_avg': average})
accs_df = pd.DataFrame(accs_data)
accs_df_rank = accs_df.rank()
cmap = plt.cm.rainbow
print np.unique(accs_df['num_parking_spaces_avg'].values)
print np.unique(accs_df_rank['num_parking_spaces_avg'].values)
values = accs_df['num_parking_spaces_avg'].values
norm = matplotlib.colors.Normalize(vmin=np.amin(values), vmax=np.amax(values))
color = cmap(norm(values))
# u, s, v = linalg.svd(accs_df_rank)
# s = s / np.sum(s)
# T = np.matmul(accs_df_rank, np.transpose(v[:2]))
fig, ax = plt.subplots()
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm)
ax.grid(True)
# ax.scatter(T[:,[0]], T[:,[1]], color=color)
print np.amax(accs_df_rank['num_parking_spaces_avg'])
ax.scatter(accs_df_rank['id'], accs_df_rank['num_parking_spaces_avg'], color=color)
plt.show()