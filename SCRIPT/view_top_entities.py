from pathlib import Path
import pandas as pd


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

file = project / "DATA" / "entity_frequency_by_language.csv"

df = pd.read_csv(file)


for language in df["language"].unique():

    print("\n====================")
    print(language)
    print("====================")

    print(
        df[df["language"] == language]
        .head(10)
        .to_string(index=False)
    )