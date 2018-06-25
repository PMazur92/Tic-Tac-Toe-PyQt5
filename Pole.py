__author__ = 'piotrek'

from PyQt5 import QtWidgets, QtCore, QtGui


class Pole(QtWidgets.QLabel):
    
    def __init__(self, parent=None):
        super().__init__('', parent)
        self.resize(100, 100)
        self.setMaximumSize(self.size())
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet('Pole { background-color: red; border: 3px solid black; color: blue; }')
        self.setFont(QtGui.QFont('arial', 30))
        self.czy_ustawiony = False

    def mousePressEvent(self, mouse_event: QtGui.QMouseEvent):
        rodzic_glowny = self.parent().parent()
        if not self.czy_ustawiony:
            self.setText(rodzic_glowny.ruchGracza)
            if rodzic_glowny.sprawdz():
                return
            rodzic_glowny.ruchGracza = 'X' if rodzic_glowny.ruchGracza == 'O' else 'O'
            rodzic_glowny.informacja.setText('Kolej gracza: {}'.format(rodzic_glowny.ruchGracza))
            rodzic_glowny.statusBar().showMessage('Kolej gracza: {}'.format(rodzic_glowny.ruchGracza), 5000)
            self.czy_ustawiony = True

        else:
            rodzic_glowny.statusBar().showMessage('Pole jest juz ustawione')

    def ustawienie(self):
        return self.czy_ustawiony

    def reset(self):
        self.czy_ustawiony = False
        self.setText('')
        self.setEnabled(True)
