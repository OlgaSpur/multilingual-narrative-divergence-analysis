from pathlib import Path
import pandas as pd
from collections import Counter


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "cleaned_entities_dataset.csv"
output_file = project / "DATA" / "entity_frequency_by_language.csv"


df = pd.read_csv(input_file)


rows = []


for index, row in df.iterrows():

    for entity_type in ["people", "organisations", "locations"]:

        entities = str(row[entity_type]).split(",")

        for entity in entities:

            entity = entity.strip()

            if entity:
                rows.append({
                    "language": row["language"],
                    "entity_type": entity_type,
                    "entity": entity
                })


entities_df = pd.DataFrame(rows)


frequency = (
    entities_df
    .groupby(["language", "entity_type", "entity"])
    .size()
    .reset_index(name="mentions")
    .sort_values(
        ["language", "entity_type", "mentions"],
        ascending=[True, True, False]
    )
)


frequency.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Frequency analysis completed!")
print(output_file)

print(frequency.head(20))