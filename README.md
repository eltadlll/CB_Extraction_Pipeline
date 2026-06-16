# Extraction System — Quick Start Guide
---
## WHat is the project about 
This is a property extraction and algebraic encoding pipeline built for the Conceptual Blending research project at iCog Labs. It sits at the first stage of the full Conceptual Blending system — before any blending happens, you need to deeply understand each concept on its own terms: what it is, what it does, and how strongly each of those properties defines it.The system takes two concepts as input — anything from Jazz to Quantum Computing to Democracy — and for each one it extracts exactly 8 defining properties, then encodes those properties in a formal algebraic representation that the blending engine can reason over symbolically.

## What it does
### Step 1 — Knowledge Base Generation

Before extracting properties, the system builds a structured knowledge base entry for each concept automatically. It sends the concept name to Gemini and gets back a semantic profile: the domain it belongs to, the processes it involves, the entities it relates to, and the ontological worlds it inhabits. This profile is cached locally as a JSON file so it never needs to be generated again — the more concepts you run through the system, the richer your knowledge base becomes over time.
### Step 2 — Property Extraction

Using that knowledge base context, a Gemini agent extracts exactly 8 properties per concept. These are not just keywords or tags — each property is a symbolic predicate that captures something the concept does or is. The 8 properties follow a strict distribution from most core to most peripheral: the first three are the definitional heart of the concept, the middle properties are supporting characteristics, and the final property is abstract or emergent — something that exists at the edge of the concept's meaning.
### Step 3 — Algebraic Encoding

Each property is encoded with two pieces of algebraic metadata:

WorldSpecSet — the set of ontological domains the property inhabits, drawn from a fixed 18-domain vocabulary (Physics, Biology, Cognition, Linguistics, etc.). A property with a full WorldSpecSet is richly grounded across multiple domains. A property with an empty WorldSpecSet () is abstract and domain-independent.
Degree — a symbolic label from degree-1 (core, centrality 0.85–1.0) down to degree-5 (peripheral, centrality 0.0–0.25) that captures how strongly the property defines the concept.

The final output is a CASL S-expression — a formal algebraic representation of the concept and all its properties in a structure that symbolic reasoning engines like MeTTa/Hyperon can directly process.
### Step 4 — Output


Three files are saved per concept: a .casl file with the algebraic S-expression, a .metta file with Hyperon-compatible atoms that are also appended to the shared knowledge base for future reasoning, and a .json file with the full structured output for downstream use.





    (Concept Evolution
      (V-predicate
      (Property
        (heritable-trait-change
          (WorldSpecSet
                    (WorldSpec-Biology
                     WorldSpec-Information
                     WorldSpec-Chemistry
                     WorldSpec-Ecology))
          degree-1)
  
        (mechanism-driven-process
          (WorldSpecSet
                    (WorldSpec-Biology
                     WorldSpec-Ecology
                     WorldSpec-Information))
          degree-1)
  
        (biodiversity-adaptation-generation
          (WorldSpecSet
                    (WorldSpec-Biology
                     WorldSpec-Ecology
                     WorldSpec-Information))
          degree-1)
  
        (long-temporal-process
          (WorldSpecSet
                    (WorldSpec-Biology
                     WorldSpec-Ecology))
          degree-2)
  
        (population-level-change
          (WorldSpecSet
                    (WorldSpec-Biology
                     WorldSpec-Ecology))
          degree-2)
  
        (genetic-variation-dependency
          (WorldSpecSet
                    (WorldSpec-Biology
                     WorldSpec-Information))
          degree-3)
  
        (environmental-interaction
          (WorldSpecSet
                    (WorldSpec-Ecology))
          degree-4)
  
        (historical-record-formation
          (WorldSpecSet ())
          degree-5)
  
      )))

---
---

## 1. Get a Gemini API Key (free)

1. Go to **https://aistudio.google.com/app/apikey**
2. Sign in with a Google account
3. Click **"Create API key"**
4. Copy the key — you'll need it in step 4

---

## 2. Install Python

You need **Python 3.8 or higher**.

Check if you already have it:
```bash
python --version
```

If not, download it from **https://www.python.org/downloads**

---

## 3. Set up the project

Unzip the downloaded file, then open a terminal inside the folder:

```bash
cd extraction_system
```

Create a virtual environment (keeps dependencies isolated):
```bash
# Mac / Linux
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 4. Set your API key

```bash
# Mac / Linux
export GEMINI_API_KEY="paste_your_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=paste_your_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="paste_your_key_here"
```

> **Tip:** You only need to do this once per terminal session.
> If you close the terminal and reopen it, run this line again.

---

## 5. Run it

### Option A — Streamlit UI (recommended)

```bash
streamlit run app.py
```

A browser window opens automatically at `http://localhost:8501`.

- Type two concept names (e.g. *Jazz* and *Architecture*)
- Click **Extract & Encode**
- View the CASL output and download `.casl`, `.metta`, `.json` files

The **Knowledge Base tab** lets you browse, add, and delete cached concepts.

---

### Option B — Command line

```bash
python pipeline.py --concept-a "Solar Energy" --concept-b "Water Purification"
```

Any two concepts work:
```bash
python pipeline.py --concept-a "Jazz" --concept-b "Architecture"
python pipeline.py --concept-a "Democracy" --concept-b "Ecosystem"
python pipeline.py --concept-a "Machine Learning" --concept-b "Evolution"
```

Output files are saved in the `outputs/` folder automatically.

---

## 6. Output files

After each run, three files are saved per concept inside `outputs/`:

| File | What it contains |
|------|-----------------|
| `ConceptName.casl` | CASL algebraic S-expression |
| `ConceptName.metta` | MeTTa atoms for Hyperon/OpenCog |
| `ConceptName.json` | Full structured output |

MeTTa atoms are also appended to `metta/knowledge_base.metta`.

---

## 7. How the knowledge base works

You **never need to write KB entries manually.**

- First time you use a concept → Gemini profiles it and saves it to `knowledge_base/concepts/ConceptName.json`
- Every time after → loaded instantly from disk, no API call

To pre-load a concept before blending:
- In the UI: go to the **Knowledge Base tab** → type a name → click **Generate & save**
- On the CLI: just run the pipeline with that concept — it caches automatically

---

## Troubleshooting

**`GEMINI_API_KEY not set` error**
→ You forgot step 4. Re-run the `export` / `set` command in your terminal.

**`ModuleNotFoundError`**
→ Your virtual environment isn't active. Run `source .venv/bin/activate` (Mac/Linux) or `.venv\Scripts\activate` (Windows) first.

**`streamlit: command not found`**
→ Dependencies aren't installed. Run `pip install -r requirements.txt` again inside the activated environment.

**Gemini returns an error about quota**
→ The free tier has rate limits. Wait 60 seconds and try again.
