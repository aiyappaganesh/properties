import pandas as pd
import numpy as np
from scipy import linalg
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

accounts_df = pd.read_csv("Accounts.csv").select_dtypes(include=[np.number])
accounts_df_num = np.nan_to_num(accounts_df)
accounts_df_num_scaled = scale(accounts_df_num)
u, s, v = linalg.svd(accounts_df_num_scaled)
s = s / np.sum(s)
plt.step(np.arange(s.size), np.cumsum(s))
plt.savefig('./skreeacc.png')
T = np.matmul(accounts_df_num_scaled, np.transpose(v[:2]))

axes_lim = [-2.0, 2.0]
ax = plt.axes()
ax.grid(True)
ax.scatter(T[:,[0]], T[:,[1]])
plt.savefig('./projectionsacc.png')
plt.show()