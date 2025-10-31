"""Exercice 9 — Composition (un cours contient des apprenants)"""


class Apprenant:
    def __init__(self, nom):
        self.nom = nom



class CoursZ():
    def __init__(self, nom_cours):
        self.nom_cours = nom_cours
        self.liste_apprenants = []

    def ajouter_apprenant(self, apprenant):
        self.liste_apprenants.append(apprenant)

    def afficher_apprenants(self):
        return f'Apprenants du cours "Combat orienté objet" : {self.liste_apprenants}'

michel = Apprenant('Michel')
flavie = Apprenant('Flavie')

cours = CoursZ("Combat orienté objet")
cours.ajouter_apprenant(michel.nom)
cours.ajouter_apprenant(flavie.nom)
print(cours.afficher_apprenants())