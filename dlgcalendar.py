# Form implementation generated from reading ui file 'dlgcalendar.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgcalendar(object):
    def setupUi(self, dlgcalendar):
        dlgcalendar.setObjectName("dlgcalendar")
        dlgcalendar.resize(247, 190)
        dlgcalendar.setMinimumSize(QtCore.QSize(247, 190))
        dlgcalendar.setMaximumSize(QtCore.QSize(247, 190))
        self.Calendario = QtWidgets.QCalendarWidget(dlgcalendar)
        self.Calendario.setGeometry(QtCore.QRect(0, 0, 247, 181))
        self.Calendario.setObjectName("Calendario")

        self.retranslateUi(dlgcalendar)
        QtCore.QMetaObject.connectSlotsByName(dlgcalendar)

    def retranslateUi(self, dlgcalendar):
        _translate = QtCore.QCoreApplication.translate
        dlgcalendar.setWindowTitle(_translate("dlgcalendar", "calendar"))
