"""Exercice 7 — Polymorphisme"""


class GuerrierZ:
    def __init__(self, nom, niveau_energie):
        self.nom = nom
        self.niveau_energie = niveau_energie
        self.__niveau_secret = "Salle du temp"


    def agir():
        return f'Je me bats pour protéger la Terre'
    


class ApprenantZ(GuerrierZ):
    def __init__(self, nom, niveau_energie):
        super().__init__(nom, niveau_energie)


    def agir(self):
        return f'Je suis {self.nom}, je code pour protéger le réseau !'

list_app = []

goku = ApprenantZ('Goku', 9000)
flavie = ApprenantZ('Flavie', 9000)
michel = ApprenantZ('Michel', 9000)

list_app.append(goku)
list_app.append(flavie)
list_app.append(michel)

for i in range(0, len(list_app)):
    print(list_app[i].agir())
