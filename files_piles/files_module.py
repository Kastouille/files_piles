# /$$      /$$                 /$$           /$$                 /$$$$$$$$ /$$ /$$          
#| $$$    /$$$                | $$          | $$                | $$_____/|__/| $$          
#| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$   /$$| $$  /$$$$$$       | $$       /$$| $$  /$$$$$$ 
#| $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$  | $$| $$ /$$__  $$      | $$$$$   | $$| $$ /$$__  $$
#| $$  $$$| $$| $$  \ $$| $$  | $$| $$  | $$| $$| $$$$$$$$      | $$__/   | $$| $$| $$$$$$$$
#| $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$_____/      | $$      | $$| $$| $$_____/
#| $$ \/  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$      | $$      | $$| $$|  $$$$$$$
#|__/     |__/ \______/  \_______/ \______/ |__/ \_______/      |__/      |__/|__/ \_______/
#
#Implémentation des files dans Python par les listes
#Les files sont de la forme : Tête-File-Queue
version = 1.0

def CREER_FILE_VIDE() -> list:
    """
    Créer une file vide
    Syntaxe:
        CREER_FILE_VIDE() => []
    """
    return []

def ENFILER(F, e):
    """
    Emfile l'élément e à la queue la file F
    Syntaxe:
        EMFILER(File, 'test')
    """
    F.append(e)
    
def DEFILER(F):
    """
    Défile le dernier élément de la file P
    Syntaxe:
        DEFILER(file)
    """
    assert EST_VIDE(F) == False, 'Impossible de défiler une file vide !'
    return F.pop(index = 0)
    
def EST_VIDE(F) -> bool:
    """
    Retourne un booléen selon l'état de la file (vide ou pas)
    Syntaxe:
        EST_VIDE(file) => True/False
    """
    return len(F) == 0

def AFFICHER_FILE(F) -> list:
    """
    Affiche le sens d'une file et la retourne
    Syntaxe:
        AFFICHER_FILE(File) =>  (Tête -----> Queue)
                            =>  [1, 2, 3, 4]
    """
    assert type(F) == list, 'La file doit être sous le type de liste'
    print("Tête -----> Queue")
    return F