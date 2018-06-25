__author__ = 'piotrek'

from random import choice
from PyQt5 import QtWidgets, QtCore, QtGui

from GlownyWidget import GlownyWidget
from Pole import Pole


class Gra(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 600)
        self.setMinimumSize(self.width(), self.height())
        self.setWindowTitle('Kolko i krzyzyk')
        self.ustaw_okno()

        self.glowny_widget = GlownyWidget()
        self.layout = QtWidgets.QGridLayout()

        self.ustaw_pola()
        self.ustaw_informacje()
        self.ustaw_przyciski()
        self.statusBar().showMessage('Gotowy', 2000)

    def ustaw_okno(self):
        rozmiar = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((rozmiar.width() - self.width())//2, (rozmiar.height() - self.height())//2)

    def ustaw_informacje(self):
        self.ruchGracza = choice(('X', 'O'))
        self.informacja = QtWidgets.QLabel('Rozpoczyna gracz: {}'.format(self.ruchGracza))
        self.informacja.setMaximumSize(self.width(), 20)
        czcionka = self.informacja.font()
        czcionka.setPointSize(10)
        self.informacja.setFont(czcionka)
        self.layout.addWidget(self.informacja, 3, 0, 1, 3, QtCore.Qt.AlignHCenter)

    def ustaw_pola(self):
        index = 1
        self.pola = []
        for i in range(3):
            lista = []
            for j in range(3):
                pole = Pole()
                self.layout.addWidget(pole, i, j)
                lista.append(pole)
                if index % 3 == 0:
                    self.pola.append(lista)
                index += 1
        self.glowny_widget.setLayout(self.layout)
        self
        self.setCentralWidget(self.glowny_widget)

    def ustaw_przyciski(self):
        self.resetuj = QtWidgets.QPushButton('Resetuj', clicked = self.resetuj_gre)
        self.zamknij = QtWidgets.QPushButton('Zamknij', clicked = self.close)
        self.layout.addWidget(self.resetuj, 4, 0)
        self.layout.addWidget(self.zamknij, 4, 2)

    def resetuj_gre(self):
        self.ruchGracza = choice(('X', 'O'))
        self.informacja.setText('Rozpoczyna gracz: {}'.format(self.ruchGracza))
        for i in range(3):
            for j in range(3):
                self.pola[i][j].reset()
        self.statusBar().showMessage('Gotowy', 2000)

    def zablokuj_i_wyswietl(self, wygrana: bool):
        for i in range(3):
            for j in range(3):
                self.pola[i][j].setEnabled(False)
        if wygrana:
            self.informacja.setText('Wygral gracz: {}'.format(self.ruchGracza))
            self.statusBar().showMessage('Wygral gracz: {}'.format(self.ruchGracza), 5000)
        else:
            self.informacja.setText('Remis')
            self.statusBar().showMessage('Remis', 5000)

    def sprawdz(self):
        print('Sprawdzanie')
        for i in range(0, 3):
            if (self.pola[i][0].text() != '' and (self.pola[i][0].text() == self.pola[i][1].text()  == self.pola[i][2].text()) \
                or (self.pola[0][i].text() != '' and (self.pola[0][i].text() == self.pola[1][i].text() == self.pola[2][i].text()))):
                print('Wygrana')
                self.zablokuj_i_wyswietl(True)
                return True
        if self.pola[0][0].text() != '' and (self.pola[0][0].text() == self.pola[1][1].text() == self.pola[2][2].text()) \
            or self.pola[0][2].text() != '' and (self.pola[0][2].text() == self.pola[1][1].text() == self.pola[2][0].text()):
                print('Wygrana')
                self.zablokuj_i_wyswietl(True)
                return True
        if all((self.pola[i][j].text() for i in range(3) for j in range(3))):
            print('Remis')
            self.zablokuj_i_wyswietl(False)
            return True
        return False
