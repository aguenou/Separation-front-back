class Personnage:
    nombreDeVies = 0
    nom = " "
    force = 0
    arme = " "

    def __init__(self,nombreDeVies,nom,force,arme):
        self.nombreDeVies = nombreDeVies
        self.nom = nom
        self.force = force
        self.arme = arme

    def parler(self,message):
        print(f"{self.nom} dit: {message} {self.nom}")

    def frapper(self,person):
        if person.force > 0 and person.nombreDeVies > 0:
            person.nombreDeVies -= 1
            person.force += 25
            if person.nombreDeVies == 0:
                print(f"le personnage {person.nom} est mort")


def main():
    perso1 = Personnage(2, 'yu',0, 'fusil')
    perso2 = Personnage(2,'ya', 1, 'fusil')

    perso1.frapper(perso2)
    perso2.parler("Je m'appelle")
    
    #print(f"{perso2.nom} \n Nombre de vie : {perso2.nombreDeVies} \n  Force: {perso2.force}  ")
    
    perso1.frapper(perso2)
    perso2.parler("Je m'appelle")

    #print(f"{perso2.nom} \n Nombre de vie : {perso2.nombreDeVies} \n  Force: {perso2.force}  ")


if __name__ == "__main__":
    main()


