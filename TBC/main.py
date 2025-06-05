import pandas as pd

df = pd.read_csv("LiloLine_EAAA_RLSp_range.csv")
cms_df = pd.read_csv("CMS.csv")

matches = [
    element
    for element in list(df["sci_name"])
    if element in list(cms_df["ScientificName"])
]

site_arr = ["Districts", "FW_EAAA", "Terrestrial_EAAA"]

selected_columns = [
    "Scientific Name",
    "Common Name",
    "Class",
    "Biome",
    "IUCN Red List status",
    "percentage of species global range in EAAA",
    "CH trigger",
    "Criterion",
    "Justification",
]

for index, i in enumerate(site_arr):
    spec_list = []
    for indexes, row in df.iterrows():
        criterion = []
        biome = []
        justif = []
        if row[i] >= 0.05 and (row["category"] == "EN" or row["category"] == "CR"):
            criterion.append("1a")
            justif.append(
                row["category"] + " with " + str(row[i])[:4] + "% range overlap"
            )
        if row[i] > 10 and (row["category"] == "VU"):
            criterion.append("1b")
            justif.append("VU with " + str(row[i])[:6] + "% range overlap")
        if (
            row[i] > 10
            and (row["biome_freshwater"] == "TRUE")
            and row["FW_Width"] < 200
            and row["FW_Length"] < 500
        ):
            criterion.append("2")
            justif.append("restricted range EOO" + row["Range_Areakm2"] + "km2")
            biome.append("Freshwater")
        elif (
            row[i] > 10
            and (row["biome_terrestrial"] == "TRUE")
            and row["Range_Areakm2"] < 50000
        ):
            criterion.append("2")
            justif.append("restricted range EOO" + row["Range_Areakm2"] + "km2")
            biome.append("Terrestrial")
        elif (
            row[i] > 10
            and (row["biome_marine"] == "TRUE")
            and row["Range_Areakm2"] < 100000
        ):
            criterion.append("2")
            justif.append("restricted range EOO" + row["Range_Areakm2"] + "km2")
            biome.append("Marine")
        if row[i] > 1 and (
            row["movementpattern"] == "Full Migrant"
            or row["movementpattern"] == "Altitudinal Migrant"
        ):
            criterion.append("3")
            justif.append("Migratory")
        elif row["sci_name"] in matches and row[i] > 1:
            criterion.append("3")
            justif.append("Migratory")
        if criterion != []:
            # print(criterion)
            # print(biome)
            row_dict = {
                "Scientific Name": row["sci_name"],
                "Common Name": row["common_name"],
                "Class": row["class_name"],
                "Biome": biome,
                "IUCN Red List status": row["category"],
                "percentage of species global range in EAAA": str(row[i])[:8],
                "CH trigger": "Likely",
                "Criterion": ", ".join([str(elem) for elem in criterion]),
                "Justification": ", ".join([str(elem) for elem in justif]),
            }
            spec_list.append(row_dict)
            # print(justif)
    df_rr = pd.DataFrame(spec_list)
    df_rr.to_csv(i + ".csv")
