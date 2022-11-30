import conexion
import var


class Clientes():
    '''
    Modulo para la validacion de Dni
    :return boolean
    '''

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
        except Exception as error:
            print('error')

    def limpiaCli(self=None):
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtDircli, var.ui.txtFechaAltaClin, var.ui.txtCar,
                       var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText(' ')
            if var.ui.chkTransferencia.isChecked():
                i.setChecked(False)

        except Exception as error:
            print('Error limpiar cliente', error)

    def borrarCli(self):
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
