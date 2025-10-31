"""Exercice 5 — Attributs privés et sécurité"""

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
        
goku = GuerrierZ('Goku', 9000)
vegeta = GuerrierZ('Vegeta', 9000)

print(goku.devoiler_secret())
print(vegeta.devoiler_secret())
    