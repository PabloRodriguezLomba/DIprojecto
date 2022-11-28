import sys,shutil,os
import zipfile
from datetime import date, datetime

import xlrd
import xlwt
import zipfile39
from PyQt6 import QtSql
from PyQt6.uic.properties import QtWidgets

import Clients
import conexion
import var


class Eventos:
        def Salir(self = None):
                try:
                    var.avisosalir.show()
                    if var.avisosalir.exec():
                        sys.exit()
                    else:
                        var.avisosalir.hide()
                except Exception as error:
                    print("Error en salir %s", str(error))
        def ExportDatos(self = None):
            try:
                var.dlgDatos.show()
            except Exception as error:
                print("Error en ExportarDatos")
        def letrasCapital(self = None):
            try:
                var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
                var.ui.txtDircli.setText(var.ui.txtDircli.text().title())
                var.ui.txtMatricula.setText(var.ui.txtCar.text().upper())
                var.ui.txtMarca.setText(var.ui.txtMarca.text().upper())
                var.ui.txtModelo.setText(var.ui.txtModelo.text().title())
            except Exception as error:
                print("Error capitalizar letras",error)

        def resizeTablacli(self):
            try:
                header = var.ui.tabClientes.horizontalHeader()
                for i in range(5):
                    header.setSectionResizeMode(i,QtWidgets.QHeaderview.Stretch)
                    if i == 0 or i == 1:
                        print(' ')
            except Exception as error:
                print('errorrr')

        def abrirCalendar(self = None):
            try:
                var.dlgcalendar.show()
                if var.dlgcalendar.exec():
                    sys.exit()
                else:
                    var.dlgcalendar.hide()
            except Exception as error:
                print('Error al abrir calendario')

        def crearBackup(self):
            try:

                fecha = datetime.today()
                fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
                copia = (str(fecha) +' _backup.zip')

                directorio, filename = var.dlgAbrir.getSaveFileName(None,'Guardar Copia',copia,' .zip')

                if var.dlgAbrir.Accepted and filename != '':
                    finchzip = zipfile.ZipFile(copia, 'w')
                    finchzip.write(var.bbdd, os.path.basename(var.bbdd),zipfile39.ZIP_DEFLATED)
                    finchzip.close()
                    shutil.move(str(copia),str(directorio))
                    msg = QtWidgets.QMessageBox()
                    msg.setModal(True)
                    msg.setWindowTittle('Arise')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('copia de Seguridad creada')
                    msg.exec()
            except Exception as error:
                print('Error crear backup', error)
        def restaurarBackup(self):
            try:
                filename = var.dlgAbrir.getOpenFileName(None,'Restaurar Copia Seguiridad','','*_zip::ALL Files')
                if var.dlgAbrir.accept and filename != '':
                    file = filename[0]
                    with zipfile.ZipFile(str(file),'r') as bbdd:
                        bbdd.extractall(pad=None)
                    bbdd.close()
                conexion.Conexion.conexion()
                conexion.Conexion.mostrarTabcarcli()
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTittle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad Restaurada')
                msg.exec()
            except Exception as error:
                print('Error al restaurar el backup' , error)
        def exportarDatos(self):
            try:

                fecha = datetime.today()
                fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
                file = (str(fecha) + ' _Clientes.xls')
                directorio,filename = var.dlgAbrir.getSaveFileName(None,'Guardar Datos',file, '.xls')

                wb = xlwt.Workbook();
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0,0,'DNI')
                sheet1.write(0,1,'Nombre')
                sheet1.write(0,2,'Fecha Alta')
                sheet1.write(0,3,'Direccion')
                sheet1.write(0,4,'Provincia')
                sheet1.wirte(0,5,'Municipio')
                sheet1.write(0,6,'Forma de pago')
                fila = 1
                query = QtSql.QSqlQuery()
                query.prepare('select * from clientes order by dni')
                if query.exec() :
                    while query.next():
                        sheet1.write(fila,0,str(query.value(0)))
                        sheet1.write(fila, 1, str(query.value(1)))
                        sheet1.write(fila, 2, str(query.value(2)))
                        sheet1.write(fila, 3, str(query.value(3)))
                        sheet1.write(fila, 4, str(query.value(4)))
                        sheet1.write(fila, 5, str(query.value(5)))
                        sheet1.write(fila, 6, str(query.value(6)))
                        fila = 2
                if (wb.save(directorio)):
                    msq = QtWidgets.QMessageBox()
                    msq.setModal(True)
                    msq.setWindowTittle('Aviso')
                    msq.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msq.setText('Exportacion de Datos Realizada')
                    msq.exec()


            except Exception as error:
                print('Error con el excel' + error)
        def importarDatos(self):
            try:
                filename = var.dlgAbrir.getOpenFileName(None, 'Importar datos:','',' *.xls;;All Files (*)')

                if var.dlgDatos.Accepted and filename != '':
                    file = filename[0]
                    documento = xlrd.open_workbook(file)
                    datos = documento.sheet_by_index(0)
                    files = datos.nrows
                    columns = datos.ncols
                    new = []
                    for i in range(files):
                        if i == 0:
                            pass
                        else:
                            new = []
                            for j in range(columns):
                                new.append(str(datos.call_value(i,j)))
                                if Clients.Clientes.validarDNI(str(new(0))):
                                    conexion.Conexion.altaExcelCoche(new)
                conexion.Conexion.mostrarTabcarcli()
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTittle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importacion de Datos Realizada')
                msg.exec()
            except Exception as error:
                print("error al importar datos " + error)