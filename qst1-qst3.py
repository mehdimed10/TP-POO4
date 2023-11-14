class Employe:
    def __init__(self, nom, identifiant, point_indiciaire=500):
        self.nom = nom
        self.id = identifiant
        self.pin = point_indiciaire

    def calcul_prime(self, a):
        
        if a:
            return self.pin * 2
        else:
            return self.pin * 0.5

    def salaire(self, prime):
        return self.pin * prime

    def affiche(self, a):
        prime = self.calcul_prime(a)
        salaire_empl = self.salaire(prime)
        
        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Point indiciaire:", self.pin)
        print("Prime:", prime)
        print("Salaire:", salaire_empl)
        print("Statut: Employé")
      

employe1 = Employe("Mehdi med", 1)
employe1.affiche(True)  #  avec a=True
print("\n")
employe2 = Employe("Jamal jel", 2)
employe2.affiche(False)  #  avec a=False
print("\n")

class Ingenieur(Employe):
    def __init__(self, nom, identifiant, etat,point_indiciaire=50):
        #super().__init__(nom, identifiant, point_indiciaire)
        Employe.__init__(self, nom, identifiant, point_indiciaire)
        self.Etat = etat

    def salaire(self, prime):
        if self.Etat == "stagiaire":
            return self.pin * 4 * prime
        else:
            return self.pin * 6 * prime
        
        
    def affiche(self, a): 
         prime = self.calcul_prime(a)
         salaire_ingen = self.salaire(prime)
         
         print("Nom:", self.nom)
         print("ID:", self.id)
         print("Point indiciaire:",self.pin)
         print("Prime:", prime)
         print("Salaire:", salaire_ingen)
         print("Statut: Employé")
         print("Statut: Ingénieur +", self.Etat)
    
ingenieur1 = Ingenieur("med ", 3, "titulaire")
ingenieur1.affiche(False)
print("\n")
stagiaire1 = Ingenieur("jel", 4, "titulaire")
stagiaire1.affiche(True)
print("\n")
class Technicien(Employe):
    def __init__(self, nom, identifiant, point_indiciaire=50):
        super().__init__(nom, identifiant, point_indiciaire)
       

    def salaire(self, prime):
        return self.pin * 2 * prime

    def affiche(self, a):
        prime = self.calcul_prime(a)
        salaire_techn = self.salaire(prime)
        
        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Point indiciaire:", self.pin)
        print("Prime:", prime)
        print("Salaire:", salaire_techn)
        print("Statut: Technicien",)
technicien1 = Technicien("meh_techn", 5)
technicien1.affiche(True)



