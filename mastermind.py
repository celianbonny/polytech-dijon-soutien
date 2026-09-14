import random
import os


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

# Nom du fichier de stats
NOM_FICHIER_STATS = ".mastermind_stats.txt"

# Chemin complet du fichier de stats, toujours à côté du script.
DOSSIER_SCRIPT = os.path.dirname(os.path.abspath(__file__))
CHEMIN_STATS = os.path.join(DOSSIER_SCRIPT, NOM_FICHIER_STATS)


def generer_code_secret():
    lettres_disponibles = list(COULEURS)
    return [random.choice(lettres_disponibles) for _ in range(TAILLE_CODE)]


def afficher_couleurs():
    print("Couleurs disponibles :")
    for lettre, nom in COULEURS:
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


# ==============
# STATISTIQUES
# ==============

def lire_stats():
    """
    Lit le fichier de stats et renvoie (nombre_parties, score_total).
    """
    if not os.path.exists(CHEMIN_STATS):
        return 0, 0

    with open(CHEMIN_STATS, "r") as fichier:
        contenu = fichier.read().strip()
        if contenu == "":
            return 0, 0
        parties, score = contenu.split(";")
        return int(parties), int(score)


def ecrire_stats(nb_parties, score_total):
    with open(CHEMIN_STATS, "w") as fichier:
        fichier.write(f"{nb_parties};{score_total}")


def reset_stats():
    ecrire_stats(0, 0)
    print("Les statistiques ont été remises à zéro.\n")


def afficher_stats():
    """Affiche les statistiques actuelles."""
    nb_parties, score_total = lire_stats()
    print("----- Statistiques -----")
    print(f"Parties jouées : {nb_parties}")
    print(f"Score total    : {score_total}")
    print("------------------------\n")


# ==============
# MENUS
# ==============

def menu_principal():
    """Menu affiché au lancement du jeu (avant la première partie)."""
    while True:
        print("Que voulez-vous faire ?")
        print("1. Jouer")
        print("2. Remettre à zéro les statistiques")
        print("3. Quitter")
        choix = input("Votre choix : ").strip()

        if choix in ("1", "2", "3"):
            return choix
        print("Choix invalide, réessayez.\n")


def menu_apres_partie():
    """Menu affiché une fois qu'au moins une partie a été terminée."""
    while True:
        print("Que voulez-vous faire ?")
        print("1. Rejouer")
        print("2. Remettre à zéro les statistiques")
        print("3. Quitter")
        choix = input("Votre choix : ").strip()

        if choix in ("1", "2", "3"):
            return choix
        print("Choix invalide, réessayez.\n")


# ==============
# PROGRAMME PRINCIPAL
# ==============

def main():
    print("=== MASTERMIND ===\n")

    a_deja_joue = False  # sert à savoir quel menu afficher (Jouer / Rejouer)
    en_jeu = True

    while en_jeu:
        afficher_stats()

        choix = menu_principal() if not a_deja_joue else menu_apres_partie()
        print()

        if choix == "1":
            score = jouer_partie()
            a_deja_joue = True

            # Mise à jour des statistiques dans le fichier
            nb_parties, score_total = lire_stats()
            nb_parties += 1
            score_total += score
            ecrire_stats(nb_parties, score_total)

            afficher_stats()

        elif choix == "2":
            reset_stats()

        elif choix == "3":
            print("Merci d'avoir joué, à bientôt !")
            en_jeu = False


if __name__ == "__main__":
    main()