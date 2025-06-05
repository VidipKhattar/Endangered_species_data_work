import pandas as pd
import requests
import urllib.parse
import csv
import requests
import urllib.parse
import csv
import pandas as pd
import time
from requests.exceptions import RequestException

# Load the CSV files into DataFrames
species_df = pd.read_csv("RL_Sp_Name.csv")
species_url_df = pd.read_csv("RL_Sp_URL (1).csv")

# Extract species lists from each DataFrame
species_list = species_df["Species"].tolist()
species_url_list = species_url_df["species"].tolist()

# Convert lists to sets for easier comparison
species_set = set(species_list)
species_url_set = set(species_url_list)

# Find species present in species_df but not in species_url_df
species_only_in_species_df = species_set - species_url_set

# Find species present in species_url_df but not in species_df
species_only_in_species_url_df = species_url_set - species_set

# Convert the sets back to lists if you want to output them
species_only_in_species_df = list(species_only_in_species_df)
species_only_in_species_url_df = list(species_only_in_species_url_df)

# Output the results
# print("Species in species.csv but not in species_url.csv:")
# print(species_only_in_species_df)

# print("Species in species_url.csv but not in species.csv:")
# print(species_only_in_species_url_df)
print(len(species_only_in_species_df))


# Function to fetch Red List URL for a given species with retries
def get_red_list_url(species_name, api_key, max_retries=1000, delay=2):
    encoded_species_name = urllib.parse.quote(species_name)  # Encode species name
    url = f"https://apiv3.iucnredlist.org/api/v3/weblink/{encoded_species_name}?token={api_key}"
    retries = 0

    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for non-200 status codes
            data = response.json()
            red_list_url = data.get(
                "rlurl", "Species not found"
            )  # Extract the URL from the JSON response
            return red_list_url

        except RequestException as e:
            print(f"Error fetching data for {species_name}: {e}")
            retries += 1
            time.sleep(delay)  # Wait before retrying

    return "Error fetching data"


# Example usage
api_key = "46d5a9f9c0eee58b93ff5b94f72e8d820ddafb3914257ac6c694d0fb3236b9af"
output_csv = "RL_Sp_URL_2.csv"
# Write the results to the output CSV
with open(output_csv, "w", newline="") as myFile:
    writer = csv.DictWriter(myFile, fieldnames=["species", "red_list_url"])
    writer.writeheader()
    for species in species_only_in_species_df:
        red_url = get_red_list_url(species, api_key)
        row = {"species": species, "red_list_url": red_url}
        writer.writerow(row)
        print(f"{species}, {red_url}")
        time.sleep(1)  # Delay between requests to avoid rate limiting
