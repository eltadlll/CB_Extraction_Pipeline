# Extraction System — Quick Start Guide

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
