import random

# Couleurs disponibles
COULEURS = {
    "R": "Rouge",
    "V": "Vert",
    "B": "Bleu",
    "J": "Jaune",
    "M": "Mauve",
    "N": "Noir",
}

TAILLE_CODE = 4     # nombre d'éléments dans le code secret
MAX_ESSAIS = 12     # nombre maximal de tentatives



lettres_disponibles = list(COULEURS.keys())
code_secret = [random.choice(lettres_disponibles) for _ in range(TAILLE_CODE)]


print("Couleurs disponibles :")
for lettre, nom in COULEURS.items():
    print(f"  {lettre} = {nom}")
print()


trouve = False

for tentative in range(1, MAX_ESSAIS + 1):
    print(f"--- Essai {tentative}/{MAX_ESSAIS} ---")

    # Saisie du joueur, avec vérification de la longueur
    while True:
        essai = input(f"Votre essai ({TAILLE_CODE} lettres) : ").strip().upper()
        if len(essai) == TAILLE_CODE:
            break
        print(f"Erreur : il faut exactement {TAILLE_CODE} lettres.")
    essai = list(essai)

    # Comptage des "Correct" (bonne couleur ET bonne position)
    nb_correct = 0
    secret_restant = []
    essai_restant = []
    for i in range(len(code_secret)):
        if code_secret[i] == essai[i]:
            nb_correct += 1
        else:
            # on garde de côté ce qui n'a pas matché, pour l'étape suivante
            secret_restant.append(code_secret[i])
            essai_restant.append(essai[i])

    # Comptage des "Partiel" (bonne couleur, mauvaise position)
    nb_partiel = 0
    for couleur in essai_restant:
        if couleur in secret_restant:
            nb_partiel += 1
            secret_restant.remove(couleur)  # pour ne pas compter deux fois le même pion

    print(f"Correct : {nb_correct} | Partiel : {nb_partiel}\n")

    if nb_correct == TAILLE_CODE:
        trouve = True
        break


if trouve:
    score = MAX_ESSAIS - tentative
    print(f"Bravo ! Code trouvé en {tentative} essai(s). Score : {score}")
else:
    print(f"Perdu ! Le code secret était : {''.join(code_secret)}. Score : 0")