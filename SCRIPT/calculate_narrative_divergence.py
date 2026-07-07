import pandas as pd
from pathlib import Path

print("STARTING SCRIPT")

base = Path(__file__).resolve().parent.parent

input_file = base / "DATA" / "final_entity_matrix.csv"
output_file = base / "DATA" / "narrative_divergence_scores.csv"

print("Loading matrix...")
df = pd.read_csv(input_file)

languages = ["English", "Russian", "Spanish", "Ukrainian"]

results = []

for _, row in df.iterrows():

    values = {}

    for lang in languages:
        values[lang] = row[lang]

    max_lang = max(values, key=values.get)
    min_lang = min(values, key=values.get)

    divergence_score = values[max_lang] - values[min_lang]

    results.append({
        "entity": row["normalised_entity"],
        "dominant_language": max_lang,
        "least_present_language": min_lang,
        "divergence_score": divergence_score,
        "English": values["English"],
        "Russian": values["Russian"],
        "Spanish": values["Spanish"],
        "Ukrainian": values["Ukrainian"]
    })

result_df = pd.DataFrame(results)

result_df = result_df.sort_values(
    by="divergence_score",
    ascending=False
)

result_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("DONE")
print(output_file)
print(result_df.head(20))