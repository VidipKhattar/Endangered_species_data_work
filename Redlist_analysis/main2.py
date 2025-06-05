import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("Yaello_buffer_STAR_TA.csv")

# Rename columns
df = df.rename(
    columns={
        "OBJECTID": "STAR_OBJECTID",
        "Sites": "STAR_Sites",
        "FREQUENCY": "STAR_FREQUENCY",
        "MEAN_Proportion": "STAR_MEAN_PROPORTION",
        "SUM_Proportion": "STAR_SUM_PROPORTION",
    }
)

# Create the star_category column based on MEAN_Proportion
df["STAR_CATEGORY"] = df["STAR_MEAN_PROPORTION"].apply(
    lambda x: (
        "Very Low"
        if x < 0.1
        else (
            "Low"
            if x < 1
            else ("Medium" if x < 10 else ("High" if x < 100 else "Very High"))
        )
    )
)

# Write the modified DataFrame back to a new CSV file
df.to_csv("modified_file.csv", index=False)

print("CSV file has been modified and saved.")
