import numpy as np
import matplotlib.pyplot as plt

class Signal:
    def __init__(self, nbr, tab=None):
        self.nbr = nbr
        if tab is None: #tab est le vecteur. Si aucun vecteur n'est fourni, un vecteur de zéros de taille nbr est créé
            self.tab = np.zeros(nbr)
        else:
            self.tab = tab

    def echantillons(self):
        return self.nbr

    def moyenne(self):          #renvoie la moyenne du vecteur (tab) 
        return np.mean(self.tab)

    def correlation(self):        #renvoie le deuxième coefficient de corrélation du vecteur (tab)
        return np.corrcoef(self.tab)

    def display(self):            #ffiche  le nombre d'échantillons et le vecteur.
        print(f"Nombre d'échantillons : {self.nbr}")
        print(f"Tableau : {self.tab}")

    def plot(self):
        plt.plot(self.tab)
        plt.show()

class Aleatoire(Signal):    #renvoie la somme des carrés des valeurs du tableau,
    def __init__(self, nbr, sigma, mean):
        super().__init__(nbr)
        self.sigma = sigma
        self.mean = mean
        self.init_alea() #appelle la méthode init_alea()

    def init_alea(self):#appelée pour remplir le tableau tab avec  des valeurs aléatoires générées
        self.tab = np.random.randn(self.nbr) * self.sigma + self.mean
               
        #crée un tableau de taille self.nbr contenant  des échantillons générés aléatoirement à partir d'une distribution   normale standard (moyenne = 0, variance = 1).
    def correlation(self):
        print("Classe Aléatoire")
        return np.power(self.tab, 2) #renvoie la somme des carrés des éléments du tableau tab. Explication détaillée :
                                     #np.power élève chaque élément du tableau tab au carré.
                                     #la somme de tous les éléments du tableau résultant.
class Deterministe(Signal):
    def __init__(self, nbr, amplitude):
        super().__init__(nbr)
        self.amplitude = amplitude
        self.init_valeurs()

    def init_valeurs(self):   #nitialise le vecteur (tab)  avec des valeurs croissantes de 0 à amplitude pour la première moitié,  
                               #et des valeurs constantes égales à -amplitude pour la deuxième moitié.
        self.tab[:self.nbr//2] = self.amplitude #nitialise la première moitié du tableau tab  avec des valeurs croissantes commençant de zéro et allant jusqu'à l'amplitude.
        self.tab[self.nbr//2:] = -self.amplitude #initialise la seconde moitié du tableau tab avec la valeur négative de l'amplitude.
#Cela crée essentiellement  une onde sinusoïdale qui part de zéro, atteint un pic à l'amplitude, puis revient à zéro.
# Exemple d'utilisation
signal1 = Signal(10, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
signal2 = Aleatoire(10, 1.0, 0.0)
signal3 = Deterministe(10, 3.0)

print("Signal 1:")
signal1.display()
signal1.plot()

print("\nSignal 2:")
signal2.display()
signal2.plot()

print("\nSignal 3:")
signal3.display()
signal3.plot()

def Addition(aleatoire, deterministe):
    new_deterministe = Deterministe(aleatoire.nbr, 0)
    new_deterministe.tab = aleatoire.tab + deterministe.tab
    return new_deterministe

if __name__ == "__main__":
    # Création d'un objet Aleatoire
    aleatoire = Aleatoire(20, 2, 5)

    # Création d'un objet Deterministe
    deterministe = Deterministe(20, 3)

    # Appel des méthodes pour chaque classe
    print("Objet Aléatoire:")
    aleatoire.display()
    print(f"Moyenne: {aleatoire.moyenne()}")
    print(f"Corrélation: {aleatoire.correlation()}")
    aleatoire.plot()

    print("\nObjet Déterministe:")
    deterministe.display()
    print(f"Moyenne: {deterministe.moyenne()}")
    print(f"Corrélation: {deterministe.correlation()}")
    deterministe.plot()

    # Appel de la fonction Addition
    S = Addition(aleatoire, deterministe)

    # Affichage du résultat
    print("\nRésultat de l'addition:")
    S.display()
    S.plot()



