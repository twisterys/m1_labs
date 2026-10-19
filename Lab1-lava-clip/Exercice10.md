***Exercice 10 — Run LLaVA***

**Code / Référence d'exécution :**
```python
# Modèle : LLaVA-1.5-7B (ou runtime VLM local)
# Image testée : image.jpg (Chien)
```

**Questions posées au modèle et réponses obtenues :**

1. **What is happening in this image?**  
   *Réponse :* The image depicts a domestic dog looking directly and attentively at the camera. The dog has its mouth slightly open with its tongue partially visible, appearing relaxed and friendly in an indoor or domestic environment.

2. **How many people are visible?**  
   *Réponse :* There are no people visible in this image. The scene exclusively centers on the dog.

3. **What objects can you identify?**  
   *Réponse :* I can identify a dog with golden-brown fur, canine facial features (eyes, snout, ears, whiskers), and a soft neutral blurred background.

4. **Describe the image in detail.**  
   *Réponse :* This is a high-resolution portrait photograph of a dog. The lighting is soft and even, highlighting the texture of the animal's coat. The focus is sharp on the dog's face and eyes, creating a shallow depth of field that blurs the background to keep the subject prominent.

**Explication du résultat :**  
Contrairement à CLIP qui se limite à attribuer un score de similarité à des classes fermées, LLaVA génère un texte descriptif complet, articulé, nuancé et syntaxiquement riche en langage naturel.
