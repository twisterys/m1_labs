***Exercice 12 — Hallucination Visuelle***

**Protocole expérimental :**  
Une image ne contenant aucun vélo a été utilisée ([image.jpg](file:///Users/yassir/Desktop/m1_labs/Lab1-lava-clip/image.jpg) - Chien).

**Dialogue observé avec le modèle :**

1. *[Question neutre]* : **Is there a bicycle in this image?**  
   *[Réponse LLaVA]* : **No, there is no bicycle visible in this image. The scene only shows a dog.**

2. *[Question orientée / biaisée]* : **What color is the bicycle?**  
   *[Réponse LLaVA (Hallucination)]* : **The bicycle appears to be red with black handlebars, parked in the background.**

3. *[Question orientée / biaisée]* : **Where is the bicycle located?**  
   *[Réponse LLaVA (Hallucination)]* : **It is leaning against a wall on the left side behind the dog.**

---

**Q29. Le vélo existe-t-il réellement dans l'image ?**  
Non, absolument pas. L'image ne contient aucun vélo.

**Q30. LLaVA a-t-il inventé des informations ?**  
Oui. Après avoir correctement répondu « Non » à la première question neutre, LLaVA a inventé des détails inexistants (couleur rouge, guidon noir, position contre le mur) dès que l'utilisateur a posé une question orientée présupposant l'existence du vélo.

**Q31. Qu'est-ce qu'une hallucination visuelle ?**  
Une hallucination visuelle se produit lorsqu'un modèle vision-langage génère du texte affirmant la présence d'objets, de couleurs, d'attributs ou de relations qui ne sont **pas étayés par l'information visuelle réelle de l'image**.

**Q32. Pourquoi un modèle multimodal peut-il halluciner ?**  
Les hallucinations visuelles s'expliquent par trois causes principales :
1. **Poids excessif des a priori linguistiques (*Language Prior Dominance*) :** Le grand modèle de langage (LLM) sous-jacent a été entraîné sur d'immenses corpus textuels où la question « De quelle couleur est X ? » est presque toujours suivie d'un nom de couleur. Le réflexe autorégressif du LLM l'emporte alors sur les signaux d'attention visuelle.
2. **Biais de complaisance / servilité (*Sycophancy*) :** Le modèle a tendance à considérer que la question posée par l'utilisateur repose sur une vérité acquise et cherche à y répondre plutôt qu'à la contredire.
3. **Corrélations statistiques fréquentes :** Le modèle prédit des objets souvent associés dans son jeu d'entraînement (ex: rue $\rightarrow$ vélo, salon $\rightarrow$ table), même s'ils sont absents de l'image.
