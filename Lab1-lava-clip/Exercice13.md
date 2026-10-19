***Part D — CLIP vs LLaVA***

***Exercice 13 — Expérience comparative***

**Tableau comparatif complété :**

| Propriété | CLIP | LLaVA |
|:---|:---|:---|
| **Entrée (Input)** | Image + Paires/Listes de textes courts (labels/prompts) | Image + Question/Instruction en langage naturel |
| **Sortie principale (Main output)** | Score scalaire / Matrice de similarité cosinus | Texte libre et structuré généré de manière autorégressive |
| **Classification Zero-shot** | **Idéale, instantanée et calibrée** (produit scalaire) | Coûteuse en calcul, verbeuse (via prompting) |
| **Recherche d'images (Retrieval)** | **Native** (espace latent partagé) | Inadaptée (pas de représentation vectorielle unifiée) |
| **Génération de texte** | **Impossible** (modèle purement discriminatif) | **Excellente** (réponses, résumés, explications détaillées) |
| **VQA** | Limité à du choix multiple fermé | **Excellent** (raisonnement interactif ouvert) |
| **Réponse ouverte (Open-ended)** | Non | **Oui** |

---

**Q33. Quel modèle est le mieux adapté à la classification d'images ?**  
**CLIP.** Il est rapide, léger, produit des scores probabilistes directement calibrés et permet de comparer une image à des milliers de classes en quelques millisecondes par simple produit matriciel.

**Q34. Quel modèle est le meilleur pour la description d'images ?**  
**LLaVA.** Il dispose d'un décodeur de langage complet capable de formuler des paragraphes descriptifs riches, détaillant la lumière, les textures, les actions et le contexte.

**Q35. Quel modèle est le meilleur pour le VQA ?**  
**LLaVA.** Il comprend la syntaxe complexe des questions en langage naturel, déduit des liens de cause à effet et formule des réponses nuancées.

**Q36. Expliquez la différence fondamentale entre CLIP et LLaVA.**  
La différence fondamentale réside dans leur **architecture et leur objectif d'apprentissage** :
- **CLIP est un modèle discriminatif à double encodeur (*Dual-Encoder*) :** Il n'a aucun générateur de texte. Il projette des images et des phrases dans un espace géométrique commun pour mesurer une proximité sémantique.
- **LLaVA est un modèle génératif autorégressif multimodal (*Vision-to-Language*) :** Il réutilise l'encodeur visuel de CLIP pour extraire des jetons visuels, puis les injecte directement dans un grand modèle de langage (LLM) qui produit une réponse textuelle fluide.
