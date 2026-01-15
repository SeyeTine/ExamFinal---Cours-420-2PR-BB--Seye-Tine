import os
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox


class InterfaceGraphique(objet):
    #Méthode pour calculer le double N
    def valider(self)  :
        #Pas de calcul si champ vide
        if not self.lineEdit.text() :
            return
        #Si saisi de N non cohérent on ne fait rien
        try:
            N = int(self.lineEdit.text())
            self.lineEdit1.setText(str(N*2))
        except ValueError:
            self.lineEdit1.setText(str(" "))
    #Methode pour sauvegarder
    def sauvegarder(self):
        # Pas de sauvegarde si champ avec resultat est vide
        if not self.lineEdit1.text() :
            return
        # Ecriture dans le fichier Resultats et si des erreurs arrive on passe
        try:
            f=open("Resultats.txt", "w")
            f.write(self.lineEdit1.text())
            f.close()
        except Exception as e:
            pass

    #Methode pour charger/lire le fichier
    def charger (self):
        try:
            f=open("Resultats.txt", "r")
            resultat = f.read
            f.close()
            if resultat:
                int(resultat)
                self.lineEdit1.setText(resultat)
        except:
            pass



