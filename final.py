import pyodbc as pdb
servidor = 'localhost'
bd = 'CEPBus'
user = 'root'
password = 'pass'

try:
	conexion = pdb.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' +servidor+';DATABASE='+bd+';UID='+user+';PWD='+password)
	print('Conexion exitosa')
except:
	print("Noup")

def ReiniciarBase():
	# Se eliminan todos los datos de la BD	
     qry = conexion.cursor()
     truncate = "DELETE FROM Conductor"
     qry.execute(truncate)
     qry.commit()	
     truncate = "DELETE FROM Cliente"
     qry.execute(truncate)
     qry.commit()     
# Consultando Base de datos
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
     insert = ("insert into Conductor (Nombre, Apellidos, CURP, Edad, Sexo, Placas) values (?, ?, ?, ?, ?,?)")
     qry.execute(insert, nombre, apellidos, curp, edad, sexo, placas)
     qry.commit()
     qry.close()     

def InsertCamion(Placas, Modelo, Capacidad):
     qry = conexion.cursor()
     insert = ("insert into Camion values (?, ?, ?)")
     qry.execute(insert, Placas, Modelo, Capacidad)
     qry.commit()
     qry.close()

def InsertViaje(Origen, Destino, LugaresDisponibles, PlacasV):
     qry = conexion.cursor()
     insert = ("insert into Viaje values (?, ?, ?, ?)")
     qry.execute(insert, Origen, Destino, LugaresDisponibles, PlacasV)
     qry.commit()
     qry.close()

def InsertInfoViaje(id_cliente, id_viaje):
     qry = conexion.cursor()
     insert = ("insert into InfoViaje values (?, ?)")
     qry.execute(insert, id_cliente, id_viaje)
     qry.commit()
     qry.close()

def id_conductor(curp):
     qry = conexion.cursor()
     select = ("SELECT id_conductor FROM Conductor WHERE CURP=?;")
     qry.execute(select, curp)
     for row in qry.fetchall():
          id = row
     return id

def placas(id_c):
     qry = conexion.cursor()
     select = ("SELECT placas FROM Camion WHERE id_conductor=?;")
     qry.execute(select, id_c)
     for row in qry.fetchall():
          placas = row
     return placas
     qry.close()

def updateModelo(modelo1, modelo2):
     qry = conexion.cursor()
     select = ("update Camion set Modelo = ? where Modelo = ?")
     qry.execute(select, modelo1,modelo2)
     qry.commit()
     qry.close()
    

def main():
     #Primero se introducen los datos del Conductor, de ahí, Camion, Viaje, Cliente y al final se genera el boleto
     #ReiniciarBase()
     #InsertCamion('GRL212', 'RUTA', 45)     
     #InsertCamion('CEP084', 'RUTA', 45)     
     #InsertCamion('DFA145', 'RUTA', 45)     
     #InsertCamion('FASD45', 'RUTA', 45)
     #InsertCamion('FAS785', 'NISSAN', 45)
     #InsertCamion('FSDA00', 'IBIZA', 45)
     
     InsertConductor('Rodrigo', 'Bazán Zurita', 'BAZR010114HPLZRDA1', 20, 'Hombre','GRL212')
     InsertConductor('Karla', 'Hernandez Morales', 'HEMK111101HPLZRDA1', 20, 'Mujer','CEP084')
     InsertConductor('Diego', 'Bazán Zurita', 'BAZD150904HPLZRDA1', 16, 'Hombre','DFA145' )
     InsertConductor('Itzel', 'Ramirez Conde', 'RACI041201HPLZRDA1', 20, 'Mujer','FASD45')
     InsertConductor('Alejandro', 'Galan Bautista', 'GABA240901HPLZRDA1', 20, 'Hombre','FAS785')
     InsertConductor('America', 'García Chapul', 'GACA090101HPLZRDA1', 20, 'Mujer','FSDA00')
     
     #SELECT conductor
     Conductores = SelectConductor()

     print("Extraemos todos los conductores")
     for conductor in Conductores:
          print (conductor)
     
     print("Extraemos todos los CURP de conductor")
     for conductor in Conductores:
          print (conductor[3])

     #id_conductor
     listaCond = []
     print("Extraemos el id de conductor")
     for conductor in Conductores:
          print(str(id_conductor(conductor[3]))[1:5])
          listaCond.append(str(id_conductor(conductor[3]))[1:5])
     #insertando camiones     
     i=0
     
     '''
     ReiniciarBase()
     '''
if __name__ == '__main__':
     main()