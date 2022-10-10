# ,-.----.                                                                                                                                     
# \    /  \             ,--,                                     ,---,.           ,--,                                                ,----,   
# |   :    \   ,--,   ,--.'|                                   ,'  .' |  ,--,   ,--.'|                                              .'   .' \  
# |   |  .\ :,--.'|   |  | :                                 ,---.'   |,--.'|   |  | :                                            ,----,'    | 
# .   :  |: ||  |,    :  : '               .--.--.           |   |   .'|  |,    :  : '               .--.--.                .---. |    :  .  ; 
# |   |   \ :`--'_    |  ' |      ,---.   /  /    '          :   :  :  `--'_    |  ' |      ,---.   /  /    '             /.  ./| ;    |.'  /  
# |   : .   /,' ,'|   '  | |     /     \ |  :  /`./          :   |  |-,,' ,'|   '  | |     /     \ |  :  /`./           .-' . ' | `----'/  ;   
# ;   | |`-' '  | |   |  | :    /    /  ||  :  ;_            |   :  ;/|'  | |   |  | :    /    /  ||  :  ;_            /___/ \: |   /  ;  /    
# |   | ;    |  | :   '  : |__ .    ' / | \  \    `.         |   |   .'|  | :   '  : |__ .    ' / | \  \    `.         .   \  ' .  ;  /  /-,   
# :   ' |    '  : |__ |  | '.'|'   ;   /|  `----.   \        '   :  '  '  : |__ |  | '.'|'   ;   /|  `----.   \         \   \   ' /  /  /.`|   
# :   : :    |  | '.'|;  :    ;'   |  / | /  /`--'  /        |   |  |  |  | '.'|;  :    ;'   |  / | /  /`--'  /          \   \  ./__;      :   
# |   | :    ;  :    ;|  ,   / |   :    |'--'.     /         |   :  \  ;  :    ;|  ,   / |   :    |'--'.     /            \   \ |   :    .'    
# `---'.|    |  ,   /  ---`-'   \   \  /   `--'---'          |   | ,'  |  ,   /  ---`-'   \   \  /   `--'---'              '---";   | .'       
#   `---`     ---`-'             `----'                      `----'     ---`-'             `----'                               `---'          

class Files:
    """
    Implémentation de la classe file en python
    Syntaxe:
        exemple = Files()
    """
    
    def __init__(self):
        self.__buffer = []
        self.__affichage = ""
        
    def est_vide(self):
        """
        Renvoie un booléen selon si la file donnée est vide
        Syntaxe:
            exemple.est_vide() -> True/False
        """
        return len(self.__buffer) == 0
        
    def enfiler(self, e):
        """
        Enfile un élément donné sur la file donnée
        Syntaxe:
            exemple.enfiler('test')
        """
        self.__buffer.append(e)
        
    def defiler(self):
        """
        Defile un élément sur la file donnée et le renvoie
        Syntaxe:
            exemple.defiler() -> 'test'
        """
        assert self.est_vide() == False, "Impossible de défiler une file vide !"
        return self.__buffer.pop(index = 0)
    
    def __str__(self):
        for elements in self.__buffer:
            self.__affichage = self.__affichage + str(elements) + ", "
        self.__affichage = self.__affichage + "\nTête -----> Queue"
        return self.__affichage
    
class Piles:
    """
    Implémentation de la classe pile en python
    Syntaxe:
        exemple = Piles()
    """
    
    def __init__(self):
        self.__buffer = []
        self.__affichage = ""
        
    def est_vide(self):
        """
        Renvoie un booléen selon si la pile donnée est vide
        Syntaxe:
            exemple.est_vide() -> True/False
        """
        return len(self.__buffer) == 0
        
    def empiler(self, e):
        """
        Enpile un élément donné sur la pile donnée
        Syntaxe:
            exemple.enpiler('test')
        """
        self.__buffer.append(e)
        
    def depiler(self):
        """
        Dépile un élément sur la pile donnée et le renvoie
        Syntaxe:
            exemple.depiler() -> 'test'
        """
        assert self.est_vide() == False, "Impossible de dépiler une pile vide !"
        return self.__buffer.pop()
    
    def __str__(self):
        for elements in self.__buffer:
            self.__affichage = self.__affichage + str(elements) + ", "
        self.__affichage = self.__affichage + "\nPile -----> Sommet"
        return self.__affichage
    
        
    
        
    
    
