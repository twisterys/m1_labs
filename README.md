# M1 Labs — Travaux Pratiques

Ce dépôt contient les travaux pratiques Doctorat en Intelligence Artificielle et Vision-Langage.

## 📂 Liste des TPs disponibles

- **[Lab 1 — Vision-Language Models : CLIP & LLaVA](Lab1-lava-clip/README.md)** : Étude et mise en pratique de modèles vision-langage multimodaux (CLIP, LLaVA, zero-shot classification, recherche d'images, VQA).

---

## 🚀 Démarrage rapide pour Lab 1

### 1. Se positionner dans le dossier du TP
```bash
cd Lab1-lava-clip
```

### 2. Créer et activer l'environnement virtuel
```bash
# Création
python3 -m venv .venv

# Activation (macOS / Linux)
source .venv/bin/activate

# Activation (Windows)
# .venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Lancer le test
```bash
python run_experiments.py
```

Pour plus de détails, consultez le [README.md de Lab1-lava-clip](Lab1-lava-clip/README.md).
