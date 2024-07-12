class Animal:
    def __init__(self, nom, poids, taille):
        self.__poids = poids
        self.__taille = taille
        self.__nom = nom

    def se_deplacer(self):
        print("je me déplace")

    def get_nom(self):
        return self.__nom
    def set_nom(self, newnom):
        self.__nom = newnom

    def get_poids(self):
        return self.__poids
    def set_poids(self, newpoids):

        if not newpoids > 0:
            raise ValueError("Poids négatif")
        else:
            self.__poids = newpoids

    
    def get_taille(self):
        return self.__taille
    def set_taille(self, newtaille):
        self.__taille = newtaille

    def __str__(self):
        return f"animal : {self.get_nom()} , poids : {self.get_poids()} kg, taille : {self.get_taille()} cm , {self.se_deplacer()}"
    

class Serpent(Animal):
    def se_deplacer(self):
        print('je rampe')


class Oiseau(Animal):
    def __init__(self, nom, poids, taille, altitude_max):
        super().__init__(nom, poids, taille)
        self.__altitude_max = altitude_max

    def get_altitude_max(self):
        return self.__altitude_max
    def set_altitude_max(self, n_altitude_max):
        self.__altitude_max = n_altitude_max

    def se_deplacer(self):
        print('je vole')

    def __str__(self):
        return f"animal : {self.get_nom()} , poids : {self.get_poids()} , taille : {self.get_taille()} cm , altitude max : {self.get_altitude_max()}"

class Zoo():
    
    def __init__(self, liste : list):
        self.liste = liste.copy()

    def ajouter_animal(self, animal : Animal):
        if isinstance(animal, Animal):
            self.liste.append(animal)
        else:
            raise ValueError
        
    def __add__(self, animaux):
        return Zoo(self.liste + animaux.liste)

if __name__ == "__main__":
                
    aigle = Oiseau('aigle', 1, 10, 6000)
    girafe = Animal('girafe', 200, 400)
    vipere = Serpent('vipere', 1, 100)

    liste = [aigle, girafe, vipere]

    cheval = Animal('cheval', 200, 250)
    licorne = Animal('licorne', 999, 999)

    dragon = Animal('dragon', 666, 666)
    loutre = Animal('loutre', 5, 50)

    zoo = Zoo(liste)
    zoo2 = Zoo([dragon])

    zoo.ajouter_animal(cheval)
    zoo.ajouter_animal(licorne)

    zoo3 = zoo.__add__(zoo2)
    for animal in zoo3.liste:
        print(animal) 

    aigle.se_deplacer




