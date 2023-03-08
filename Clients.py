import conexion
import var
from   dlgcalendar import   Ui_dlgcalendar

class Clientes():
    '''
    Modulo para la validacion de Dni
    :return boolean
    '''

    @staticmethod
    def validarDNI(dni):
        try:
            numeros = '1234567890'
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            ndni = ''
            leter = ''
            reemp_dig_ext = {'x': '0', 'Y': '1', 'Z': '2'}
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                for n in range(len(dni) -1):
                    ndni += dni[n]
                leter = int(ndni) % 23


                if (tabla[int(leter)] == dig_control):
                    return True


            return False
        except Exception as error:
            print('Error validar dni', error)

    def mostraValidodni(self=None):
        """
            modulo que valida espera a que se valide el dni y muestra un indicador de si es valido o no
        """
        try:
            dni = var.ui.txtDni.text()
            if Clientes.validarDNI(dni):
                var.ui.lblValidarDni.setStyleSheet('color: green')
                var.ui.lblValidarDni.setText('V')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: white')
            else:
                var.ui.lblValidarDni.setStyleSheet('color: red')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: red')
        except Exception as error:
            print("Error mostrar marcado validez dni:", error)

    def selMotor(self=None):
        try:
            var.motor = var.ui.rbtDiesel, var.ui.rbtGasolina, var.ui.rbtHibrido, var.ui.rbtElt
            for i in var.motor:
                i.toggled.connect(Clientes.checkMotor)
        except Exception as error:
            print('Error seleccion motor:', error)

    def checkMotor(self=None):
        try:
            if var.ui.rbtGasolina.isChecked():
                print('Gasolina')
                return 'Gasolina'
            elif var.ui.rbtDiesel.isChecked():
                print('Diesel')
                return 'Diesel'
            elif var.ui.rbtHibrido.isChecked():
                print('Hibrido')
                return 'Hibrido'
            elif var.ui.rbtElt.isChecked():
                print('Electrico')
                return 'Electrico'
            else:
                pass
        except Exception as error:
            print("Error seleccion motor", error)

    def guardarCli(self=None):
        """
        modulo que  toma los datos del cliente y coche y los pasa al modulo alta cli del fichero conexion
        """
        try:
            newcli = []
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaClin, var.ui.txtModelo]
            newcar = []
            for i in cliente:
                newcli.append(i.text())
            prov = var.ui.cmbProcli.currentText()
            newcli.append(prov)
            muni = var.ui.cmbMunicli.currentText()
            newcli.append(muni)
            pagos = []
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            elif var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            elif var.ui.chkTransferencia.isChecked():
                pagos.append('Transferencia')
            pagos = set(pagos)
            newcli.append('; '.join(pagos))
            print(newcli)

            car = {var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo}
            for i in car:
                newcar.append(i.text())
            motor = Clientes.checkMotor()
            newcar.append(motor)

            conexion.Conexion.altaCli(newcli, newcar)
            conexion.Conexion.mostrarTabcarcli()
        except Exception as error:
            print('error')

    def limpiaCli(self=None):
        """
        Limpia el campo de los clientes
        """
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtDircli, var.ui.txtFechaAltaClin, var.ui.txtMatricula,
                       var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText(' ')
            if var.ui.chkTransferencia.isChecked():
                var.ui.chkTransferencia.setCheckable()
            elif var.ui.chkEfectivo.isChecked():
                var.ui.chkEfectivo.setCheckable()
            elif var.ui.chkTarjeta.isChecked():
                var.ui.chkTarjeta.setCheckable()


        except Exception as error:
            print('Error limpiar cliente', error)

    def borrarCli(self):
        """
            invoca el metodo borrarCli de conexion al cual
        """
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borrarCli(dni)
            conexion.Conexion.mostrarTabcarcli(self)
        except Exception as error:
            print("error baja cliente y sus coches" + error)

    def modifCli(self):
        try:
            modcli = []
            modcar = []
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaAltaClin, var.ui.txtDircli]
            for i in cliente:
                modcli.append(i.text())
            prov = var.ui.cmbProcli.currentText()
            modcli.append(prov)
            muni = var.ui.cmbMunicli.currentText()
            modcli.append(muni)
            pagos = []
            if var.ui.chkTarjeta.isChecked():
                pagos.append("Tarjeta")
            if var.ui.chkTransferencia.isChecked():
                pagos.append("Transferencia")
            if var.ui.chkEfectivo.isChecked():
                pagos.append("Efectivo")
            pagos = set(pagos)
            modcli.append('; '.join(pagos))
            car = {var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo}
            for i in car:
                modcar.append(i.text())
            motor = Clientes.checkMotor()
            modcar.append(motor)

            conexion.Conexion.modificarCli(modcli, modcar)
            conexion.Conexion.mostrarTabcarcli()

        except Exception as Error:
            print("Error modificar datos clientes y sus coches ",Error)



    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAltaClin.setText(str(data))
            var.dlgcalendar.hide()


        except Exception as error:
            print('Error cargar fecha alta cliente  ', error)


    def GuardarServ(self):
        try:
            Con = var.ui.txtConcepto.text()
            Precio = var.ui.txtPrecioUnidad.text()
            if Precio.__contains__(','):
                pass
            else:
                Precio += ',00'
            conexion.Conexion.AltaServicio(Con,Precio)
            conexion.Conexion.mostrarTabServicios()
        except Exception as Error:
            print('Error en GuardarServ ',Error)
    def ModServ(self):
        try:
            codigo = var.ui.lbCodigo.text()
            Con = var.ui.txtConcepto.text()
            Precio = var.ui.txtPrecioUnidad.text()
            conexion.Conexion.ModificarServicio(Con, Precio,codigo)
            conexion.Conexion.mostrarTabServicios()
        except Exception as Error:
            print('Error en ModServ ',Error)
    def BorrarServ(self):
        try:
            codigo = var.ui.lbCodigo.text()
            conexion.Conexion.BorrarServicio(codigo)
            conexion.Conexion.mostrarTabServicios()
        except Exception as Error:
            print('Error en ModServ ',Error)

    def mostrarFormSer(self):
        try:
            row = var.ui.tabServicios.row(var.ui.tabServicios.currentItem())
            var.ui.lbCodigo.setText(var.ui.tabServicios.item(row,0).text())
            var.ui.txtConcepto.setText(var.ui.tabServicios.item(row,1).text())
            var.ui.txtPrecioUnidad.setText(var.ui.tabServicios.item(row,2).text())


        except Exception as Error:
            print('Error en mostrarFormSer' , Error)

    def mostrarFormCli(self):
        try:
            row = var.ui.tabClientes.row(var.ui.tabClientes.currentItem())
            dni = var.ui.tabClientes.item(row,0).text()
            var.ui.txtDni.setText(dni)
            var.ui.txtMatricula.setText(var.ui.tabClientes.item(row,1).text())
            var.ui.txtMarca.setText(var.ui.tabClientes.item(row,2).text())
            var.ui.txtModelo.setText(var.ui.tabClientes.item(row,3).text())
            if var.ui.tabClientes.item(row,4).text() == "Diesel":
                var.ui.rbtDiesel.setChecked(True)
            elif var.ui.tabClientes.item(row,4).text() == "Gasolina":
                var.ui.rbtGasolina.setChecked(True)
            elif var.ui.tabClientes.item(row,4).text() == "Hibrido":
                var.ui.rbtHibrido.setChecked(True)
            else:
                var.ui.rbtElt.setChecked(True)
            conexion.Conexion.conseguirCliente(var.ui.tabClientes.item(row,0).text())


        except Exception as Error:
            print('Error en mostarFormCli',Error)

    def mostrarFormFact(self):
        try:
            row = var.ui.tabFacturas.row(var.ui.tabFacturas.currentItem())
            NFact = var.ui.tabFacturas.item(row,0).text()
            cliente = var.ui.tabFacturas.item(row,1).text()
            conexion.Conexion.conseguirFact(NFact,cliente)
        except Exception as Error:
            print("Erroren mostrarFormFact",Error)