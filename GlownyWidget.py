__author__ = 'piotrek'

from PyQt5 import QtWidgets, QtGui, QtCore

class GlownyWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


    def paintEvent(self, paint_event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 5, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))

        pola = self.parent().pola

        diffv = (pola[0][1].x() - (pola[0][0].x()+pola[0][0].width()))/2
        y_start = pola[0][0].y() - 20
        y_end = pola[2][0].y() + pola[0][0].height() + 20
        for i in range(1, 3):
            xv = pola[0][i].x() - diffv
            painter.drawLine(xv, y_start, xv, y_end)


        diffh = (pola[1][0].y() - (pola[0][0].y()+pola[0][0].height()))/2
        x_start = pola[0][0].x() - 20
        x_end = pola[0][2].x() + pola[0][0].width() + 20
        for j in range(1, 3):
            yh = pola[j][0].y() - diffh
            painter.drawLine(x_start, yh, x_end, yh)


