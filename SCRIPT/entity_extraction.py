from pathlib import Path
import pandas as pd
import spacy


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

data_file = project / "DATA" / "articles_dataset.csv"
output_file = project / "DATA" / "entities_dataset.csv"


# Load multilingual model
nlp = spacy.load("xx_ent_wiki_sm")


df = pd.read_csv(data_file)


results = []

for index, row in df.iterrows():

    text = row["text"]

    doc = nlp(text)

    people = []
    organisations = []
    locations = []

    for ent in doc.ents:

        if ent.label_ == "PER":
            people.append(ent.text)

        elif ent.label_ == "ORG":
            organisations.append(ent.text)

        elif ent.label_ in ["LOC", "GPE"]:
            locations.append(ent.text)


    results.append({
        "article_file": row["article_file"],
        "language": row["language"],
        "people": ", ".join(set(people)),
        "organisations": ", ".join(set(organisations)),
        "locations": ", ".join(set(locations))
    })


entities_df = pd.DataFrame(results)

entities_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Entity extraction completed!")
print(output_file)