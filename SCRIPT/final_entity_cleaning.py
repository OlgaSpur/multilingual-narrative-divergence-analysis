from pathlib import Path
import pandas as pd


project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

input_file = project / "DATA" / "divergence_matrix.csv"
output_file = project / "DATA" / "final_entity_matrix.csv"


df = pd.read_csv(input_file)


# Merge obvious multilingual variants
rename_map = {

    # Ukraine / Russia
    "Francia": "France",
    "Járkov": "Kharkiv",
    "Volodímir Zelenski": "Volodymyr Zelensky",
    "Volodimir Zelenski": "Volodymyr Zelensky",
    "Zelensky": "Volodymyr Zelensky",
    "Zelenskyy": "Volodymyr Zelensky",
    "Зеленский": "Volodymyr Zelensky",
    "Володимир Зеленський": "Volodymyr Zelensky",

    "Putin": "Vladimir Putin",
    "Владимир Путин": "Vladimir Putin",

    "Trump": "Donald Trump",

    "Киев": "Kyiv",
    "Київ": "Kyiv",
    "Киеве": "Kyiv",

    "Ucrania": "Ukraine",
    "Украина": "Ukraine",
    "Україна": "Ukraine",
    "України": "Ukraine",

    "Россию": "Russia",
    "Росії": "Russia",
    "Rusia": "Russia",

    # Heritage
    "Catedral de la Dormición": "Dormition Cathedral",
    "catedral de la Dormición": "Dormition Cathedral",
    "Успенський собор": "Dormition Cathedral",

    "ЮНЕСКО": "UNESCO",
    "Unesco": "UNESCO",

    # Kyiv Pechersk Lavra
"Kyiv-Pechersk Lavra": "Kyiv Pechersk Lavra",
"Pechersk Lavra": "Kyiv Pechersk Lavra",
"Pechersk Lavra de Kyiv": "Kyiv Pechersk Lavra",
"Perchersk Lavra": "Kyiv Pechersk Lavra",
"Perchersk-Lavra": "Kyiv Pechersk Lavra",
"Лавры": "Kyiv Pechersk Lavra",
"Лавру": "Kyiv Pechersk Lavra",
"Лаврі": "Kyiv Pechersk Lavra",
"Лавра": "Kyiv Pechersk Lavra",

"Киево-Печерская Лавра": "Kyiv Pechersk Lavra",
"Киево-Печерской": "Kyiv Pechersk Lavra",
"Киево-Печерской Лавры": "Kyiv Pechersk Lavra",
"Киево-Печерской лавре": "Kyiv Pechersk Lavra",
"Киево-Печерской лавры": "Kyiv Pechersk Lavra",
"Киево-Печорской Лавре": "Kyiv Pechersk Lavra",
"Киево-Печорской Лавры": "Kyiv Pechersk Lavra",

"Києво-Печерська": "Kyiv Pechersk Lavra",
"Києво-Печерської": "Kyiv Pechersk Lavra",
"Києво-Печерську": "Kyiv Pechersk Lavra",
"Києво-Печерській": "Kyiv Pechersk Lavra",

# Tymur Tkachenko
"Timur Tkachenko": "Tymur Tkachenko",
"Tkachenko": "Tymur Tkachenko",
"Тимур Ткаченко": "Tymur Tkachenko",

# Klitschko
"Vitaliy Klitschko": "Vitali Klitschko",
"Vitali Klitchkó": "Vitali Klitschko",
"Klitschko": "Vitali Klitschko",

# Notre Dame
"Notre-Dame": "Notre Dame",

# Epiphanius
"Metropolitan Epiphanius of Kyiv": "Metropolitan Epiphanius",
"Epifanio": "Metropolitan Epiphanius",

# Dormition Cathedral
"Успенского собора": "Dormition Cathedral",
"Успенського собору": "Dormition Cathedral",
"Успенському собору": "Dormition Cathedral",

}


df["normalised_entity"] = (
    df["normalised_entity"]
    .replace(rename_map)
)


# Remove extraction noise
bad_entities = [
    "T]he",
    "URL:",
    "El",
    "Russian-",
    "US-manufactured",
    "Vladimir",
    "Украине",
    "Украину",
    "Catedral de la Dormición\nEl",
    "Dormición de Kiev\nEl",
    "які живі",
    "мати щастя",
    "друзям",
]


df = df[
    ~df["normalised_entity"].isin(bad_entities)
]


# Remove empty rows
df = df[
    df["normalised_entity"].notna()
]


# Merge duplicate entities by summing language counts
df = (
    df
    .groupby("normalised_entity", as_index=False)
    .agg({
        "English": "sum",
        "Russian": "sum",
        "Spanish": "sum",
        "Ukrainian": "sum",
        "total_mentions": "sum"
    })
)


df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("Final cleaning completed!")
print(output_file)
print(df.head(30))