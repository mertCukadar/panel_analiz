import pandas as pd


data_g7 = pd.read_csv('g7.csv')
data_e7 = pd.read_csv('e7.csv')

columns_g7 = {
    'Year': 'year',
    'Country': 'country',
    'Inflation Rate (%)': 'inflation_rate',
    'Foreign direct inflows, net (BoP, current US$)': 'fdi_inflows',
    'GDP (current US$)': 'gdp',
    'Population ages 15-64 (% of total population)': 'population_15_64',
    'average_wages': 'average_wages',
    'robot': 'robots',
    'unemployment': 'unemployment'
}

columns_e7 = {
    'Year': 'year',
    'Country': 'country',
    'Inflation Rate (%)': 'inflation_rate',
    'Foreign direct investment, net inflows (BoP, current US$)': 'fdi_inflows',
    'gdp': 'gdp',
    'Population ages 65 and above (% of total population)': 'population_65_and_above',
    'average wages': 'average_wages',
    'robots': 'robots',
    'unemployment': 'unemployment'
}

data_g7 = data_g7.rename(columns={
    'Year': 'year',
    'Country': 'country',
    'Inflation Rate (%)': 'inflation_rate',
    'Foreign direct inflows, net (BoP, current US$)': 'fdi_inflows',
    'GDP (current US$)': 'gdp',
    'Population ages 15-64 (% of total population)': 'population_15_64',
    'average_wages': 'average_wages',
    'robot': 'robots',
    'unemployment': 'unemployment'
})

g7_data = data_g7[['year', 'country', 'inflation_rate', 'fdi_inflows', 'gdp', 'population_15_64', 'average_wages', 'robots', 'unemployment']]

data_e7 = data_e7.rename(columns={
    'Year': 'year',
    'Country': 'country',
    'Inflation Rate (%)': 'inflation_rate',
    'Foreign direct investment, net inflows (BoP, current US$)': 'fdi_inflows',
    'gdp': 'gdp',
    'Population ages 65 and above (% of total population)': 'population_65_and_above',
    'average wages': 'average_wages',
    'robots': 'robots',
    'unemployment': 'unemployment'
})

e7_data = data_e7[['year', 'country', 'inflation_rate', 'fdi_inflows', 'gdp', 'population_65_and_above', 'average_wages', 'robots', 'unemployment']]

# Düzenlenmiş verilerin başına bir göz atalım
print("G7 Data:")
print(g7_data.head())

print("\nE7 Data:")
print(e7_data.head())

# G7 ve E7 için temel istatistikleri hesaplayalım
g7_stats = g7_data.describe()
e7_stats = e7_data.describe()

print("G7 Basic Statistics:")
print(g7_stats)

print("\nE7 Basic Statistics:")
print(e7_stats)

# save desciptive data as excel
g7_stats.to_excel('g7_desc.xlsx')
e7_stats.to_excel('e7_desc.xlsx')

e7_data.to_excel('e7_filtered.xlsx')
g7_data.to_excel('g7_filtered.xlsx')
