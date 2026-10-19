***Part C — LLaVA***

***Exercice 9 — Architecture***

**Schéma complété :**
```text
Image
  |
  v
CLIP Vision Encoder (ViT-L/14)
  |
  v
Projection Layer (MLP Adapter)   <--- Couche de projection / Alignement multimodal
  |
  v
Language Model (Vicuna / LLaMA)
  |
  v
Text Response
```

**Q24. Quel est le rôle de l'encodeur visuel (vision encoder) ?**  
L'encodeur visuel (généralement `CLIP ViT-L/14`) traite l'image brute en la découpant en une grille de patchs et extrait un ensemble dense de représentations visuelles (*visual tokens*), capturant les formes, les textures, les couleurs et les relations spatiales.

**Q25. Pourquoi une couche de projection (projection layer / MLP adapter) est-elle indispensable ?**  
La couche de projection est indispensable pour deux raisons :
1. **Alignement dimensionnel :** L'encodeur visuel produit des vecteurs de dimension 1024 (pour ViT-L), alors que le modèle de langage attend des tokens en dimension 4096 (pour LLaMA/Vicuna 7B).
2. **Alignement sémantique :** Elle agit comme un traducteur en convertissant les caractéristiques spatiales de l'image en « pseudo-mots » (*visual word embeddings*) que le modèle de langage peut ingérer de la même manière que des tokens textuels.

**Q26. Quel est le rôle du modèle de langage (language model) ?**  
Le modèle de langage (LLM comme Vicuna ou LLaMA) est le moteur de raisonnement du système. Il concatène les tokens visuels projetés et les tokens de la question textuelle, applique son mécanisme d'attention autorégressive pour comprendre le contexte global, et génère la réponse mot par mot en langage naturel.
