from pathlib import Path
import pandas as pd


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "entity_frequency_by_language.csv"
output_file = project / "DATA" / "normalised_entity_frequency.csv"


df = pd.read_csv(input_file)


normalisation = {

    # countries
    "Russia": "Russia",
    "Rusia": "Russia",
    "Россию": "Russia",
    "Росії": "Russia",
    "Росію": "Russia",
    "France": "France",

    "Ukraine": "Ukraine",
    "Ucrania": "Ukraine",
    "Украина": "Ukraine",
    "Україна": "Ukraine",
    "України": "Ukraine",
    "Україні": "Ukraine",

    # cities
    "Kyiv": "Kyiv",
    "Kiev": "Kyiv",
    "Киев": "Kyiv",
    "Київ": "Kyiv",
    "Киеве": "Kyiv",

    "Moscow": "Moscow",
    "Moscú": "Moscow",

    "Kharkiv": "Kharkiv",
    "Járkov": "Kharkiv",

    # organisations
    "UNESCO": "UNESCO",
    "Unesco": "UNESCO",
    "ЮНЕСКО": "UNESCO",

    "EU": "European Union",
    "ЕС": "European Union",
    "ЄС": "European Union",

    "Nato": "NATO",
    "НАТО": "NATO",

    # people
    "Zelensky": "Volodymyr Zelensky",
    "Volodymyr Zelensky": "Volodymyr Zelensky",
    "Zelenskyy": "Volodymyr Zelensky",
    "Володимир Зеленський": "Volodymyr Zelensky",
    "Зеленский": "Volodymyr Zelensky",

    "Putin": "Vladimir Putin",
    "Владимир Путин": "Vladimir Putin",

    "Volodímir Zelenski": "Volodymyr Zelensky",
    "Volodimir Zelenski": "Volodymyr Zelensky",

    # heritage
    "Dormition Cathedral": "Dormition Cathedral",
    "Catedral de la Dormición": "Dormition Cathedral",
    "Успенський собор": "Dormition Cathedral",

}


def normalise(entity):

    entity = str(entity).strip()

    if entity in normalisation:
        return normalisation[entity]

    return entity



df["normalised_entity"] = df["entity"].apply(normalise)


result = (
    df
    .groupby(
        ["normalised_entity", "language", "entity_type"]
    )["mentions"]
    .sum()
    .reset_index()
    .sort_values(
        "mentions",
        ascending=False
    )
)


result.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Normalisation completed!")
print(output_file)
print(result.head(30))
