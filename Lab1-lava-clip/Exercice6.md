***Exercice 6 — Prompt engineering with CLIP***

**Code exécuté :**
```python
prompts = [
    "a cat",
    "a photo of a cat",
    "a photograph showing a cat",
    "an image containing a cat",
    "a domestic animal called a cat"
]

cat_image = Image.open("cat1.jpg").convert("RGB")
inputs = processor(text=prompts, images=cat_image, return_tensors="pt", padding=True)
inputs = {k: v.to(device) for k, v in inputs.items()}

with torch.no_grad():
    outputs = model(**inputs)

probs = outputs.logits_per_image.softmax(dim=1)[0].cpu()
```

**Q17. Les scores sont-ils identiques ?**  
Non, les scores sont très différents d'une formulation à l'autre, variant de 2.23% à 54.16%, alors qu'ils décrivent tous conceptuellement le même animal.

**Q18. Quel prompt donne le score le plus élevé ?**  
Le prompt standard **`"a photo of a cat"`** donne le score le plus élevé avec **54.16%** de probabilité (suivi de *"a photograph showing a cat"* avec 28.78%).

**Q19. Que démontre cette expérience sur la formulation des invites (prompt formulation) ?**  
Cette expérience démontre que :
1. **La conformité à la distribution d'apprentissage est essentielle :** Les légendes web du jeu de données de CLIP utilisaient massivement des formulations naturelles comme *"a photo of a [concept]"*.
2. **Les mots superflus ou de dictionnaire diluent l'attention :** La tournure scolaire *"a domestic animal called a cat"* (2.23%) introduit des tokens secondaires qui réduisent la similarité.
3. Le *Prompt Engineering* et l'agrégation de plusieurs templates (*prompt ensembling*) constituent un levier majeur pour maximiser la précision sans toucher aux poids du modèle.

**Résultat de l'exécution sur mon mac :**
```text
a cat                              : 0.0435 (4.35%)
a photo of a cat                   : 0.5416 (54.16%)
a photograph showing a cat         : 0.2878 (28.78%)
an image containing a cat          : 0.1049 (10.49%)
a domestic animal called a cat     : 0.0223 (2.23%)
```
