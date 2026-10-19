***Exercice 11 — Visual Question Answering (VQA)***

**Tableau d'évaluation VQA (5 images × 5 questions = 25 questions) :**

| Image | Question | Réponse LLaVA | Évaluation Humaine |
|:---|:---|:---|:---|
| `football.jpg` | How many people are visible? | One person is clearly visible. | **Correct** |
| `football.jpg` | What sport is being played? | Soccer (football). | **Correct** |
| `football.jpg` | What object is near the person's feet? | A soccer ball. | **Correct** |
| `football.jpg` | Where is the scene taking place? | On a grass sports field. | **Correct** |
| `football.jpg` | What color is the jersey? | Blue and white. | **Correct** |
| `basketball.jpg` | How many people are visible? | Two players on the court. | **Correct** |
| `basketball.jpg` | What objects can you see? | A basketball, hoop, and backboard. | **Correct** |
| `basketball.jpg` | What are the players doing? | Competing for the ball under the rim. | **Correct** |
| `basketball.jpg` | Where is the hoop located? | At the top right of the court. | **Correct** |
| `basketball.jpg` | What is the floor made of? | Polished hardwood court. | **Correct** |
| `classroom.jpg` | How many people are visible? | Approximately 12 students. | **Incorrect** (15 présents) |
| `classroom.jpg` | What is visible on the board? | Mathematical equations and notes. | **Correct** |
| `classroom.jpg` | Where are the people? | Sitting at wooden school desks. | **Correct** |
| `classroom.jpg` | What are they doing? | Listening and taking notes. | **Correct** |
| `classroom.jpg` | Is there a clock on the wall? | Yes, above the chalkboard. | **Correct** |
| `car.jpg` | What color is the car? | Glossy red. | **Correct** |
| `car.jpg` | What type of vehicle is it? | A sports coupe. | **Correct** |
| `car.jpg` | Where is the car parked? | On an asphalt road near the coast. | **Correct** |
| `car.jpg` | Is the headlights turned on? | No, they appear off. | **Correct** |
| `car.jpg` | Read the license plate letters. | ABC-1234 | **Incorrect** (texte flou) |
| `coffee.jpg` | What beverage is shown? | A cup of cappuccino with latte art. | **Correct** |
| `coffee.jpg` | What shape is the latte art? | A heart or leaf pattern. | **Correct** |
| `coffee.jpg` | What is next to the cup? | A ceramic saucer and a metal spoon. | **Correct** |
| `coffee.jpg` | What surface is it resting on? | A rustic wooden tabletop. | **Correct** |
| `coffee.jpg` | Are there coffee beans visible? | Yes, scattered roasted beans. | **Correct** |

**Calcul de l'exactitude VQA :**
$$Accuracy = \frac{N_{correct}}{N_{total}} = \frac{23}{25} = 0.92 \quad (92.0\%)$$

**Q27. Quelle est l'exactitude VQA obtenue ?**  
L'exactitude VQA obtenue est de **92.0%** (23 réponses correctes sur 25).

**Q28. Quels types de questions sont difficiles pour LLaVA ?**  
LLaVA éprouve des difficultés sur trois types de tâches :
1. **Le comptage précis d'objets multiples et petits (*Fine-grained Counting*) :** Estimer avec exactitude le nombre de personnes dans une classe ou une foule compacte.
2. **La lecture de texte (*OCR fine*) :** Lire des petits caractères, des logos ou des plaques d'immatriculation floues, car le découpage en patchs compresse la haute fréquence visuelle.
3. **Les relations spatiales fines en 3D :** Déterminer précisément quel objet est en avant ou en arrière-plan dans des perspectives complexes.
