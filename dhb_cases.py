# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

# %%
r = requests.get("https://www.health.govt.nz/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-case-demographics")

# %%
soup = BeautifulSoup(r.text, 'html.parser')

# %%
file_location = soup.find(id = "case-details-csv-file").get('href')

# %%
file_address = "https://www.health.govt.nz" + file_location

# %%
storage_options = {'User-Agent': 'Mozilla/5.0'}

# %%
df = pd.read_csv(file_address, storage_options=storage_options)

# %%
df_dhb = df[['Report Date', 'DHB']]

# %%
df_temp = df_dhb.value_counts(['DHB','Report Date'], ascending = False, sort = False).to_frame()

# %%
df_temp_reset = df_temp.reset_index()

# %%
df_temp_reset.columns = ["dhb","report_date","count"]


# %%
os.makedirs('data/csvs', exist_ok=True)
df_temp_reset.to_csv('data/csvs/dhb_case_count.csv', index = False)
# %%
