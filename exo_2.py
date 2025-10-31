"""Exercice 2 — Ajouter une méthode"""


class GuerrierZ:
    def __init__(self, nom, niveau_energie):
        self.nom = nom
        self.niveau_energie = niveau_energie


    def se_presenter(self):
        return f'Je suis {self.nom}, mon énergie est de {self.niveau_energie}.'


goku = GuerrierZ('Goku', 9000)

print(goku.se_presenter())
