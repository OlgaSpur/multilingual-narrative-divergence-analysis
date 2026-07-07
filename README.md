# Multilingual Narrative Divergence Analysis

A multilingual NLP project analysing narrative divergence across English, Spanish, Russian and Ukrainian media coverage of the 15 June 2026 attack on the Kyiv-Pechersk Lavra using qualitative annotation, entity extraction and comparative quantitative analysis.

## Project Overview

This project explores multilingual narrative divergence across English, Spanish, Russian, and Ukrainian media sources.

It analyses how a single geopolitical event is framed differently across languages through comparative narrative analysis, combining manual annotation, automated entity extraction, and structured Python-based text analysis.

The goal is not sentiment classification, but comparative narrative framing analysis: how meaning, agency, and emphasis shift across information environments.

This project demonstrates how lightweight NLP techniques and structured qualitative analysis can be combined to investigate multilingual narrative divergence in geopolitical reporting.

---

## Dataset

The dataset consists of 12 news articles collected on 15 June 2026 surrounding the attack on the Kyiv-Pechersk Lavra.

### Languages included

- English
- Spanish
- Russian
- Ukrainian

### Sources

Sources were selected from reputable news outlets to ensure consistency across languages.

#### English sources

- BBC
- CNN
- The Guardian

#### Spanish sources

- El Mundo
- ABC
- UNITED24 Media

#### Russian sources

- Komsomolskaya Pravda (Комсомольская Правда)
- Argumenty i Fakty (Аргументы и Факты)
- RIA Novosti (РИА Новости)

#### Ukrainian sources

- Ukrainska Pravda (Українська Правда)
- European Pravda (Європейська Правда)
- Suspilne (Суспільне)

---

## Project Structure

```text
DATA/
    Raw and processed datasets used throughout the analysis.

SCRIPT/
    Python scripts for preprocessing, entity extraction,
    aggregation and visualisation.

VISUALS/
    Generated figures illustrating multilingual entity
    distributions and narrative divergence.

RESULTS/
    Summary findings and analytical outputs.

README.md
    Project documentation.
```

---

## Technologies

- Python
- pandas
- NumPy
- Matplotlib
- pathlib
- VS Code
- PowerShell
- CSV-based multilingual datasets

---

## Skills Demonstrated

- Multilingual text analysis
- Narrative framing analysis
- Named Entity Recognition (NER)
- Entity normalisation
- Data cleaning and preprocessing
- Comparative data analysis
- Data visualisation
- Python scripting

---

## Methodology

### Manual Narrative Coding

Each article was manually analysed using a structured framework including:

- Dominant themes
- Tone (neutral, defensive, critical, etc.)
- Key actors
- Framing direction (security, diplomacy, escalation, sovereignty)

This stage produced structured qualitative labels for each article, enabling cross-language comparison of framing patterns.

### Comparative Linguistic Analysis

Comparative analysis examined differences in actor prominence, attribution of responsibility, thematic emphasis and narrative framing across languages.

Particular attention was paid to how identical factual events were contextualised differently through diplomatic, humanitarian, military, cultural and religious narratives.

Articles were compared across languages to identify:

- Differences in emphasis
- Shifts in actor portrayal
- Variation in narrative framing and attribution of agency across actors

### NLP-Assisted Extraction

Named entities were automatically extracted using custom Python-based text processing and subsequently standardised to consolidate equivalent references across languages.

Extracted entities were used to support frequency analysis and cross-language comparison of narrative focus.

Entity mention frequencies were calculated per language to identify dominant narrative actors.

---

## Pipeline

The project was implemented in Python using VS Code, with a local development workflow managed via PowerShell.

Text processing and analysis were implemented using standard Python libraries and custom logic.

Visualisations were generated using Python-based plotting tools.

### 1. Data Collection

- Manual retrieval of news articles across languages
- Filtering for reputable journalistic sources

### 2. Data Organisation

- Articles stored in structured format (CSV / spreadsheet)
- Metadata includes language, source, date and headline

### 3. Manual Annotation

- Narrative coding using a predefined analytical framework

### 4. Feature Extraction and Automated Text Processing

