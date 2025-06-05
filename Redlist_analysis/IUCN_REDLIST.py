import csv
import requests

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
    "Nymphoides tenuissima",
    "Eleocharis dulcis",
    "Aponogeton junceus",
    "Nymphoides rautanenii",
    "Eriocaulon afzelianum",
    "Zantedeschia albomaculata",
    "Utricularia microcalyx",
    "Xyris gossweileri",
    "Utricularia bracteata",
    "Eriocaulon transvaalicum",
    "Aponogeton desertorum",
    "Aponogeton rehmannii",
    "Eriocaulon cinereum",
    "Schoenoplectiella mucronata",
    "Lagarosiphon ilicifolius",
    "Fimbristylis squarrosa",
    "Juncus oxycarpus",
    "Juncus punctorius",
    "Juncus dregeanus subsp. bachitii",
    "Aspilia helianthoides",
    "Ascolepis lineariglumis",
    "Ottelia fischeri",
    "Litogyne gariepina",
    "Rhynchospora gracillima",
    "Nymphoides indica",
    "Aponogeton stuhlmannii",
    "Nymphoides brevipedicellata",
    "Lagarosiphon cordofanus",
    "Conyza clarenceana",
    "Ascolepis capensis",
    "Eleocharis acutangula",
    "Sesbania bispinosa",
    "Cyperus papyrus",
    "Typha capensis",
    "Adenostemma caffrum",
    "Anagallis kochii",
    "Anagallis elegantula",
    "Hypoestes aristata",
    "Cyperus imbricatus",
    "Oryza schweinfurthiana",
    "Cyperus compressus",
    "Hygrophila senegalensis",
    "Rhynchospora holoschoenoides",
    "Juncus dregeanus",
    "Aponogeton vallisnerioides",
    "Eriocaulon setaceum",
    "Ottelia verdickii",
    "Najas pectinata",
    "Rhynchospora corymbosa",
    "Digitaria nuda",
    "Juncus rigidus",
    "Cyperus digitatus",
    "Oryza barthii",
    "Eleocharis atropurpurea",
    "Heteranthera callifolia",
    "Nymphoides forbesiana",
    "Myriophyllum spicatum",
    "Cyperus amabilis",
    "Oryza punctata",
    "Eleocharis atropurpurea",
    "Rhipsalis baccifera",
    "Pistia stratiotes",
    "Cyperus rotundus",
    "Aeschynomene indica",
    "Potamogeton schweinfurthii",
    "Centrostachys aquatica",
    "Schoenoplectiella senegalensis",
    "Oryza longistaminata",
    "Eleocharis geniculata",
    "Cyperus longus",
    "Ascolepis elata",
    "Cyperus iria",
    "Enydra fluctuans",
    "Alternanthera sessilis",
    "Limnophyton obtusifolium",
    "Grangea maderaspatana",
    "Potamogeton trichoides",
    "Potamogeton octandrus",
    "Vallisneria spiralis",
    "Landoltia punctata",
    "Nymphaea nouchali",
    "Crassocephalum picridifolium",
    "Hydrilla verticillata",
    "Trapa natans",
    "Typha domingensis",
    "Fimbristylis bisumbellata",
    "Potamogeton nodosus",
    "Najas marina",
    "Juncus effusus",
    "Stuckenia pectinata",
    "Spirodela polyrhiza",
    "Potamogeton pusillus",
    "Zannichellia palustris",
]

# Create a CSV file and write the species name and the related link
csv_file_path = "species_links.csv"
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Species Name", "Link"])  # Write the header row

    # Iterate through the species names
    for species_name in species_names:
        print(species_name)
        # Make the request to get the link for the species
        response = requests.get(
            f"https://apiv3.iucnredlist.org/api/v3/website/{species_name}"
        )

        # Extract the link from the response
        if response.status_code == 200:
            link = response.url
        else:
            link = "Link not available"

        # Write the species name and the related link to the CSV file
        writer.writerow([species_name, link])

print(f"CSV file has been created at {csv_file_path}")
