"""Exercice 6 — Héritage"""


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
        

class GuerrierSaiyan(GuerrierZ):
    def __init__(self, nom, niveau_energie, transformation):
        super().__init__(nom, niveau_energie)
        self.transformation = transformation

    def se_presenter(self):
        return f'Je suis {self.nom}, mon energie est de {self.niveau_energie} transformation : {self.transformation}'
    

gohan = GuerrierSaiyan("Gohan", 10000, "Super Saiyan 2")
print(gohan.se_presenter())