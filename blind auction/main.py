import os
from art import logo


def gather_bids():
    """
    Recueille les offres des utilisateurs et les stocke dans un dictionnaire.

    Retourne:
        dict: Un dictionnaire contenant les noms des utilisateurs comme clés et leurs offres comme valeurs.
    """
    auction_data = {}  # Initialisation du dictionnaire pour stocker les données de l'enchère

    while True:
        # Recueillir le nom et l'offre de l'utilisateur
        name = input("Quel est votre nom? ")
        bid = int(input("Quelle est votre offre? "))

        # Stocker l'offre dans le dictionnaire
        auction_data[name] = bid

        # Demander s'il y a d'autres enchérisseurs
        more_bidders = input(
            "Y a-t-il d'autres enchérisseurs? Tapez 'yes' ou 'no': ").lower()

        # Si l'utilisateur répond "no", sortir de la boucle
        if more_bidders == "no":
            break

        # Effacer l'écran du terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    return auction_data


def find_winner(auction):
    """
    Trouve et retourne le nom et l'offre du gagnant de l'enchère.

    Args:
        auction (dict): Un dictionnaire contenant les noms des utilisateurs comme clés et leurs offres comme valeurs.

    Retourne:
        tuple: Le nom et l'offre du gagnant.
    """
    # Trouver le nom avec l'offre la plus élevée
    winner_name = max(auction, key=auction.get)
    winner_bid = auction[winner_name]

    return winner_name, winner_bid


print(logo)
# Recueillir les offres des utilisateurs
auction_data = gather_bids()

# Trouver le gagnant et son offre
winner_name, winner_bid = find_winner(auction_data)

# Afficher le gagnant et son offre
print(f"Le gagnant est {winner_name} avec une offre de ${winner_bid}")
