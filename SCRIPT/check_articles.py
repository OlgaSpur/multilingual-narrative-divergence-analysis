from pathlib import Path

project = Path(r"C:\Users\admin\Documents\Project Multilingual Narrative Divergence Analysis")

articles_folder = project / "ARTICLES"

print("Articles folder exists:", articles_folder.exists())
print("Articles folder path:", articles_folder)

for file in articles_folder.rglob("*.docx"):
    print(file)
