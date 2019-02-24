import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fund = pd.read_csv('fund_20190223.csv', encoding='GBK',dtype={'Net_value': np.float64,
                                                                                     'Gross_value': np.float64,
                                                                                     'Day_rate': np.float64,
                                                                                     'One_week': np.float64,
                                                                                     'One_month': np.float64,
                                                                                     'Three_month': np.float64,
                                                                                     'Six_month': np.float64,
                                                                                     'One_year': np.float64,
                                                                                     'Two_year': np.float64,
                                                                                     'Three_year': np.float64,
                                                                                     'From_this_y': np.float64,
                                                                                     'From_establish': np.float64},
                   parse_dates=['Establish_date'])

fund['Establish_rate'] = fund['From_establish'] / 100

net = fund.sort_values(by='Net_value', ascending=False)

gross = fund.sort_values(by='Gross_value', ascending=False)

profit = fund.sort_values(by='Establish_rate', ascending=False)

top_20_net = net.iloc[0:20]

top_20_gross = gross.iloc[0:20]

top_20_profit = profit.iloc[0:20]

# Visualization Part
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sns.barplot(x='Net_value', y='Name', data=top_20_net)

sns.barplot(x='Gross_value', y='Name', data=top_20_gross)

sns.barplot(x='Establish_rate', y='Name', data=top_20_profit)

# sns.scatterplot(x='Net_value', y='Name', data=fund)
