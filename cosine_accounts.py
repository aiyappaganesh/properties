import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import scale

accounts_df = pd.read_csv("Accounts.csv").select_dtypes(include=[np.number])
accounts_df_num = np.nan_to_num(accounts_df)
# print accounts_df_num[:10]
accounts_df_num_scaled = scale(accounts_df_num)
# print accounts_df_num_scaled[:10]
corr = cosine_similarity(accounts_df_num_scaled)
# for index1, account1 in enumerate(accounts_df_num[:10]):
# 	for index2, account2 in enumerate(accounts_df_num[10:20]):
# 		if corr[index1][index2] >= 0.9:
# 			print account1
# 			print account2
# 			print corr[index1][index2]

fig, ax = plt.subplots()
im = ax.imshow(corr)
fig.colorbar(im)
plt.show()