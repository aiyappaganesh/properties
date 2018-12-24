import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

props_data = pd.read_csv("Properties.csv")
accs_props_data = pd.read_csv("Accounts_properties.csv")
accs_data = pd.read_csv("Accounts.csv")

accs_props = props_data.merge(accs_props_data, on='id_props')
accs_props_merged = accs_props.merge(accs_data, on='id_accs')

corr = accs_props_merged.corr()
cols = corr.columns

for i in range(len(cols)):
	for j in range(len(cols)):
		if abs(corr[cols[i]][cols[j]]) > 0.5 and abs(corr[cols[i]][cols[j]]) < 1:
			print cols[i], cols[j], corr[cols[i]][cols[j]]

plt.matshow(corr)
plt.show()