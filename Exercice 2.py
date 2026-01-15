import os
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import QRect


class InterfaceGraphique(object):
    # Méthode pour calculer le double N
    def valider(self):
        # Pas de calcul si champ vide
        if not self.lineEdit.text():
            return
        # Si saisi de N non cohérent on ne fait rien
        try:
            N = int(self.lineEdit.text())
            self.lineEdit1.setText(str(N * 2))
        except ValueError:
            self.lineEdit1.setText(str(" "))

    # Methode pour sauvegarder
    def sauvegarder(self):
        # Pas de sauvegarde si champ avec resultat est vide
        if not self.lineEdit1.text():
            return
        # Ecriture dans le fichier Resultats et si des erreurs arrive on passe
        try:
            f = open("Resultats.txt", "w")
            f.write(self.lineEdit1.text())
            f.close()
        except Exception as e:
            pass

    # Methode pour charger/lire le fichier
    def charger(self):
        try:
            f = open("Resultats.txt", "r")
            resultat = f.read()
            f.close()
            if resultat:
                int(resultat)
                self.lineEdit1.setText(resultat)
        except:
            pass

    # Creation des widgets
    def windows(self, win):
        win.setObjectName("Form")
        win.resize(450, 250)
        win.setWindowTitle("Calculer Double")

        # Label pour saisir N
        self.label = QLabel("Entrez la valeur N : ", win)
        self.label.setGeometry(QRect(20, 20, 150, 30))

        # Champ pour N
        self.lineEdit = QLineEdit(win)
        self.lineEdit.setGeometry(QRect(180, 20, 100, 30))
        self.lineEdit.returnPressed.connect(self.valider)

        # Label pour le double
        self.label1 = QLabel("Voici le double : ", win)
        self.label1.setGeometry(QRect(20, 60, 150, 30))

        # Champ pour le double
        self.lineEdit1 = QLineEdit(win)
        self.lineEdit1.setGeometry(QRect(180, 60, 100, 30))
        self.lineEdit1.setReadOnly(True)

        # Bouton pour calculer le double
        self.button1 = QPushButton("Valider l'opération", win)
        self.button1.setGeometry(QRect(20, 140, 120, 30))
        self.button1.clicked.connect(self.valider)

        # Bouton pour sauvegarder le resultat
        self.button2 = QPushButton("Sauvegarder", win)
        self.button2.setGeometry(QRect(150, 140, 120, 30))
        self.button2.clicked.connect(self.sauvegarder)

        # Bouton pour charger le resultat
        self.button3 = QPushButton("Charger", win)
        self.button3.setGeometry(QRect(280, 140, 120, 30))
        self.button3.clicked.connect(self.charger)


# Point d'entrée
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    ui = InterfaceGraphique()
    ui.windows(win)
    win.show()
    sys.exit(app.exec())