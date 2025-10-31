"""Exercice 4 — Interaction entre classes"""


class ApprenantZ:
    def __init__(self, prenom, specialite):
        self.prenom = prenom
        self.specialite = specialite

    def etudier(self):
        return f'{self.prenom} étudie intensément la spécialité {self.specialite}'
    

michel = ApprenantZ('Michel', 'REACT')


class GuerrierZ:
    def __init__(self, nom, niveau_energie):
        self.nom = nom
        self.niveau_energie = niveau_energie


    def se_presenter(self):
        return f'Je suis {self.nom}, mon énergie est de {self.niveau_energie}.'


    def former(self, apprenant):
        return f'{self.nom} forme {apprenant.prenom} à devenir un codeur Super Saiyan !'
    
goku = GuerrierZ('Goku', 9000)
print(goku.former(michel))