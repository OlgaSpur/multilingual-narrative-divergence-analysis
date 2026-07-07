from pathlib import Path
import pandas as pd
import re


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "entities_dataset.csv"
output_file = project / "DATA" / "cleaned_entities_dataset.csv"


df = pd.read_csv(input_file)


def clean_entity_list(text):

    if pd.isna(text) or text == "":
        return ""

    entities = text.split(",")

    cleaned = []

    for entity in entities:

        entity = entity.strip()

        # remove URLs
        if entity.startswith("http"):
            continue

        # remove very short fragments
        if len(entity) < 3:
            continue

        # remove obvious noise
        if entity.lower() in [
            "el",
            "la",
            "de",
            "the",
            "and"
        ]:
            continue

        cleaned.append(entity)


    # remove duplicates while keeping order
    cleaned = list(dict.fromkeys(cleaned))

    return ", ".join(cleaned)


for column in [
    "people",
    "organisations",
    "locations"
]:
    df[column] = df[column].apply(clean_entity_list)


df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Cleaning completed!")
print(output_file)
from pathlib import Path
import pandas as pd
import re


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "entities_dataset.csv"
output_file = project / "DATA" / "cleaned_entities_dataset.csv"


df = pd.read_csv(input_file)


remove_words = [
    "Haremos",
    "Віра",
    "Добро",
    "Православия",
    "Слово",
    "які від",
    "які живі",
    "Раніше",
    "Росії",
    "Росію",
    "El",
    "The",
    "and",
    "of"
]


media_names = [
    "CNN",
    "BBC",
    "RIA Novosti",
    "RIA",
    "Argumenty I Fakty",
    "Komsomolskaya Pravda",
    "Ukrainska Pravda",
    "European Pravda"
]


def clean_entity_list(text):

    if pd.isna(text):
        return ""

    entities = text.split(",")

    cleaned = []

    for e in entities:

        e = e.strip()

        if not e:
            continue

        # remove URLs
        if "http" in e:
            continue

        # remove unwanted words
        if e in remove_words:
            continue

        # remove media from people
        if e in media_names:
            continue

        # remove very long fragments
        if len(e) > 60:
            continue

        cleaned.append(e)


    cleaned = list(dict.fromkeys(cleaned))

    return ", ".join(cleaned)


for col in ["people", "organisations", "locations"]:
    df[col] = df[col].apply(clean_entity_list)


df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Improved cleaning completed!")
print(output_file)
from pathlib import Path
import pandas as pd


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "entities_dataset.csv"
output_file = project / "DATA" / "cleaned_entities_dataset.csv"


df = pd.read_csv(input_file)


def clean_entity_list(text):

    if pd.isna(text):
        return ""

    entities = str(text).split(",")

    cleaned = []

    for e in entities:

        e = e.strip()

        if not e:
            continue

        # remove URLs
        if "http" in e.lower():
            continue

        # remove obvious noise
        if len(e) < 3:
            continue

        # remove long broken fragments
        if len(e) > 80:
            continue

        cleaned.append(e)


    # remove duplicates
    cleaned = list(dict.fromkeys(cleaned))

    return ", ".join(cleaned)


for column in ["people", "organisations", "locations"]:
    df[column] = df[column].apply(clean_entity_list)


df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Cleaning completed!")
print(output_file)
print(df.head())
print("\nSaved file size:")
print(output_file.stat().st_size, "bytes")