from reportlab.pdfgen import canvas

import conexion
import var
from ventana import Ui_ventana
from PyQt6 import QtSql
from PyQt6 import QtWidgets, QtCore

class facturas():


    def cargaLineaVentana(self= None):
        try:
            index = 0;
            var.cmbservicio = QtWidgets.QComboBox()
            var.txtUnidades = QtWidgets.QLineEdit()
            var.txtUnidades.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabVentas.setRowCount(index +1)
            var.ui.tabVentas.setCellWidget(index,0,var.cmbservicio)
            var.ui.tabVentas.setCellWidget(index, 1, var.txtUnidades)


        except Exception as Error:
            print("error en cargaLienaVentana facturas " + Error)

    def cargaPrecioVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            servicio = var.cmbservicio.currentText()
            datos = conexion.Conexion.obtenerPrecio(servicio)
            precio = datos
            var.idser = datos[0]
            var.precio = datos[1]
            precio = precio.replace(',', '.')
            var.ui.tabVentas.setItem(row,2,QtWidgets.QTableWidgetItem(str(precio)))
            var.ui.tabVentas.item(row,2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        except Exception as Error:
            print("error en carga Precio Venta",Error)

    def totalLineaventa(self = None):
        try:

            if str(var.ui.lblBusca.text()) == "":
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Datos del servicio Borrados con exito")
                msg.exec()
            else:
                venta = []
                venta.append(int(var.ui.lblBusca.text()))
                venta.append(int(var.idser))
                venta.append(round(float(var.precio),2))
                row = var.ui.tabVentas.currentRow()
                cantidad= var.ui.tabVentas.cellWidget(row,2).text()
                cantidad = cantidad.replace(",",".")
                venta.append(round(float(cantidad),2))
                totallineaVenta = round(float(var.precio)*round(float(cantidad,2)))
                totallineaVenta = str(f"{totallineaVenta:.2f}")
                totallineaVenta = totallineaVenta.replace('.',',') + ' €'
                var.ui.tabVentas.setItem(row,3,QtWidgets.QTableWidgetItem(str(totallineaVenta)))
                var.ui.tabVentas.item(row,3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        except Exception as Error:
            print("error en talt Linea venta ",Error)

    def cargaLineasVenta(codfact):
        try:
            suma = 0.0
            var.ui.tabServicios.clearContent()
            index = 0

            query = QtSql.QSqlQuery
            query.prepare("select codservicio,precio,unidades from ventas where codfact = :codfact")
            query.bindValue(":codfact", str(codfact))
            if query.exec():
                while query.next():
                    precio = str("{..2f}", format(round(query.value(1), 2)))
                    cantidad = str("{..2f}", format(query.value(2)))
                    servicio = conexion.Conexion.BuscarArt(int(query.value(0)))
                    suma = suma + (round(query.value(1) * query.value(2), 2))
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem)
                    var.ui.tabVentas.item(index, 0, ).setTextAligment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(servicio))
                    var.ui.tabVentas.item(index, 0).setTextAligment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(precio.replace(",", "."))))
                    var.ui.tabVentas.item(index, 1).setTextAligment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(cantidad.replace(",", "."))))
                    var.ui.tabVentas.item(index, 2).setTextAligment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(suma.replace(",", "."))))
                    index = index + 1
                var.ui.lblSubtotal.setText(str(2))

        except Exception as Error:
            print("exception en cargaLineasVentas ", Error)

    def createNewRow(self = None):
        try:
            index = var.ui.tabVentas.rowCount() + 1;
            var.ui.tabVentas.insertRow(index);
            var.cmbservicio = QtWidgets.QComboBox()
            var.txtUnidades = QtWidgets.QLineEdit()
            var.txtUnidades.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabVentas.setCellWidget(index, 0, QtWidgets.QComboBox())
            var.ui.tabVentas.setCellWidget(index, 1, QtWidgets.QLineEdit())


        except Exception as Error:
            print("exception en createNewRow " , Error)