import requests
import urllib.parse
import csv
import requests
import urllib.parse
import csv
import pandas as pd
import time
from requests.exceptions import RequestException


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
input_csv = "RL_Sp_Name.csv"  # Replace with the path to your input CSV
output_csv = "RL_Sp_URL.csv"

# Read the list of species from the input CSV
species_list = pd.read_csv(input_csv)["Species"].tolist()

# Write the results to the output CSV
with open(output_csv, "w", newline="") as myFile:
    writer = csv.DictWriter(myFile, fieldnames=["species", "red_list_url"])
    writer.writeheader()

    for species in species_list:
        red_url = get_red_list_url(species, api_key)
        row = {"species": species, "red_list_url": red_url}
        writer.writerow(row)
        print(f"{species}, {red_url}")
        time.sleep(1)  # Delay between requests to avoid rate limiting
