# Form implementation generated from reading ui file 'dlgBuscarSer.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogBuscarSer(object):
    def setupUi(self, DialogBuscarSer):
        DialogBuscarSer.setObjectName("DialogBuscarSer")
        DialogBuscarSer.resize(271, 165)
        self.label = QtWidgets.QLabel(DialogBuscarSer)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnBuscarPorNombre = QtWidgets.QPushButton(DialogBuscarSer)
        self.btnBuscarPorNombre.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.btnBuscarPorNombre.setObjectName("btnBuscarPorNombre")
        self.widget = QtWidgets.QWidget(DialogBuscarSer)
        self.widget.setGeometry(QtCore.QRect(10, 60, 245, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Nombre = QtWidgets.QLabel(self.widget)
        self.Nombre.setObjectName("Nombre")
        self.horizontalLayout.addWidget(self.Nombre)
        self.txtBuscarNombre = QtWidgets.QLineEdit(self.widget)
        self.txtBuscarNombre.setMinimumSize(QtCore.QSize(150, 0))
        self.txtBuscarNombre.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtBuscarNombre.setObjectName("txtBuscarNombre")
        self.horizontalLayout.addWidget(self.txtBuscarNombre)

        self.retranslateUi(DialogBuscarSer)
        QtCore.QMetaObject.connectSlotsByName(DialogBuscarSer)

    def retranslateUi(self, DialogBuscarSer):
        _translate = QtCore.QCoreApplication.translate
        DialogBuscarSer.setWindowTitle(_translate("DialogBuscarSer", "Dialog"))
        self.label.setText(_translate("DialogBuscarSer", "Buscador"))
        self.btnBuscarPorNombre.setText(_translate("DialogBuscarSer", "Buscar"))
        self.Nombre.setText(_translate("DialogBuscarSer", "Nomber/Concepto"))
