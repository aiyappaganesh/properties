import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import scale

properties_df = pd.read_csv("Properties.csv").select_dtypes(include=[np.number])
properties_df_num = np.nan_to_num(properties_df)
properties_df_num_scaled = scale(properties_df_num)
corr = cosine_similarity(properties_df_num_scaled)
# for index1, property1 in enumerate(properties_df_num_scaled[:10]):
# 	for index2, property2 in enumerate(properties_df_num_scaled[10:20]):
# 		if corr[index1][index2] >= 0.9:
# 			print property1
# 			print property2
# 			print corr[index1][index2]

fig, ax = plt.subplots()
im = ax.imshow(corr)
fig.colorbar(im)
plt.show()