import random


# ==============
# CONFIGURATION
# ==============

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




def generer_code_secret():
    lettres_disponibles = list(COULEURS.keys())
    return [random.choice(lettres_disponibles) for _ in range(TAILLE_CODE)]


def afficher_couleurs():
    print("Couleurs disponibles :")
    for lettre, nom in COULEURS.items():
        print(f"  {lettre} = {nom}")
    print()


def saisir_essai():
    while True:
        essai = input(f"Votre essai ({TAILLE_CODE} lettres) : ").strip().upper()
        if len(essai) == TAILLE_CODE:
            return list(essai)
        print(f"Erreur : il faut exactement {TAILLE_CODE} lettres.")


def comparer(code_secret, essai):
    """
    Renvoie (nb_correct, nb_partiel) :
    - correct : bonne couleur ET bon emplacement
    - partiel : bonne couleur mais mauvais emplacement
    """
    nb_correct = 0
    secret_restant = []
    essai_restant = []

    for i in range(len(code_secret)):
        if code_secret[i] == essai[i]:
            nb_correct += 1
        else:
            secret_restant.append(code_secret[i])
            essai_restant.append(essai[i])

    nb_partiel = 0
    for couleur in essai_restant:
        if couleur in secret_restant:
            nb_partiel += 1
            secret_restant.remove(couleur)

    return nb_correct, nb_partiel


def jouer_partie():
    code_secret = generer_code_secret()
    afficher_couleurs()

    for tentative in range(1, MAX_ESSAIS + 1):
        print(f"--- Essai {tentative}/{MAX_ESSAIS} ---")
        essai = saisir_essai()
        nb_correct, nb_partiel = comparer(code_secret, essai)
        print(f"Correct : {nb_correct} | Partiel : {nb_partiel}\n")

        if nb_correct == TAILLE_CODE:
            score = MAX_ESSAIS - tentative
            print(f"Bravo ! Code trouvé en {tentative} essai(s). Score : {score}")
            return score

    print(f"Perdu ! Le code secret était : {''.join(code_secret)}. Score : 0")
    return 0



if __name__ == "__main__":
    jouer_partie()