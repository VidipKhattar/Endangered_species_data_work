import requests
import json
import csv

csv_file_path = "output.csv"

species_names = [
    "Cyperus demangei",
    "Scleria mikawana",
    "Aponogeton afroviolaceus",
    "Ottelia kunenensis",
    "Monochoria africana",
    "Cyperus clavinux",
    "Sphaeranthus steetzii",
    "Xyris lejolyanus",
    "Ottelia muricata",
    "Bulbostylis clarkeana",
]

# Make a sample request to get the field names
sample_request = requests.get(
    "http://services.tropicos.org/Name/Scleria mikawana/Specimens?apikey=6dd331a5-2ec2-4ab0-90ac-86f9da8fd5fe&format=json"
)

sample_data = json.loads(sample_request.text)
print(sample_data)

# Extract fieldnames from the sample data
fieldnames = list(sample_data[0].keys())
print(fieldnames)

# Open CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    for i in species_names:
        # Make request for each species name
        x = requests.get(
            "http://services.tropicos.org/Name/Search?name="
            + i
            + "&type=wildcard&apikey=6dd331a5-2ec2-4ab0-90ac-86f9da8fd5fe&format=json"
        )
        data = json.loads(x.text)
        print(data)

        # Write rows
        for row in data:
            print("done")
            writer.writerow(row)

print(f"CSV file has been created at {csv_file_path}")
