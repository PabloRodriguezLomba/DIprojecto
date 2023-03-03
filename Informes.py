from datetime import datetime

from PyQt6 import QtSql
from PyQt6.uic.properties import QtWidgets

import conexion
import var,os
from reportlab.pdfgen import canvas
class Informes:
    def listClientes(self):
        try:
            var.report = canvas.Canvas("Informes/ListadoClientes.pdf")
            var.report.drawString(50,700,"Listado Clientes")
            Informes.pieInforme(self)
            Informes.topInforme(self)
            Items = ('DNI','Nombre','Direccion','Municipio','Provincia')
            var.report.setFont('Helvetica-Bold',size=10)
            var.report.drawString(60,675,str(Items[0]))
            var.report.drawString(120, 675, str(Items[1]))
            var.report.drawString(270, 675, str(Items[2]))
            var.report.drawString(370, 675, str(Items[3]))
            var.report.drawString(460, 675, str(Items[4]))
            var.report.line(50,670,525,670)

            query = QtSql.QSqlQuery()
            query.prepare("select * from clientes")
            if query.exec():
                var.report.setFont('Helvetica',size=10)
                fac = 650
                while query.next():
                    dni=str(query.value(1))
                    var.report.drawString(60,fac,'*****'+dni[5:9])
                    var.report.drawString(120,fac,str(query.value(0)))
                    var.report.drawString(270, fac, str(query.value(2)))
                    var.report.drawString(370, fac, str(query.value(3)))
                    var.report.drawString(460, fac, str(query.value(4)))
                    fac -=30
            var.report.save()
            reportPath = '.\\Informes'
            for file in os.listdir(reportPath):
                if file.endswith('Clientes.pdf'):
                    os.startfile(os.path.join(reportPath,file))



        except Exception as Error:
            print("Error informes estado cliente",Error)

    def pieInforme(self):
        try:
            var.report.line(50,50,525,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y.%H.%M.%S')
            var.report.setFont('Helvetica-Oblique',size=7)
            var.report.drawString(250,40,str(fecha))
            var.report.drawString(475,40,str('Pagina' + str(var.report.getPageNumber())))

        except Exception as Error:
            print("Error en pie de pagina",Error)

    def topInforme(self):
        try:
            logo = '.\img\logo.png'
            var.report.line(50,800,525,800)
            var.report.setFont('Helvetica-Bold', size=16)
            var.report.drawString(50,785,'Taller mecanico Teis ')
            var.report.line(50,712,525,713)
            var.report.drawImage(logo,430,740,width=80,height=45)
            var.report.setFont('Helvetica',size=9)
            var.report.drawString(55,770,'CIF')


        except Exception as error:
            print("error en topInfrome",error)


    def listCoches(self):
        try:
            var.report = canvas.Canvas("Informes/ListadoCoches.pdf")
            var.report.drawString(50,700,"Listado Coches")
            Informes.pieInforme(self)
            Informes.topInforme(self)
            Items = ('DNI','Matricula','Marca','Modelo','Motor')
            var.report.setFont('Helvetica-Bold',size=10)
            var.report.drawString(60,675,str(Items[0]))
            var.report.drawString(120, 675, str(Items[1]))
            var.report.drawString(270, 675, str(Items[2]))
            var.report.drawString(370, 675, str(Items[3]))
            var.report.drawString(460, 675, str(Items[4]))
            var.report.line(50,670,525,670)

            queryo = QtSql.QSqlQuery()
            queryo.prepare("select * from coches")
            if queryo.exec():
                var.report.setFont('Helvetica',size=10)
                fac = 650
                while queryo.next():
                    dni=str(queryo.value(1))
                    var.report.drawString(120,fac,str(queryo.value(0)))
                    var.report.drawString(60, fac, '*****' + dni[5:9])
                    var.report.drawString(270, fac, str(queryo.value(2)))
                    var.report.drawString(370, fac, str(queryo.value(3)))
                    var.report.drawString(460, fac, str(queryo.value(4)))
                    fac -=30
            var.report.save()
            reportPath = '.\\Informes'
            for file in os.listdir(reportPath):
                if file.endswith('Coches.pdf'):
                    os.startfile(os.path.join(reportPath,file))



        except Exception as Error:
            print("Error informes estado cliente",Error)

        def factura(self):
            try:
                var.report = canvas.Canvas("Informes/Factura.pdf")
                titulo = "FACTURA"
                Informes.pieInforme()
                Informes.topInforme()
                cliente = []
                nfac = str(var.ui.lblNumfac.text())
                fechaFac = str(var.ui.txt)
                if nfac == "":
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText("Seleccione una Factura")
                    msg.exec()
                dni = str(var.ui.lblDnifact.text())
                cliente = conexion.Conexion.oneCli(dni)



                var.report.setFont("Helvetica-bold",size=9)
                var.report.drawString(55,680,"Datos Cliente")
                var.report.drawString(400,660," Nº Factura: ")
                var.report.drawString(400,645,"Fecha Factura: ")
                var.report.setFont("Helvetica", size=9)
                var.report.drawString(55,675,"DNI/Cif" + str(dni))
                var.report.drawString(480,660,str(nfac))
                var.report.drawString(480,645,str(fechaFac))
                var.report.drawString(55,660,"Nombre" + str(cliente[0]))
                var.report.drawString(55,645,"Direccion" + str(cliente[2]))
                var.report.drawString(55,630,"Municipio" + str(cliente[4]))
                var.report.drawString(55,615,"Provincia" + str(cliente[3]))
                var.report.save()
                reportPath = '.\\Informes'
                for file in os.listdir(reportPath):
                    if file.endswith('Factura.pdf'):
                        os.startfile(os.path.join(reportPath, file))
            except Exception as Error:
                print("error en factura:", Error)