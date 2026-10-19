# LAB 1 — Vision-Language Models : CLIP & LLaVA

Ce projet constitue les travaux pratiques sur les modèles multimodaux de vision-langage (**CLIP** et **LLaVA**). Il couvre la représentation conjointe image-texte, la classification zero-shot, l'évaluation de performance, le prompt engineering, la recherche d'images basée sur le texte (*text-to-image retrieval*), ainsi que l'interrogation visuelle (*Visual Question Answering* - VQA).

---

## 📋 Prérequis

- **Python** 3.10 ou supérieur
- **pip** (gestionnaire de paquets Python)
- Accélération matérielle recommandée : Apple Silicon (MPS), GPU NVIDIA (CUDA), ou CPU.

---

## 🚀 Guide d'installation rapide

### 1. Naviguer dans le dossier du TP
Ouvrez votre terminal et placez-vous dans le répertoire du projet :

```bash
cd Lab1-lava-clip
```

### 2. Créer l'environnement virtuel
Créez un environnement virtuel isolé nommé `.venv` :

```bash
python3 -m venv .venv
```

### 3. Activer l'environnement virtuel

- **Sur macOS / Linux :**
  ```bash
  source .venv/bin/activate
  ```

- **Sur Windows (PowerShell) :**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

- **Sur Windows (Invite de commandes cmd) :**
  ```cmd
  .venv\Scripts\activate.bat
  ```

*(Une fois activé, vous devriez voir `(.venv)` au début de votre invite de commande).*

### 4. Mettre à jour pip et installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note :** Les dépendances principales installées sont : `torch`, `torchvision`, `transformers`, `pillow`, `pandas`, `jupyter`, `accelerate`.

---

## 🧪 Lancement des tests et expériences

Deux méthodes sont disponibles pour exécuter le TP :

### Option A : Lancer le script de test automatique (CLI)
Un script de test regroupant les exercices 2 à 8 est prêt à l'emploi. Lancez simplement :

```bash
python run_experiments.py
```

Ce script exécutera successivement :
1. **Initialisation & Détection du matériel** (`mps`, `cuda` ou `cpu`).
2. **Chargement du modèle CLIP** (`openai/clip-vit-base-patch32`).
3. **Exercices 2 & 3** : Calcul des similarités et probabilités texte-image sur une image cible.
4. **Exercice 4** : Prédiction par classification Zero-Shot.
5. **Exercice 5** : Évaluation du modèle sur un échantillon d'images (calcul d'accuracy et tableau de résultats).
6. **Exercice 6** : Impact du Prompt Engineering sur les scores de prédiction.
7. **Exercices 7 & 8** : Indexation et recherche Top-5 d'images par requête textuelle (*Text-to-Image Retrieval*).

---

### Option B : Lancer le Notebook Jupyter interactif
Pour explorer pas à pas le sujet du TP, visualiser les images et interagir avec LLaVA :

```bash
jupyter notebook LAB_CLIP_LLaVA_Full_Lab.ipynb
```
*(ou utilisez l'extension Jupyter directement dans votre IDE).*

---

## 📂 Structure du projet

```text
Lab1-lava-clip/
├── LAB_CLIP_LLaVA_Full_Lab.ipynb  # Notebook complet du TP (Partie énoncé & correction)
├── run_experiments.py             # Script automatisé exécutant les exercices 2 à 8
├── requirements.txt               # Liste des dépendances Python
├── README.md                      # Documentation du projet
├── images/                        # Base d'images pour la recherche text-to-image
├── *.jpg                          # Images de test pour la classification zero-shot
├── Exercice*.md                   # Réponses et fiches de synthèse par exercice
└── MiniProjet.md                  # Conception de l'assistant multimodal (CLIP + LLaVA)
```

---

## 🛑 Désactiver l'environnement virtuel

Lorsque vous avez terminé :

```bash
deactivate
```
