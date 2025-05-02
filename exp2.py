import pandas as pd

data = {
    'Year': ['2022', '2022', '2022', '2023', '2023', '2023'],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3'],
    'Region': ['Asia', 'Europe', 'Asia', 'Europe', 'Asia', 'Europe'],
    'Product': ['Laptop', 'Laptop', 'Mobile', 'Mobile', 'Laptop', 'Mobile'],
    'Sales': [200, 150, 300, 250, 400, 100]
}
df =pd.DataFrame(data)
print("Original Data:")
print(df)

slice_df = df[df['Year'] == '2023']
print("\nSlice Operation (Year = 2023):")
print(slice_df)

dice_df = df[(df['Year'].isin(['2022', '2023'])) & (df['Region'] == 'Asia')]
print("\nDice Operation (Year in ['2022', '2023'] AND Region = 'Asia'):")
print(dice_df)

rollup_df = df.groupby('Year')['Sales'].sum().reset_index()
print("\nRoll-up Operation (Sales by Year):")
print(rollup_df)

drilldown_df = df.groupby(['Year', 'Quarter'])['Sales'].sum().reset_index()
print("\nDrill-down Operation (Sales by Year and Quarter):")
print(drilldown_df)

pivot_df = pd.pivot_table(df, values='Sales', index='Product', columns='Region',
aggfunc='sum')
print("\nPivot Operation (Product vs Region):")
print(pivot_df)