from enum import Enum
list_personnage = []
class Niveau(Enum):
    DEBUTANT = "Débutant"
    INTERMEDIAIRE = "Intermédiaire"
    EXPERT = "Expert"

class Personnage:
    nombreDeVies = 2
    nom = " "
    force = 0
    arme = " "
    nombreCombat = 0
    niveau = Niveau.DEBUTANT.value if nombreCombat < 3 else (Niveau.INTERMEDIAIRE.value if nombreCombat < 10 else Niveau.EXPERT.value)

    def __init__(self,nom,force,arme):
        self.nom = nom
        self.force = force
        self.arme = arme

    def parler(self,message):
        print(f"{self.nom} dit: {message} {self.nom}")
        menu()

    def frapper(self):
        self.nombreCombat += 1
        force(self)
        if self.force > 0 and self.nombreDeVies > 0:
            self.nombreDeVies -= 1
            self.force += 25
            if self.nombreDeVies == 0:
                print(f"le personnage {self.nom} est mort")
        menu()

def force(person):
    if person.niveau == Niveau.DEBUTANT.value:
        person.force += person * 0.01


def sousMenu():
        print("a-Frapper \nb-Parler")
        b = input("Effectuez un choix: ")
        if b == 'a':
            c = int(input("Donnez l'index du personnage: "))
            if list_personnage[c]:
                list_personnage[c].frapper()
        elif b == 'b':
            d = int(input("Donnez l'index du personnage: "))
            message = input("Votre message: ")
            if list_personnage[d]:
                list_personnage[d].parler(message)
        menu()

def menu():
        print("i- Créer un personnage \nii- Effectuer une action\niii- Quitter le programme")
        a = input("Effectuez un choix: ")
        if a == 'i':
            nom = input("Nom du personnage: ")
            force = int(input("Force: "))
            arme = input("Arme: ")
            creerPersonnage(nom,force,arme)
        elif a == 'ii':
            sousMenu()
        else:
            exit()

def creerPersonnage(nom, force, arme):
    list_personnage.append(Personnage(nom, force, arme))
    print(f'Le nom des personnages créés: ')
    for x in range(0, len(list_personnage)) :
        print(f" {list_personnage[x].nom} ")
    menu()
        
def main():
    menu()
    
        

if __name__ == "__main__":
    main()
