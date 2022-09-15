#  /$$      /$$                 /$$           /$$                 /$$$$$$$  /$$ /$$          
# | $$$    /$$$                | $$          | $$                | $$__  $$|__/| $$          
# | $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$   /$$| $$  /$$$$$$       | $$  \ $$ /$$| $$  /$$$$$$ 
# | $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$  | $$| $$ /$$__  $$      | $$$$$$$/| $$| $$ /$$__  $$
# | $$  $$$| $$| $$  \ $$| $$  | $$| $$  | $$| $$| $$$$$$$$      | $$____/ | $$| $$| $$$$$$$$
# | $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$_____/      | $$      | $$| $$| $$_____/
# | $$ \/  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$      | $$      | $$| $$|  $$$$$$$
# |__/     |__/ \______/  \_______/ \______/ |__/ \_______/      |__/      |__/|__/ \_______/
#
#Implémentation des piles dans Python par les listes
#Les piles sont de la forme Pile-Sommet
version = 1.0

def CREER_PILE_VIDE() -> list:
    """
    Créer une pile vide
    Syntaxe:
        CREER_PILE_VIDE() => []
    """
    return []

def EMPILER(P, e):
    """
    Empile l'élément e sur la pile P
    Syntaxe:
        EMPILER(Pile, 'test')
    """
    P.append(e)
    
def DEPILER(P):
    """
    Dépile le dernier élément de la pile P
    Syntaxe:
        DEPILER(Pile)
    """
    assert EST_VIDE(P) == False, 'Impossible de dépiler une pile vide !'
    return P.pop()
    
def EST_VIDE(P) -> bool:
    """
    Retourne un booléen selon l'état de la liste (vide ou pas)
    Syntaxe:
        EST_VIDE(Pile) => True/False
    """

    return len(P) == 0

def AFFICHER_PILE(P:list) -> list:
    """
    Affiche le sens d'une pile et la retourne
    Syntaxe:
        AFFICHER_PILE(Pile) =>  (Pile -----> Sommet)
                            =>  [1, 2, 3, 4]
    """
    assert type(P) == list, 'La pile doit être sous le type de liste'
    print("Pile -----> Sommet")
    return P