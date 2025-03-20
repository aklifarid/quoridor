from api import débuter_partie, jouer_coup
from generator import formater_jeu, sélectionner_un_coup

def main():
    """
    Fonction principale du programme. Gère la boucle de jeu.
    """
    # Informations d'authentification
    idul = "ton-idul"  # Remplace par ton IDUL
    secret = "ton-jeton-secret"  # Remplace par ton jeton secret

    # Débuter une nouvelle partie
    print("Début d'une nouvelle partie...")
    partie = débuter_partie(idul, secret)
    if not partie:
        print("Erreur : Impossible de débuter une nouvelle partie.")
        return

    # Boucle de jeu
    while True:
        # Afficher l'état du jeu
        print("\nÉtat du jeu :")
        print(formater_jeu(partie["état"]))

        # Demander à l'utilisateur de jouer
        print("\nÀ toi de jouer !")
        type_coup, position = sélectionner_un_coup()

        # Envoyer le coup au serveur
        print(f"Jouer le coup : type={type_coup}, position={position}")
        partie = jouer_coup(partie["id"], idul, secret, {"type": type_coup, "position": position})
        if not partie:
            print("Erreur : Impossible de jouer ce coup.")
            break

        # Vérifier si la partie est terminée
        if partie.get("gagnant"):
            print(f"Partie terminée ! Le gagnant est : {partie['gagnant']}")
            break

if __name__ == "__main__":
    main()
