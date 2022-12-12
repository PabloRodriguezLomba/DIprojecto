from datetime import datetime
from idlelib import query
from ventana import Ui_ventana
from PyQt6 import QtSql
from PyQt6 import QtWidgets, QtCore

import var


class Conexion():


    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        filedb = 'bbdd.sqlite'
        db.setDatabaseName(filedb)
        if not db.open():
            QtWidgets.QMessageBox.critical(None,'No se abre la base de datos','conexion no establecida. \n','Haga click para cerra',QtWidgets.QMessageBox.StandarButton.cancel)
            return False
        else:
            print('Conexion establecida')
        return True
    def cargarProv(self = None):
        try:
                var.ui.cmbProcli.clear()
                query = QtSql.QSqlQuery()
                query.prepare('select provincia from provincias')
                if query.exec():
                    var.ui.cmbProcli.addItem(' ')
                    while query.next():
                        var.ui.cmbProcli.addItem(query.value(0))
        except Exception as error:
            print('Error cargar provincia')

    def selMuni(self=None):
            try:
                id = 0
                var.ui.cmbMunicli.clear()
                prov = var.ui.cmbProcli.currentText()
                query = QtSql.QSqlQuery()
                query.prepare('select id from provincias where provincia = :prov')
                query.bindValue(':prov', prov)
                if query.exec():
                    while query.next():
                        id = query.value(0)

                query1 = QtSql.QSqlQuery()
                query1.prepare('select municipio from municipios where provincia_id = :id')
                query1.bindValue(':id', int(id))
                if query1.exec():
                    var.ui.cmbMunicli.addItem(' ')
                    while query1.next():
                        var.ui.cmbMunicli.addItem(query1.value(0))



            except Exception as error:
                print("Error carde de municipios" + error)
    @staticmethod
    def altaCli(newcli,newcar):
        try:
            consulta = QtSql.QSqlQuery()
            consulta.prepare('insert into clientes (nombre,dni,alta,direccion,provincia,municipio,pago) VALUES (:nombre,:dni,:alta,:direccion,:provincia,:municipio,:pago)')
            consulta.bindValue(':dni', str(newcli[0]))
            consulta.bindValue(':nombre', str(newcli[1]))
            consulta.bindValue(':alta', str(newcli[2]))
            consulta.bindValue(':direccion', str(newcli[3]))
            consulta.bindValue(':provincia', str(newcli[4]))
            consulta.bindValue(':municipio', str(newcli[5]))
            consulta.bindValue(':pago', str(newcli[6]))
            if consulta.exec():
                esg = QtWidgets.QMessageBox()

                esg.setWindowTitle('Aviso')
                esg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                esg.setText('Cliente  dado de Alta')
                esg.exec()
            else:
                esg = QtWidgets.QMessageBox()
                esg.setModal(True)
                esg.setWindowTitle('Aviso')
                esg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                esg.setText(consulta.lastError().text())
                esg.exec()

            query1 = QtSql.QSqlQuery()
            query1.prepare('insert into coches (matricula,dnicli,marca,modelo,motor) VALUES (:matricula,:dnicli,:marca,:modelo,:motor)')
            query1.bindValue(':matricula',str(newcar[0]))
            query1.bindValue(':dnicli', str(newcli[0]))
            query1.bindValue(':marca', str(newcar[1]))
            query1.bindValue(':modelo', str(newcar[2]))
            query1.bindValue(':motor', str(newcar[3]))
            if query1.exec():
                esg = QtWidgets.QMessageBox()
                esg.setModal(True)
                esg.setWindowTitle('Aviso')
                esg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                esg.setText('Cliente - Coche dado de Alta')
                esg.exec()
            else:
                esg = QtWidgets.QMessageBox()
                esg.setModal(True)
                esg.setWindowTitle('Aviso')
                esg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                esg.setText(query1.lastError().text())
                esg.exec()
        except Exception as error:
            print('problemas conexion alta cliente', error)

    def mostrarTabcarcli(self = None):
        try:
            var.ui:Ui_ventana
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select * from coches where fechabajacar is null order by marca,modelo')
            if query.exec():
                while query.next():
                    var.ui.tabClientes.setRowCount(index+1)
                    var.ui.tabClientes.setItem(index,0,QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(query.value(3))))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))
                    var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index +=1
        except Exception as error:
            print('Problema al mostrar listado clientes')
    def borrarCli(dni):
        try:

            fecha = datetime.today()
            fecha = fecha.strftime("%d.%m.%Y.%H.%M.%S")

            query = QtSql.QSqlQuery()
            query.prepare("update clientes set fechabajacli = :fecha where dni = :dni")
            query.bindValue(':fecha',str(fecha))
            query.bindValue(':dni', str(dni))
            if query.exec():
               pass

            query1 = QtSql.QSqlQuery()
            query1.prepare("update coches set fechabajacar = :fecha where dnicli = :dni")
            query1.bindValue(":fecha",str(fecha))
            query1.bindValue(":dni",str(dni))
            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Borrado con exito")
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText(query1.lastError().text())
                msg.exec()



        except Exception as error:
            print("Error borrar cliente en conexion" + error)
    @staticmethod
    def modificarCli(modcli,modcar):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("update clientes set nombre = :nombre , alta = :alta , direccion = :direccion , provincia = :provincia , municipio = :municipio, pago = :pago  where dni = :dni")
            query.bindValue(':dni',str(modcli[0]))
            query.bindValue(':nombre', str(modcli[1]))
            query.bindValue(':alta', str(modcli[2]))
            query.bindValue(':direccion', str(modcli[3]))
            query.bindValue(':provincia', str(modcli[4]))
            query.bindValue(':municipio', str(modcli[5]))
            query.bindValue(':pago', str(modcli[6]))
            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Datos Cliente Modificados")
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
            query1 = QtSql.QSqlQuery()
            query1.prepare('update coches set dnicli = :dni , marca = :marca , modelo = :modelo, motor = :motor where matricula = :matricula')
            query1.bindValue(":dni",str(modcli[0]))
            query1.bindValue(":marca", str(modcar[1]))
            query1.bindValue(":modelo", str(modcar[2]))
            query1.bindValue(":motor", str(modcar[3]))
            query1.bindValue(":matricula", str(modcar[0]))
            if query1.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Datos Cliente Modificados")
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query1.lastError().text())
                msg.exec()


        except Exception as error:
            print("Error en modificarCli as ",error)

    @staticmethod
    def altaExcelCoche(newcli,newcar):
        try:
            consulta = QtSql.QSqlQuery()
            consulta.prepare(
                'insert into clientes (nombre,dni,alta,direccion,provincia,municipio,pago) VALUES (:nombre,:dni,:alta,:direccion,:provincia,:municipio,:pago)')
            consulta.bindValue(':dni', str(newcli[1]))
            consulta.bindValue(':nombre', str(newcli[0]))
            consulta.bindValue(':alta', str(newcli[2]))
            consulta.bindValue(':direccion', str(newcli[3]))
            consulta.bindValue(':provincia', str(newcli[4]))
            consulta.bindValue(':municipio', str(newcli[5]))
            consulta.bindValue(':pago', str(newcli[6]))
            if consulta.exec():
              pass
            else:
               print('oh no')
            if newcar[0] == '':
                pass
            else:
                query1 = QtSql.QSqlQuery()
                query1.prepare(
                    'insert into coches (matricula,dnicli,marca,modelo,motor) VALUES (:matricula,:dnicli,:marca,:modelo,:motor)')
                query1.bindValue(':matricula', str(newcar[0]))
                query1.bindValue(':dnicli', str(newcli[1]))
                query1.bindValue(':marca', str(newcar[1]))
                query1.bindValue(':modelo', str(newcar[2]))
                query1.bindValue(':motor', str(newcar[3]))
                if query1.exec():
                    pass
                else:
                    print('oh no')
        except Exception as Error:
            print("error en altaExcelCoche",Error)

