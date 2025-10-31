"""Exercice 1 — Créer sa première classe"""


class GuerrierZ:
    def __init__(self, nom, niveau_energie):
        self.nom = nom
        self.niveau_energie = niveau_energie


goku = GuerrierZ('Goku', 9000)

print(goku.nom)
print(goku.niveau_energie)

