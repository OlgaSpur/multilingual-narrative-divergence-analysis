from pathlib import Path
from docx import Document
import pandas as pd

project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

articles_folder = project / "ARTICLES"
data_folder = project / "DATA"

rows = []

for file in articles_folder.rglob("*.docx"):

    doc = Document(file)

    text = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
        if paragraph.text.strip()
    )

    language = file.parent.name

    rows.append({
        "article_file": file.name,
        "language": language,
        "path": str(file),
        "word_count": len(text.split()),
        "text": text
    })


df = pd.DataFrame(rows)

output = data_folder / "articles_dataset.csv"

df.to_csv(output, index=False, encoding="utf-8-sig")

print("Dataset created!")
print(output)
print(df[["article_file", "language", "word_count"]])
