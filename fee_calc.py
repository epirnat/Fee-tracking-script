import pandas as pd
df = pd.read_csv('transcations_data.csv')

df['change'] = df['fee'].diff()

df_filtered = df[df['change'] != 0].to_csv('change_in_fees.csv', index=False)