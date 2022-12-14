# This is a sample Python script.
import datetime

import app as app

import Clients
import conexion
import events
from dlgDatos import Ui_dlgExportarDatos
from dlgcalendar import Ui_dlgcalendar
from ventana import *
import sys
import var
from dlgSalir import *



class FileDialogAbrir(QtWidgets.QFileDialog):

    def __init__(self):
        super(FileDialogAbrir,self).__init__()



class DialogCalendar(QtWidgets.QDialog):

    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgcalendar()
        var.dlgcalendar.setupUi(self)

        dia = datetime.datetime.now().day
        mes = datetime.datetime.now().month
        ano = datetime.datetime.now().year
        var.dlgcalendar.Calendario.setSelectedDate(QtCore.QDate(ano,mes,dia))


        var.dlgcalendar.Calendario.clicked.connect(Clients.Clientes.cargaFecha)










class DialogoSalir(QtWidgets.QDialog):

    def __init__(self):
        super(DialogoSalir,self).__init__()
        var.avisosalir = Ui_Dialog()
        var.avisosalir.setupUi(self)
        var.avisosalir.btnSalir.clicked.connect(events.Eventos.Salir)

class DialogoDatos(QtWidgets.QDialog):

    def __init__(self):
        super(DialogoDatos,self).__init__()
        var.dlgDatos = Ui_dlgExportarDatos()
        var.dlgDatos.setupUi(self)
        var.dlgDatos.btnExportarDatos.clicked.connect(events.Eventos.exportarDatos)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
            super(Main,self).__init__()
            var.ui = Ui_ventana()
            var.ui.setupUi(self)
            var.avisosalir = DialogoSalir()
            var.dlgcalendar = DialogCalendar()
            var.dlgAbrir = FileDialogAbrir()
            var.dlgDatos = DialogoDatos()
            conexion.Conexion.conexion()
            conexion.Conexion.cargarProv()
            var.ui.cmbProcli.currentIndexChanged.connect(conexion.Conexion.selMuni)
            var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
            var.ui.ActionSalirBar.triggered.connect(events.Eventos.Salir)
            Clients.Clientes.selMotor()
            conexion.Conexion.mostrarTabcarcli()

            var.ui.tabClientes.setStyleSheet(
                "QTableView::item:alternate { background-color: #C0C0C0; } QTableView::item { background-color: #d1c8c6; }")


            var.motor = (var.ui.rbtDiesel, var.ui.rbtGasolina, var.ui.rbtHibrido, var.ui.rbtElt)
            var.ui.btnGuardarCli.clicked.connect(Clients.Clientes.guardarCli)
            var.ui.btnFechaAltaClin.clicked.connect(events.Eventos.abrirCalendar)
            var.ui.btnBorraCli.clicked.connect(Clients.Clientes.borrarCli)
            var.ui.btnModificarCli.clicked.connect(Clients.Clientes.modifCli)


            var.ui.txtDni.editingFinished.connect(Clients.Clientes.mostraValidodni)
            var.ui.txtNombre.editingFinished.connect(events.Eventos.letrasCapital)
            var.ui.txtDircli.editingFinished.connect(events.Eventos.letrasCapital)
            var.ui.txtModelo.editingFinished.connect(events.Eventos.letrasCapital)
            var.ui.txtMarca.editingFinished.connect(events.Eventos.letrasCapital)

            var.ui.actionCrear_Copia_de_Seguridad.triggered.connect(events.Eventos.crearBackup)
            var.ui.actionRestaurar_Copia_de_Seguridad.triggered.connect(events.Eventos.restaurarBackup)
            var.ui.ActionCrearBackup.triggered.connect(events.Eventos.crearBackup)
            var.ui.ActionRecuperarBackup.triggered.connect(events.Eventos.restaurarBackup)
            var.ui.ActionExportar_Datos.triggered.connect(events.Eventos.exportarDatos)
            var.ui.ActionImportarDatos.triggered.connect(events.Eventos.importarDatos)


'''
            var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
            var.ui.txtDni.editingFinished.connect(Clients.Clientes.mostraValidodni)
            var.ui.ActionSalirBar.triggered.connect(events.Eventos.Salir)
            Clients.Clientes.selMotor()
            var.ui.actionSalir.triggered.connect(events.Eventos.Salir())
            var.ui.ActionSalirBar.triggered.connect(events.Eventos.Salir())
            
            
            var.motor = (var.ui.rbtDiesel, var.ui.rbtGasolina, var.ui.rbtHibrido, var.ui.rbtElt)
            var.ui.btn_guard_cli.clicked.connect(Clients.guarda_cli)
            var.ui.btn_fecha_alta_cli.clicked.connect(events.Eventos.abrir_calendar)
            var.ui.btnSalir.clicked.connect(events.Eventos.Salir())
           
            letrasCapital metodo para poner mayuscula la primera letra de todas las frases
            
            var.ui.txtDni.editingFinished.connect(Clients.Clientes.mostraValidodni)
            var.ui.txtNombre.editingFinished.connect(events.Eventos.letrasCapital)
            var.ui.txtDircli.editingFinished.connect(events.Eventos.letrasCapital)
            var.ui.txtModelo.editingFinished.connect(events.Eventos.letrasCapital)
            var.ui.txtMarca.editingFinished.connect(events.Eventos.letrasCapital)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    print_hi('PyCharm')
    window = Main()
    window.show()
    sys.exit(app.exec())

