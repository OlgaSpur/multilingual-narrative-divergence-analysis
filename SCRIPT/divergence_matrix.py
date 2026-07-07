from pathlib import Path
import pandas as pd


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "normalised_entity_frequency.csv"

output_file = project / "DATA" / "divergence_matrix.csv"


df = pd.read_csv(input_file)


pivot = df.pivot_table(
    index="normalised_entity",
    columns="language",
    values="mentions",
    aggfunc="sum",
    fill_value=0
)


pivot["total_mentions"] = pivot.sum(axis=1)


pivot = pivot.sort_values(
    "total_mentions",
    ascending=False
)


pivot.to_csv(
    output_file,
    encoding="utf-8-sig"
)


print("Divergence matrix created!")
print(output_file)

print(pivot.head(20))