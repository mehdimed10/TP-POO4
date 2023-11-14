from module_detrois_classes import Ingenieur, Technicien

""" Ingenieur et Technicien"""
ingenieur1 = Ingenieur("med", 6, "bonne etat")
technicien1 = Technicien("Bob", 8, "bonne etat")

#  affiche avec true et false
ingenieur1.affiche(True)  #  avec a=True
print("\n")  
technicien1.affiche(False)  #  avec a=False
