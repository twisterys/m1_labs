# M1 Labs — Travaux Pratiques

Ce dépôt contient les travaux pratiques Doctorat en Intelligence Artificielle et Vision-Langage.

## 📂 Liste des TPs disponibles

- **[Lab 1 — Vision-Language Models : CLIP & LLaVA](Lab1-lava-clip/README.md)** : Étude et mise en pratique de modèles vision-langage multimodaux (CLIP, LLaVA, zero-shot classification, recherche d'images, VQA).
- **[Lab 2 — Local AI with Ollama & RAG](Lab2-ollama-rag/LocalAI_Lab/README.md)** : Déploiement et exécution de LLMs locaux (Ollama, Qwen, SmolLM2), prompt engineering, mémoire conversationnelle, sorties structurées (JSON Schema), moteur RAG local (TF-IDF) et assistant web FSTT Flask.

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

