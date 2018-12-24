import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
properties_data = pd.read_csv("Properties.csv")

corr = properties_data.corr()
cols = corr.columns
print cols

plt.rcParams['figure.figsize'] = [16, 6]
fig, ax = plt.subplots(nrows=1, ncols=len(cols))

ax=ax.flatten()
j=0
for ind, i in enumerate(ax):
  i.scatter(corr[cols[j]], corr[cols[ind]],  alpha=0.5)
  i.set_xlabel(cols[j])
  j+=1
plt.show()