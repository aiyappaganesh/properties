import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import itertools

properties_df = pd.read_csv("Properties.csv")
accounts_df = pd.read_csv("Accounts.csv")
property_to_account_df = pd.read_csv("Accounts_properties.csv") #(70350, 4)
id_to_data = {
	'id_accs': {
		'df': accounts_df,
		'map': accounts_df.set_index('id_accs').T.to_dict()
	},
	'id_props': {
		'df': properties_df,
		'map': properties_df.set_index('id_props').T.to_dict()
	}
}

property_join = property_to_account_df.join(properties_df.set_index('id_props'), on='id_props', rsuffix='_prop')
final_join = property_join.join(accounts_df.set_index('id_accs'), on='id_accs', rsuffix='_acc')

def get_non_numeric_cols(df):
	return df.select_dtypes(exclude=[np.number]).columns.tolist()

def get_cols(df):
	return df.columns.tolist()

def get_col_permutations(dfs):
	cols1 = get_cols(dfs[0])
	cols2 = get_cols(dfs[1])
	product = itertools.product(cols1, cols2)
	perms = {}
	for (left, right) in product:
		if left in perms:
			perms[left].append(right)
		else:
			perms[left] = [right]
	return perms


perms = get_col_permutations([properties_df, accounts_df])
heatmap = np.empty([len(perms) ,20])
non_numeric_cols1 = get_non_numeric_cols(properties_df)
non_numeric_cols2 = get_non_numeric_cols(accounts_df)
non_numeric_cols = non_numeric_cols1 + non_numeric_cols2
for left_idx, (left, arr) in enumerate(perms.iteritems()):
	for right_idx, right in enumerate(arr):
		dfl = final_join[left]
		if left in non_numeric_cols:
			dfl = dfl.rank()
		dfr = final_join[right]
		if right in non_numeric_cols:
			dfr = dfr.rank()
		corr = dfl.corr(dfr, method='spearman')
		heatmap[left_idx][right_idx] = corr

fig, ax = plt.subplots()
im = ax.imshow(heatmap)
fig.colorbar(im)
plt.show()