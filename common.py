import csv
from sets import Set

account_properties = []
account_properties_deals = Set()
account_properties_properties = Set()
account_properties_accounts = Set()
with open('Accounts_properties.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    for row in csv_reader:
        if line_count == 0:
            columns = row
            line_count += 1
        else:
            account_property = {}
            for idx, column in enumerate(columns):
                account_property[column] = row[idx]
                if column == 'id_deals':
                    account_properties_deals.add(row[idx])
                if column == 'id_props':
                    account_properties_properties.add(row[idx])
                if column == 'id_accs':
                    account_properties_accounts.add(row[idx])
            account_properties.append(account_property)
            line_count += 1
print('account_properties deals', len(account_properties_deals))
print('account_properties properties', len(account_properties_properties))
print('account_properties accounts', len(account_properties_accounts))

opportunities = []
opportunities_deals = Set()
opportunities_accounts = Set()
with open('Opportunities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    for row in csv_reader:
        if line_count == 0:
            columns = row
            line_count += 1
        else:
            opportunity = {}
            for idx, column in enumerate(columns):
                opportunity[column] = row[idx]
                if column == 'id_deals':
                    opportunities_deals.add(row[idx])
                if column == 'id_accs':
                    opportunities_accounts.add(row[idx])
            opportunities.append(opportunity)
            line_count += 1
print('opportunities deals', len(opportunities_deals))
print('opportunities accounts', len(opportunities_accounts))

properties = []
properties_deals = Set()
properties_properties = Set()
with open('Properties.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    for row in csv_reader:
        if line_count == 0:
            columns = row
            line_count += 1
        else:
            property = {}
            for idx, column in enumerate(columns):
                property[column] = row[idx]
                if column == 'id_deals':
                    properties_deals.add(row[idx])
                if column == 'id_props':
                    properties_properties.add(row[idx])
            properties.append(property)
            line_count += 1
print('properties deals', len(properties_deals))
print('properties properties', len(properties_properties))

deals_properties = []
deals_properties_deals = Set()
deals_properties_properties = Set()
with open('Deals_to_Properties.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    for row in csv_reader:
        if line_count == 0:
            columns = row
            line_count += 1
        else:
            deal_property = {}
            for idx, column in enumerate(columns):
                deal_property[column] = row[idx]
                if column == 'id_deals':
                    deals_properties_deals.add(row[idx])
                if column == 'id_props':
                    deals_properties_properties.add(row[idx])
            deals_properties.append(deal_property)
            line_count += 1
print('deals_properties deals', len(deals_properties_deals))
print('deals_properties properties', len(deals_properties_properties))

accounts = []
accounts_accounts = Set()
with open('Accounts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    for row in csv_reader:
        if line_count == 0:
            columns = row
            line_count += 1
        else:
            account = {}
            for idx, column in enumerate(columns):
                account[column] = row[idx]
                if column == 'id_accs':
                    accounts_accounts.add(row[idx])
            accounts.append(account_property)
            line_count += 1
print('accounts accounts', len(accounts_accounts))

deals_union = account_properties_deals | opportunities_deals | properties_deals | deals_properties_deals
print('all deals', len(deals_union))

properties_union = account_properties_properties | properties_properties | deals_properties_properties
print('all properties', len(properties_union))

accounts_union = account_properties_accounts | opportunities_accounts | accounts_accounts
print('all accounts', len(accounts_union))

common_account_properties_opportunities = account_properties_deals.intersection(opportunities_deals)
print('common deals account_properties & opportunities', len(common_account_properties_opportunities))

common_account_properties_properties = account_properties_deals.intersection(properties_deals)
print('common deals account_properties & properties', len(common_account_properties_properties))

common_account_properties_deals_properties = account_properties_deals.intersection(deals_properties_deals)
print('common deals account_properties & deals_properties', len(common_account_properties_deals_properties))

common_opportunities_properties = opportunities_deals.intersection(properties_deals)
print('common deals opportunities & properties', len(common_opportunities_properties))

common_opportunities_deals_properties = opportunities_deals.intersection(deals_properties_deals)
print('common deals opportunities & deals_properties', len(common_opportunities_deals_properties))

common_properties_deals_properties = properties_deals.intersection(deals_properties_deals)
print('common deals properties & deals_properties', len(common_properties_deals_properties))

common_account_properties_properties_p = account_properties_properties.intersection(properties_properties)
print('common properties account_properties & properties', len(common_account_properties_properties_p))

common_account_properties_deals_properties_p = account_properties_properties.intersection(deals_properties_properties)
print('common properties account_properties & deals_properties', len(common_account_properties_deals_properties_p))

common_properties_deals_properties_p = properties_properties.intersection(deals_properties_properties)
print('common properties properties & deals_properties', len(common_properties_deals_properties_p))

common_account_properties_opportunities_a = account_properties_accounts.intersection(opportunities_accounts)
print('common accounts account_properties & opportunities', len(common_account_properties_opportunities_a))

common_account_properties_accounts_a = account_properties_accounts.intersection(accounts_accounts)
print('common accounts account_properties & accounts', len(common_account_properties_accounts_a))

common_opportunities_accounts_a = opportunities_accounts.intersection(accounts_accounts)
print('common accounts opportunities_accounts & accounts', len(common_opportunities_accounts_a))

