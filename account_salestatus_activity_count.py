import pandas as pd
import numpy as np
from scipy import linalg
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

properties_df = pd.read_csv("Properties.csv")
property_to_account_df = pd.read_csv("Accounts_properties.csv")
accounts_df = pd.read_csv("Accounts.csv")
property_account_join = property_to_account_df.join(properties_df.set_index('id_props'), on='id_props', rsuffix='_prop')
property_account_join = property_account_join.join(accounts_df.set_index('id_accs'), on='id_accs', rsuffix='_acc')
property_account_join = property_account_join.dropna()
accs = np.unique(property_account_join['id_accs'].values)
accs_data = []
for acc in accs:
	acc_props = property_account_join.loc[property_account_join['id_accs'].isin([acc])]
	unique, counts = np.unique(acc_props['sale_status'], return_counts=True)
	data_dict = dict(zip(unique, counts))
	data_dict['id'] = acc
	data_dict['activity_count'] = np.unique(acc_props['activity_count'])[0]
	accs_data.append(data_dict)
accs_df = pd.DataFrame(accs_data)
accs_df = accs_df.dropna()
cmap = plt.cm.rainbow
values = accs_df['Y'].values
norm = matplotlib.colors.Normalize(vmin=np.amin(values), vmax=np.amax(values))
color = cmap(norm(values))
fig, ax = plt.subplots()
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm)
ax.grid(True)
print np.amax(values)
print np.amax(accs_df['activity_count'].values)
ax.scatter(values, accs_df['activity_count'].values, color=color)
plt.show()