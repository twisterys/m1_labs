***Part B — CLIP Image Retrieval***

***Exercice 7 — Construire une base d'images***
***Exercice 8 — Recherche image par le texte (Text-to-Image Retrieval)***

**Code exécuté :**
```python
# 1. Calcul des embeddings normalisés de la galerie (20 images)
image_paths = sorted([os.path.join("images", f) for f in os.listdir("images") if f.endswith(('.jpg', '.png', '.jpeg'))])
image_embeddings = []
for path in image_paths:
    img = Image.open(path).convert("RGB")
    inp = processor(images=img, return_tensors="pt").to(device)
    with torch.no_grad():
        emb = model.get_image_features(**inp)
        emb = emb / emb.norm(dim=-1, keepdim=True)
        image_embeddings.append(emb.cpu())
image_embeddings = torch.cat(image_embeddings, dim=0)

# 2. Embedding normalisé de la requête textuelle
QUERY = "a person playing football"
text_inputs = processor(text=[QUERY], return_tensors="pt").to(device)
with torch.no_grad():
    text_emb = model.get_text_features(**text_inputs)
    text_emb = text_emb / text_emb.norm(dim=-1, keepdim=True)
    text_emb = text_emb.cpu()

# 3. Similarité cosinus & Top-5
similarities = (image_embeddings @ text_emb.T).squeeze(1)
topk = torch.topk(similarities, k=5)
```

**Q20. Quelle est l'image la plus similaire ?**  
L'image la plus similaire est **`images/football.jpg`** avec la similarité cosinus la plus élevée (**0.2899**).

**Q21. Est-elle sémantiquement pertinente ?**  
Oui, parfaitement pertinente. Le modèle a correctement identifié l'image de football parmi 20 images contenant des scènes très variées (animaux, voitures, paysages, nourriture, bâtiments).

**Q22. Pourquoi cette méthode ne nécessite-t-elle pas d'étiquettes d'images ?**  
Parce que la recherche s'opère par **similarité géométrique continue** dans un espace latent multimodal partagé. L'image est encodée directement sous forme de caractéristiques visuelles denses, sans métadonnées textuelles associées. La requête textuelle est projetée dans le même repère vectoriel. Il suffit ensuite de calculer le produit scalaire (similarité cosinus) entre les deux vecteurs.

**Q23. Donnez une application concrète de la recherche sémantique d'images dans le monde réel.**  
- **Moteurs de recherche d'albums photo (Google Photos, Apple Photos) :** Permet de rechercher des photos personnelles avec des requêtes libres (*"pique-nique en montagne"*, *"chien sur la plage"*) sans aucun tag manuel.
- **E-commerce visuel :** Recherche d'articles vestimentaires à partir de descriptions en langage naturel (*"robe d'été fleurie vintage"*).
- **Vidéosurveillance et police scientifique :** Retrouver un événement dans des milliers d'heures de vidéo à partir d'un signalement textuel.

**Résultat de l'exécution sur mon mac :**
```text
Total images in gallery: 20

=== Top-5 Retrieved Images for Query: 'a person playing football' ===
Rank 1: images/football.jpg            | Cosine Similarity: 0.2899
Rank 2: images/horse.jpg               | Cosine Similarity: 0.2257
Rank 3: images/person_portrait.jpg     | Cosine Similarity: 0.2092
Rank 4: images/basketball.jpg          | Cosine Similarity: 0.2002
Rank 5: images/dog.jpg                 | Cosine Similarity: 0.1972
```
