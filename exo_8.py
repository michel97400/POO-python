"""Exercice 8 — Attribut de classe"""


class ApprenantZ:
    nombre_total = 0

    def __init__(self, prenom, specialite):
        self.prenom = prenom
        self.specialite = specialite
        ApprenantZ.nombre_total += 1

    def etudier(self):
        return f'{self.prenom} étudie intensément la spécialité {self.specialite}'
    

michel = ApprenantZ('Michel', 'REACT')

print(michel.nombre_total)