
import pandas as pd
df = pd.read_excel("data4.xls")
df.rename(columns={'account': 'Account Number'}, inplace=True)
df['Total'] = df['Jan'] + df['Feb'] + df['Mar']
maxdepo = df.max()
print(maxdepo)
meandepojan = df['Jan'].mean()
meandepofeb = df['Feb'].mean()
meandepomar = df['Mar'].mean()
print(df[df.Total > 300000])

# By defalut pandas converts it to dataframe
# data = pandas.read_excel("data4.xls")

# data.set_index('state', inplace=True)

# mystate = "Texas"

# # A
# print(data[["name", "Jan", "Feb", "Mar"]].query("state=='Texas'"))

# # B
# print(data[["street", "city"]].query("state=='Lowa'"))

# # C
# print(len(data))

# D
# Print first 2 records
# print(data.head(2))
