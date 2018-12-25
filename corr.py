import pandas as pd
import numpy as np
import itertools
import math

properties_df = pd.read_csv("Properties.csv")
accounts_df = pd.read_csv("Accounts.csv")

properties_map = properties_df.set_index('id_props').T.to_dict()
accounts_map = accounts_df.set_index('id_accs').T.to_dict()
property_to_account = pd.read_csv("Accounts_properties.csv")

accounts = []
properties = []

def extract(col_name, map, row):
    id = row[col_name]
    if id in map:
        return map[id]
    return None

for index, row in property_to_account.iterrows():
    if index < 2:
        accounts.append(extract('id_accs', accounts_map, row))
        properties.append(extract('id_props', properties_map, row))

# print accounts[:1]

accs_df = pd.DataFrame(accounts)
props_df = pd.DataFrame(properties)

def get_numeric_cols(df):
    return df.select_dtypes(include=[np.number]).columns.tolist()

def get_col_permutations(dfs):
    numeric_cols1 = get_numeric_cols(dfs[0])
    numeric_cols2 = get_numeric_cols(dfs[1])
    return itertools.product(numeric_cols1, numeric_cols2)

def get_col_index(col_name, frame):
    return list(frame.columns.values).index(col_name)

perms = get_col_permutations([properties_df, accounts_df])
for perm in perms:
    prop_col = perm[0]
    acc_col = perm[1]
    # print prop_col, acc_col
    prop_col_ind = get_col_index(prop_col, properties_df)
    acc_col_ind = get_col_index(acc_col, accounts_df)
    # print prop_col_ind, acc_col_ind
    acol = accs_df[acc_col]
    pcol = props_df[prop_col]
    product = np.multiply(pcol, acol)
    print 'product', product
    product_sum = np.sum(product)
    print 'product_sum', product_sum
    props_mean = np.mean(pcol)
    print 'props_mean', props_mean
    accs_mean = np.mean(acol)
    print 'accs_mean', accs_mean
    numerator = product_sum - (len(pcol)*props_mean*accs_mean)
    print 'numerator', numerator
    props_sq = np.square(pcol)
    props_sq_sum = np.sum(props_sq)
    accs_sq = np.square(acol)
    accs_sq_sum = np.sum(accs_sq)
    props_sqrt = math.sqrt(props_sq_sum - (len(pcol)*props_mean**2))
    accs_sqrt = math.sqrt(accs_sq_sum - (len(acol)*accs_mean**2))
    denominator = props_sqrt * accs_sqrt
    print 'denominator', denominator
    corr = numerator/denominator
    print 'corr', corr
