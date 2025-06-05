# import libraries
import pandas as pd
import numpy as np

# convert csv files to dataframes
sites_csv = pd.read_csv("Sites.csv")
df = pd.read_csv("Species.csv")

# get site names from csv and convert to list
sites = sites_csv["Sites"].to_list()

# df filter species df to only EN CR categories
species_df = df[df["category"].isin(["EN", "CR"])]
en_df = df[df["category"] == "EN"]
cr_df = df[df["category"] == "CR"]
# df filter species df to "Range_Areakm2" < 50000
range_df = df[df["Range_Areakm2"] < 50000]

print(range_df)


count_dict = {}

# loop through all sites
for i in sites:
    # convert site columns to list
    site_en_list = en_df[i].to_list()
    site_cr_list = cr_df[i].to_list()
    site_range_list = range_df[i].to_list()

    # find counts for each column above respective value
    count_above_0_5_en = sum(
        1 for value in site_en_list if not np.isnan(value) and value > 0.5
    )
    count_above_0_5_cr = sum(
        1 for value in site_cr_list if not np.isnan(value) and value > 0.5
    )
    count_above_10 = sum(
        1 for value in site_range_list if not np.isnan(value) and value > 10
    )
    # add count to dictionary
    count_dict[i] = [count_above_0_5_en, count_above_0_5_cr, count_above_10]


# Create an empty list to store data
data_list = []

print(count_dict)

# Iterate through the dictionary and unpack values
for site, values in count_dict.items():
    data_list.append([site, values[0], values[1], values[2]])

# Create a DataFrame from the list with column names
df = pd.DataFrame(data_list, columns=["site", "en", "cr", "range"])

# Save the DataFrame to a CSV file
df.to_csv("output.csv", index=False)