- Automated named entity extraction from multilingual texts
- Entity normalisation across English, Spanish, Russian and Ukrainian variants
- Frequency calculation of entity mentions by language
- Construction of multilingual entity comparison matrices
- Narrative divergence score calculation based on cross-language mention differences

### 5. Data Aggregation

- Generation of multilingual comparison tables
- Calculation of narrative divergence scores

### 6. Visualisation

- Charts and comparative narrative summaries

---

## Visualisations

The following visualisations were generated to support comparative analysis:

- **Language Entity Heatmap** — shows the distribution of named entities across languages to compare narrative focus across language groups.
- **Top Narrative Divergence Entities** — highlights entities with the highest variation in mention frequency across language sources.

Visualisations are primarily descriptive rather than predictive.

---

## Key Findings

- English sources emphasised international diplomacy and heritage protection.
- Spanish sources placed greater emphasis on operational and military details.
- Russian sources prioritised attribution disputes and alternative explanations.
- Ukrainian sources focused on cultural heritage preservation and domestic impact.
- Entity frequency analysis quantitatively supported these qualitative framing differences.

---

## Results

Although all four language groups reported the same physical event, the analysis revealed systematic differences in narrative framing. While the factual basis remained largely consistent, each language group prioritised different actors, themes and explanations, producing measurable narrative divergence.

The combination of manual annotation and quantitative entity analysis demonstrated that the differences extended beyond wording to the broader organisation and emphasis of each narrative.

### English-Language Coverage

English-language coverage primarily framed the attack through the lenses of international diplomacy, civilian impact and the protection of globally recognised cultural heritage.

UNESCO, G7 leaders and international reactions featured prominently alongside descriptions of the attack.

Although responsibility for the strike was consistently attributed to Russia, English-language outlets typically acknowledged competing Russian claims regarding the cause of the cathedral damage, reflecting a journalistic emphasis on presenting contested attribution.

### Spanish-Language Coverage

Spanish-language coverage generally maintained a factual and chronological style but displayed greater internal variation than the English corpus.

While ABC strongly emphasised religious symbolism, historical continuity and the cultural significance of the Lavra, El Mundo devoted considerably more attention to operational military details, attack statistics and weapon systems.

Across the Spanish-language articles, official Ukrainian statements and technical aspects of the attack received greater prominence than broader diplomatic discussion.

### Russian-Language Coverage

Russian-language coverage differed fundamentally from the other language groups in both attribution and thematic focus.

Rather than concentrating on the physical consequences of the strike, Russian outlets frequently centred the narrative on disputes over responsibility, questioning Western and Ukrainian accounts and presenting alternative explanations involving Ukrainian Patriot air defence systems.

Several articles framed the incident as an information legitimacy issue, while others interpreted the event through religious and civilisational narratives, emphasising Orthodox identity over humanitarian or cultural heritage concerns.

### Ukrainian-Language Coverage

Ukrainian-language coverage consistently framed the attack as deliberate Russian damage to Ukrainian cultural heritage and national identity.

Compared with the other language groups, Ukrainian sources devoted substantially greater attention to documenting architectural damage, heritage preservation, restoration efforts and the protection of cultural artefacts.

Although diplomatic responses were covered, the dominant emphasis remained on preserving nationally significant historical and religious sites and documenting the broader impact on Ukraine's cultural landscape.

### Cross-Language Comparison

Across all four language groups, the same event exhibited clear and measurable differences in entity prominence, attribution of agency and thematic prioritisation.

Quantitative entity frequency analysis supported the qualitative findings by demonstrating that languages consistently foregrounded different actors and concepts.

---

## Limitations

- Small dataset (12 articles)
- Manual narrative coding inevitably involves researcher interpretation despite the use of a structured annotation framework
- Analysis focuses on a single event and should not be generalised to broader media ecosystems
- Entity extraction was designed for exploratory analysis rather than production-scale NLP

---

## Future Work

- Expand the dataset to include multiple geopolitical events and longer observation periods for comparative analysis
- Incorporate dependency parsing to analyse subject–verb–object relationships and improve automatic identification of narrative agency
- Explore transformer-based multilingual models for semantic similarity and narrative clustering
