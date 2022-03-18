# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

# %%
file_address = "https://raw.githubusercontent.com/minhealthnz/nz-covid-data/main/cases/covid-cases.csv"

# %%
storage_options = {'User-Agent': 'Mozilla/5.0'}

# %%
df = pd.read_csv(file_address, storage_options=storage_options)

# %%
df_dhb = df[['Report Date', 'DHB']]

# %%
df_age = df[["Report Date","DHB","Age group"]]
# %%
df_temp = df_dhb.value_counts(['DHB','Report Date'], ascending = False, sort = False).to_frame()

# %%
df_age_temp = df_age.value_counts(['DHB','Report Date','Age group'], ascending = False, sort = False).to_frame()

# %%
df_temp_reset = df_temp.reset_index()

# %%
df_age_temp_reset = df_age_temp.reset_index()
# %%
df_temp_reset.columns = ["dhb","report_date","count"]

# %%
df_age_temp_reset.columns = ["dhb","report_date","age_group","count"]

# %%
dhb_population = pd.read_csv('data/csvs/dhb_population.csv')
# %%
os.makedirs('data/csvs', exist_ok=True)
df_temp_reset.to_csv('data/csvs/dhb_case_count.csv', index = False)
df_age_temp_reset.to_csv('data/csvs/dhb_age_case_count.csv', index = False)
# %%
