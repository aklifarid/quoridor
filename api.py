import requests

# URL de base de l'API du serveur de jeu
BASE_URL = "https://pax.ulaval.ca/quondor/api/n25"

def lister_parties(idul, secret):
    """
    Liste les parties existantes sur le serveur.

    Args:
        idul (str): Ton IDUL.
        secret (str): Ton jeton d'authentification.

    Returns:
        dict: Un dictionnaire contenant la liste des parties.
    """
    # Fait une requête GET pour lister les parties
    response = requests.get(f"{BASE_URL}/parties", auth=(idul, secret))
    
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        return response.json()  # Retourne les données JSON de la réponse
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return None

def débuter_partie(idul, secret):
    """
    Débute une nouvelle partie sur le serveur.

    Args:
        idul (str): Ton IDUL.
        secret (str): Ton jeton d'authentification.

    Returns:
        dict: Un dictionnaire contenant les informations de la nouvelle partie.
    """
    # Fait une requête POST pour débuter une nouvelle partie
    response = requests.post(f"{BASE_URL}/parties", auth=(idul, secret))
    
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        return response.json()  # Retourne les données JSON de la réponse
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return None

def jouer_coup(id_partie, idul, secret, coup):
    """
    Joue un coup dans une partie existante.

    Args:
        id_partie (str): L'identifiant de la partie.
        idul (str): Ton IDUL.
        secret (str): Ton jeton d'authentification.
        coup (dict): Un dictionnaire représentant le coup à jouer.

    Returns:
        dict: Un dictionnaire contenant l'état mis à jour de la partie.
    """
    # Fait une requête PUT pour jouer un coup
    response = requests.put(f"{BASE_URL}/parties/{id_partie}", auth=(idul, secret), json=coup)
    
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        return response.json()  # Retourne les données JSON de la réponse
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return None
