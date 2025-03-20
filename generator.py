def formater_jeu(état):
    """
    Formate l'état du jeu en art ASCII.

    Args:
        état (dict): Un dictionnaire contenant l'état du jeu.

    Returns:
        str: Une chaîne de caractères représentant le damier en art ASCII.
    """
    damier = []
    for ligne in range(9):
        ligne_damier = []
        for colonne in range(9):
            # Vérifie si un pion est présent sur cette case
            if (colonne, ligne) == tuple(état["joueurs"][0]["position"]):
                ligne_damier.append("1")  # Pion du joueur 1
            elif (colonne, ligne) == tuple(état["joueurs"][1]["position"]):
                ligne_damier.append("2")  # Pion du joueur 2
            else:
                ligne_damier.append(".")  # Case vide
        damier.append(" ".join(ligne_damier))
    return "\n".join(damier)

def sélectionner_un_coup():
    """
    Demande à l'utilisateur de choisir un coup.

    Returns:
        tuple: Un tuple contenant le type de coup et la position.
    """
    type_coup = input("Quel coup voulez-vous jouer ? (0: déplacer, 1: mur horizontal, 2: mur vertical) : ")
    position = input("Donnez la position du coup (x, y) : ")
    return type_coup, [int(x) for x in position.split(",")]
