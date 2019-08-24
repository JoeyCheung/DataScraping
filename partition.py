import pandas as pd

pd1 = pd.read_csv("test.csv")

# Columns 20 and 25 are specifically chosen because those are the columns that always gives the URL and the load_start data
x = pd1.iloc[:, 20]
y = pd1.iloc[:, 25]

# Store the data into a dataframe 
pd_data = pd.DataFrame({'load_start': x, 'full_url': y})
 

urls = [] # Store full_url data
loads = [] #Store load_start data
substring = "" # This is the substring that identifies if it's in the string or not
for i in pd_data.itertuples():
    # Checks if the substring is in the URL, then appends that row into two separate lists
    if substring in i.full_url:
        urls.append(i.full_url)
        loads.append(i.load_start)
        
new_pd_data = pd.DataFrame({'load_start': loads, 'full_url': urls})

pd_data.to_csv('output.csv', encoding='utf-8', index=False)
