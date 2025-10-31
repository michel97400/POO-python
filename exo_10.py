"""Exercice 10 — Fusion ultime 💥"""

class CoursZ():
    def __init__(self, nom_cours):
        self.nom_cours = nom_cours
        self.liste_apprenants = []

    def ajouter_apprenant(self, apprenant):
        self.liste_apprenants.append(apprenant)

    def afficher_apprenants(self):
        return f'Apprenants du cours "Combat orienté objet" : {self.liste_apprenants}'


class GuerrierZ:
    def __init__(self, nom, niveau_energie):
        self.nom = nom
        self.niveau_energie = niveau_energie
        self.__niveau_secret = "Salle du temp"


    def se_presenter(self):
        return f'Je suis {self.nom}, mon énergie est de {self.niveau_energie}.'


    def former(self, apprenant):
        return f'{self.nom} forme {apprenant.prenom} à devenir un codeur Super Saiyan !'
    
    def devoiler_secret(self):
        if self.nom == 'Goku':
            return f'Le niveau secrect est : {self.__niveau_secret}'
        else:
            return 'Erreur lors de la lecture du nom !'


class FormateurZ(GuerrierZ):
    def __init__(self, nom, niveau_energie):
        super().__init__(nom, niveau_energie)


    def donner_cours(self, cours):
        return f'{self.nom} enseigne le cours à {cours} à {len(cours)} apprenants.'
    
    
class ApprenantZ(GuerrierZ):
    def __init__(self, nom, niveau_energie):
        super().__init__(nom, niveau_energie)


    def agir(self):
        return 'Je code pour protéger le réseau !'


cours = CoursZ("Python Super Saiyan")


michel = ApprenantZ('Michel', 9000)
flavie = ApprenantZ('Flavie', 9000)
fidel = ApprenantZ('Fidel', 9000)

goku = FormateurZ('Goku', 10000)

cours.ajouter_apprenant(michel.nom)
cours.ajouter_apprenant(flavie.nom)
cours.ajouter_apprenant(fidel.nom)

print(goku.donner_cours(cours.liste_apprenants))