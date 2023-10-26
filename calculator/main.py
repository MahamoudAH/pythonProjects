# Importation des modules nécessaires
import os
from art import logo

# Définition des fonctions d'opérations arithmétiques


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 != 0:  # Vérification de la division par zéro
        return n1 / n2
    else:
        print("Error: Division by zero.")
        return None


# Dictionnaire associant les symboles d'opérations aux fonctions correspondantes
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def clear_screen():
    # 'cls' pour Windows, 'clear' pour Mac et Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour obtenir le symbole d'opération de l'utilisateur


def get_operation_symbol():
    for symbol in operations:  # Affichage des options d'opérations
        print(symbol)
    return input("Pick an operation: ")

# Fonction pour obtenir un nombre de l'utilisateur avec gestion d'erreur


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:  # Gestion des entrées non numériques
            print("Invalid input. Please enter a number.")

# Fonction récursive de la calculatrice


def calculator(num1=None):
    print(logo)  # Affichage du logo
    if num1 is None:  # Obtention du premier nombre si nécessaire
        num1 = get_number("What's the first number?: ")
    operation_symbol = get_operation_symbol()  # Obtention du symbole d'opération
    # Obtention du deuxième nombre
    num2 = get_number("What's the next number?: ")
    # Obtention de la fonction d'opération correspondante
    calculation_function = operations.get(operation_symbol)
    if calculation_function:  # Vérification de la validité de l'opération
        answer = calculation_function(num1, num2)
        # Vérification de la validité du résultat (non None en cas de division par zéro)
        if answer is not None:
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            # Demande à l'utilisateur s'il souhaite continuer avec le résultat précédent ou démarrer une nouvelle calculatrice
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
                calculator(answer)  # Appel récursif avec le résultat précédent
            else:
                clear_screen()   # Effacement de l'écran
                calculator()  # Nouvel appel récursif pour démarrer une nouvelle séquence de calculs
        else:
            # Appel récursif pour réessayer avec le même num1 en cas d'erreur
            calculator(num1)
    else:
        print("Invalid operation. Try again.")
        # Appel récursif pour réessayer avec le même num1 en cas d'opération invalide
        calculator(num1)


# Appel initial de la fonction de calculatrice
calculator()
