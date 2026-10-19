***Exercice 5 — Évaluation de CLIP***


**Q14. Quelle est l'exactitude (accuracy) obtenue ?**
L'exactitude obtenue est de 80.0% 
**Q15. Quelles images sont mal classées ?**
Deux images ont été mal prédites :
horse2.jpg (vrai : horse) prédit comme airplane avec probabilité 0.5096.
airplane1.jpg (vrai : airplane) prédit comme car avec probabilité 0.5455.
**Q16. Donnez au moins deux raisons possibles pour ces erreurs.**
Biais de contexte / fond dominant : Le cheval galopant dans un champ ouvert avec un grand ciel bleu présente une signature visuelle (horizon dégagé, textures de ciel) que CLIP associe statistiquement aux photos aériennes (airplane).
Ambiguïté géométrique à basse résolution : Une photo d'avion au sol ou de face partage des structures métalliques, des roues et une silhouette industrielle proches de certains véhicules terrestres (car), surtout après le découpage en patchs grossiers de 32×32 pixels de l'architecture ViT-B/32.

=== Evaluation Results Table ===
        Image   Actual Class Predicted Class Probability  Correct
     dog1.jpg            dog             dog      0.9900     True
     dog2.jpg            dog             dog      0.9959     True
     cat1.jpg            cat             cat      0.9914     True
     cat2.jpg            cat             cat      0.9898     True
     car1.jpg            car             car      0.9784     True
     car2.jpg            car             car      0.9902     True
   horse1.jpg          horse           horse      0.9991     True
   horse2.jpg          horse        airplane      0.5096    False
    bird1.jpg           bird            bird      0.9985     True
airplane1.jpg       airplane             car      0.5455    False

Accuracy: 0.80 (8/10 = 80.0%)



