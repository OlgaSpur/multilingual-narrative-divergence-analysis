import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT = "DATA/final_entity_matrix.csv"
OUTPUT = "VISUALS"

os.makedirs(OUTPUT, exist_ok=True)

df = pd.read_csv(INPUT)

# Calculate divergence score from the master matrix
langs = ["English", "Russian", "Spanish", "Ukrainian"]

df["divergence_score"] = (
    df[langs].max(axis=1) -
    df[langs].min(axis=1)
)

# Select the 15 most divergent entities
top = df.sort_values(
    by="divergence_score",
    ascending=False
).head(15)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(top["normalised_entity"], top["divergence_score"])
ax.set_xlabel("Difference between highest and lowest language mention counts")
ax.set_title("Top 15 Entities with the Highest Narrative Divergence")
ax.invert_yaxis()

fig.tight_layout()

fig.savefig(
    os.path.join(OUTPUT, "top_divergent_entities.png"),
    dpi=300
)

plt.close(fig)

# ----------------------------
# Heatmap
# ----------------------------

langs = ["English", "Russian", "Spanish", "Ukrainian"]

matrix = top.set_index("normalised_entity")[langs]

fig, ax = plt.subplots(figsize=(8, 10))

im = ax.imshow(
    matrix.values,
    aspect="auto",
    interpolation="nearest"
)

ax.set_xticks(range(len(langs)))
ax.set_xticklabels(
    langs,
    fontsize=12
)

ax.set_yticks(range(len(matrix.index)))
ax.set_yticklabels(
    matrix.index,
    fontsize=10
)

# Write values inside cells
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        ax.text(
            j,
            i,
            int(matrix.iloc[i, j]),
            ha="center",
            va="center",
            color="white",
            fontsize=10
        )

ax.set_title("Entity Mention Frequency Across Languages")
ax.set_xlabel("Language")
ax.set_ylabel("Entity")

fig.colorbar(
    im,
    ax=ax,
    label="Mentions"
)

fig.tight_layout()

fig.savefig(
    os.path.join(OUTPUT, "language_entity_heatmap.png"),
    dpi=400
)

plt.close(fig)

print("Visualisations created")
