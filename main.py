__author__ = 'piotrek'

import sys

from PyQt5 import Qt
from Gra import Gra

if __name__ == '__main__' :
    app = Qt.QApplication(sys.argv)

    gra = Gra()
    gra.show()

    sys.exit(app.exec_())

