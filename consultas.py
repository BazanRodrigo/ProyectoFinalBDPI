from tkinter.constants import INSERT
import pyodbc as pdb

servidor = 'localhost'
bd = 'CEPBus'
user = 'root'
password = 'pass'

try:
	conexion = pdb.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' 
     +servidor+';DATABASE='+bd+';UID='+user+';PWD='+password)
	print('Conexion exitosa')
except:
	print("Conexión erronea")

def ReiniciarBase():
	# Se eliminan todos los datos de la BD	Este metodo ayudará a limpiar la BD
     qry = conexion.cursor()
     truncate = "DELETE FROM Conductor"
     qry.execute(truncate)
     qry.commit()	
     truncate = "DELETE FROM Cliente"
     qry.execute(truncate)
     qry.commit()     #Instrucción para enviar cambios al server de SQL
# Consultando Base de datos
#Se genero un
def SelectCliente():     
     qry = conexion.cursor()
     qry.execute("select * from Cliente;")
     Cliente = qry.fetchone()
     while Cliente:
          print(Cliente)
          Cliente = qry.fetchone()
     qry.close()

def SelectCamion():
     qry = conexion.cursor()
     qry.execute("select * from Camion;")
     conductores = qry.fetchall()
     qry.close()
     print("Seleccionando camion")
     print(conductores)
     return conductores

def SelectConductor():
     qry = conexion.cursor()
     qry.execute("select * from Conductor;")
     conductores = qry.fetchall()
     qry.close()
     print(conductores)
     return conductores

def SelectInfoViaje():
     qry = conexion.cursor()
     qry.execute("select * from InfoViaje;")
     Cliente = qry.fetchall()
     while Cliente:
          print(Cliente)
          Cliente = qry.fetchone()
     qry.close()

def SelectViaje():
     qry = conexion.cursor()
     qry.execute("select * from Viaje;")
     Cliente = qry.fetchall()     
     qry.close()
     return Cliente

def InsertCliente(nombre, edad):
     # Insertando a Base de datos
     qry = conexion.cursor()
     insert = "insert into Cliente Values(?, ?);"
     qry.execute(insert, nombre, edad)
     qry.commit()
     qry.close()

def InsertConductor(nombre, apellidos, curp, edad, sexo, placas):
     qry = conexion.cursor()
     insert = ("insert into Conductor (Nombre, Apellidos, CURP, Edad, Sexo, placas) values (?, ?, ?, ?, ?, ?)")
     qry.execute(insert, nombre, apellidos, curp, edad, sexo, placas)
     print(nombre, apellidos, curp, edad, sexo,'Insertado con exito')
     qry.commit()
     qry.close()     

def InsertCamion(Placas, Modelo, Capacidad):
     qry = conexion.cursor()
     insert = ("insert into Camion values (?, ?, ?)")
     qry.execute(insert, Placas,  Modelo, Capacidad)
     qry.commit()
     qry.close()
     print(Placas,  Modelo, Capacidad, 'Ingresado con exito')

def InsertViaje(Origen, Destino, LugaresDisponibles, horaSalida, id_conductor):
     qry = conexion.cursor()
     insert = ("insert into Viaje values (?, ?, ?, ?, ?)")
     qry.execute(insert, Origen, Destino, LugaresDisponibles, horaSalida, id_conductor)
     qry.commit()
     qry.close()

def InsertInfoViaje(id_cliente, id_viaje):
     qry = conexion.cursor()
     insert = ("insert into InfoViaje values (?, ?)")
     qry.execute(insert, id_cliente, id_viaje)
     qry.commit()
     qry.close()

def get_id_conductor(placas):
     qry = conexion.cursor()
     select = ("SELECT id_conductor FROM Conductor WHERE Placas=?;")
     qry.execute(select, placas)
     for row in qry.fetchall():
          id_conductor = row
     return id_conductor

def get_placas(id_conductor):
     qry = conexion.cursor()
     select = ("SELECT placas FROM Camion WHERE id_conductor=?;")
     qry.execute(select, id_conductor)
     for row in qry.fetchall():
          placas = row
     qry.close()
     placass = str(placas)
     placass = placass[2:-4]
     print(placass)
     return placass    

def get_Id_viaje(o, d):
     qry = conexion.cursor()
     select = ("SELECT Id_viaje FROM Viaje where Origen= ? and Destino=?")
     qry.execute(select, o, d)
     for row in qry.fetchall():
          Id_viaje = row
     qry.close()
     return Id_viaje   

def get_Id_Cliente(Nombre):
     qry = conexion.cursor()
     select = ("SELECT Id_Cliente FROM Cliente WHERE Nombre=?;")
     qry.execute(select, Nombre)
     for row in qry.fetchall():
          Id_Cliente = row
     qry.close()
     return Id_Cliente

def get_id_boleto(Id_cliente, Id_viaje):
     qry = conexion.cursor()
     select = ("SELECT id_boleto FROM InfoViaje WHERE Id_Cliente=? and WHERE Id_viaje=?;")
     qry.execute(select, Id_cliente, Id_viaje)
     for row in qry.fetchall():
          id_boleto = row
     qry.close()
     return id_boleto

def get_LugaresDisponibles(placas):
     qry = conexion.cursor()
     select = ("SELECT Capacidad FROM Camion WHERE placas=?;")
     qry.execute(select, placas)
     for row in qry.fetchall():
          lds = row
     qry.close()
     LugaresDisponibles = str(lds) [1:-3]
     print(LugaresDisponibles)
     return LugaresDisponibles

def updateLugaresDisponibles(id_viaje):     
     qry = conexion.cursor()
     ld = int(get_LugaresDisponibles(id_viaje))
     ld = ld-1     
     update = ("update viaje set LugaresDisponibles= ? where Id_viaje = ?")
     qry.execute(update, ld, id_viaje)
     qry.commit()
     qry.close()


def main():
     InsertCamion('RCP140','VW 2009', 60)
     InsertConductor('Rodolfo', 'Cota Sostigo',  'COSR190814HOLSRAA4',56, 'Hombre', 'RCP140' )
     InsertViaje('Puebla', 'Tlaxcala',56, '2021-10-12 14:30:00:00',7)
     InsertCliente('Rodrigo Bazán Zuirta', 21)
     SelectConductor()
     SelectCamion()
     SelectViaje()
     SelectCliente()
     SelectInfoViaje()

     
     


if __name__ == '__main__':
     main()


         #Primero se introducen los datos del Conductor, de ahí, Camion, Viaje, Cliente y al final se genera el boleto
     #ReiniciarBase()
     #InsertCliente('Cliente Jajaja', 21)
     #InsertInfoViaje(1003, 3003)
     #InsertCamion('GRL212','2021-10-12 14:30:00:00','2021-10-12 14:40:00:00', 'Mercedez', 45,10)
     #SelectCamion()
     #SelectCliente()
     #SelectConductor
     #SelectInfoViaje
     #SelectViaje
     #get_LugaresDisponibles(3003)
     #updateLugaresDisponibles(3003)
     #estados = ['Puebla', 'CDMX', 'Tlaxcala', 'Veracruz', 'Oaxaca', 'Cuernavaca', 'Guerrero', 'Monterrey', 'Baja California sur', 'Baja California norte']
     #j = 9
     #for i in range(10):
     #     InsertViaje(estados[i], estados[j], 50, '2021-12-02 08:20:00.000', 5 )
     #     #print(i,j)
     #     j = j-1
