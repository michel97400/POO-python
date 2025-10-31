"""Exercice 3 — L’apprenant Super Saiyan"""


class ApprenantZ:
    def __init__(self, prenom, specialite):
        self.prenom = prenom
        self.specialite = specialite

    def etudier(self):
        return f'{self.prenom} étudie intensément la spécialité {self.specialite}'
    

michel = ApprenantZ('Michel', 'REACT')
flavie = ApprenantZ('Flavie', 'IA')
fidel = ApprenantZ('Fidel', 'Git')
print(michel.etudier())
print(flavie.etudier())
print(fidel.etudier())