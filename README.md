# M1 Labs — Travaux Pratiques

Ce dépôt contient les travaux pratiques Doctorat en Intelligence Artificielle et Vision-Langage.

## 📂 Liste des TPs disponibles

- **[Lab 1 — Vision-Language Models : CLIP & LLaVA](Lab1-lava-clip/README.md)** : Étude et mise en pratique de modèles vision-langage multimodaux (CLIP, LLaVA, zero-shot classification, recherche d'images, VQA).
- **[Lab 2 — Local AI with Ollama & RAG](Lab2-ollama-rag/LocalAI_Lab/README.md)** : Déploiement et exécution de LLMs locaux (Ollama, Qwen, SmolLM2), prompt engineering, mémoire conversationnelle, sorties structurées (JSON Schema), moteur RAG local (TF-IDF) et assistant web FSTT Flask.
- **[Lab 3 — AI Agents & Workflows with LangGraph](Lab3-langGraph/README.md)** : Conception et orchestration de flux multi-agents à états (StateGraph), routage conditionnel d'intentions, exécution sécurisée d'outils (AST calculator, datetime), persistance de la mémoire conversationnelle (`MemorySaver`) et projet Capstone Assistant Universitaire.

---

## 🚀 Démarrage rapide pour Lab 1
*(Consultez le [README.md de Lab1-lava-clip](Lab1-lava-clip/README.md) pour les détails complets)*

```bash
cd Lab1-lava-clip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_experiments.py
```

---

## 🚀 Démarrage rapide pour Lab 2 — Local AI with Ollama & RAG
*(Consultez le [README.md de Lab2-ollama-rag](Lab2-ollama-rag/LocalAI_Lab/README.md) et le notebook [Local_AI_Ollama_Lab_Statement.ipynb](Lab2-ollama-rag/Local_AI_Ollama_Lab_Statement.ipynb))*

### 1. Démarrer le serveur Ollama et télécharger les modèles
```bash
ollama serve
ollama pull qwen2.5:0.5b
ollama pull smollm2:135m
```

### 2. Installer les dépendances Python
```bash
cd Lab2-ollama-rag
pip install flask requests psutil pandas matplotlib numpy
```

### 3. Lancer l'assistant Web FSTT
```bash
cd LocalAI_Lab/source
python3 app.py
```
Ouvrez ensuite votre navigateur sur **http://127.0.0.1:5001**.

### 4. Lancer le chatbot en console
```bash
cd LocalAI_Lab/source
python3 chatbot.py
```

### 5. Livrables & Rapport
- 📄 Rapport : [report.md](Lab2-ollama-rag/LocalAI_Lab/report.md) & [report.docx](Lab2-ollama-rag/LocalAI_Lab/report.docx) & [report.pdf](Lab2-ollama-rag/LocalAI_Lab/report.pdf)
- 📓 Notebook complet : [Local_AI_Ollama_Lab_Statement.ipynb](Lab2-ollama-rag/Local_AI_Ollama_Lab_Statement.ipynb)
- 🖼️ Captures d'écran : `Lab2-ollama-rag/LocalAI_Lab/screenshots/`

---

## 🚀 Démarrage rapide pour Lab 3 — AI Agents & Workflows with LangGraph
*(Consultez le [README.md de Lab3-langGraph](Lab3-langGraph/README.md), le rapport [REPORT.md](Lab3-langGraph/REPORT.md) et le notebook [langgraph_lab.ipynb](Lab3-langGraph/langgraph_lab.ipynb))*

### 1. Naviguer dans le dossier du TP et créer l'environnement virtuel
```bash
cd Lab3-langGraph
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer la clé d'API (OpenAI)
```bash
export OPENAI_API_KEY="votre_cle_api"
```

### 4. Lancer la démonstration de l'Assistant Universitaire en console
```bash
python3 main.py
```

### 5. Lancer le Notebook Jupyter
```bash
jupyter notebook langgraph_lab.ipynb
```

### 6. Livrables & Rapport
- 📄 Rapport académique complet : [REPORT.md](Lab3-langGraph/REPORT.md)
- 📓 Notebook complété et exécuté : [langgraph_lab.ipynb](Lab3-langGraph/langgraph_lab.ipynb)
- 🏗️ Schéma d'architecture Mermaid : [architecture.mmd](Lab3-langGraph/architecture.mmd)
- 🖼️ Captures d'écran de l'exécution : `Lab3-langGraph/screenshots/`
- 💻 Code source modulaire : `Lab3-langGraph/src/` (`state.py`, `tools.py`, `agents.py`, `graph.py`)

