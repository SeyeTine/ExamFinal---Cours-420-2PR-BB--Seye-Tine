import os
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget, QtCore



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

    #Creation des wifgets
    def Widgets (self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setWindowTitle("Calculer Double")
        #Label pour saisir N
        self.label = QtWidgets.QLabel("Entrez la valeur N : ", Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 150, 30))
        #Champ pour N
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 20, 100, 30))
        self.lineEdit.returnPressed.connect(self.valider)
        #Label pour le doucble
        self.label1 = QtWidgets.QLabel("Voici le double : ", Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 150, 30))
        #Champ pour le double
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(20, 100, 140, 30))
        self.lineEdit1.setReasOnly(True)

        #Bouton pour calculer le double
        self.button1 = QtWidgets.QPushButton("Valider l'opération", Form)
        self.button1.setGeometry(QtCore.QRect(20, 100, 140, 30))
        self.button1.clicked.connect(self.valider)
        #Bouton pour sauvegarder le resultat
        self.button2 = QtWidgets.QPushButton("Sauvegarder", Form)
        self.button2.setGeometry(QtCore.QRect(170, 100, 120, 30))
        self.button2.clicked.connect(self.sauvegarder)
        #Bouton pour charger le resultat
        self.button3 = QtWidgets.QPushButton("Charger", Form)
        self.button3.setGeometry(QtCore.QRect(20, 100, 140, 30))
        self.button3.clicked.connect(self.charger)


