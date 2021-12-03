import tkinter as tk
import tkinter 
from tkinter.constants import END
from tkinter import messagebox
import consultas

def ActualizarDatos():     
     ventanaDatos = tk.Tk()          
     ventanaDatos.title("Ingresando Datos")
     ventanaDatos.geometry("720x480")
     ventanaDatos.resizable(0,0)
     cabezera = tk.Label(ventanaDatos, text="Registrando choferes, camiones y viajes")
     registerConductorWindow = ventanaDatos
     def RegistroConductor():                    
          listaConductores = tkinter.Listbox(ventanaDatos)
          listaCamiones = tkinter.Listbox(ventanaDatos)
          listaViajes = tkinter.Listbox(ventanaDatos)          
          labelNombre = tk.Label(registerConductorWindow, text = 'Nombre(s)')
          labelNombre.place(x=0,y=0)
          NombreBox = tk.Entry(registerConductorWindow)
          NombreBox.place(x=60,y=0)
          labelApellidos = tk.Label(registerConductorWindow, text='Apellidos(s)')
          labelApellidos.place(x=0, y=20)
          ApellidosBox = tk.Entry(registerConductorWindow)
          ApellidosBox.place(x=65,y=20)
          labelCurp = tk.Label(registerConductorWindow, text='CURP')
          labelCurp.place(x=0, y=40)
          CurpBox = tk.Entry(registerConductorWindow)
          CurpBox.place(x=45, y=40)
          labelEdad = tk.Label(registerConductorWindow, text='Edad')
          labelEdad.place(x=0, y=60)
          EdadBox = tk.Entry(registerConductorWindow)
          EdadBox.place(x=45, y=60)
          labelSexo = tk.Label(registerConductorWindow, text='Sexo')
          labelSexo.place(x=0, y=80)
          SexoBox = tk.Entry(registerConductorWindow)
          SexoBox.place(x=45, y=80)          

               
          def LeerConductores():
               listaConductores.delete(0,END)
               index = 0
               conductores = consultas.SelectConductor()
               for conductor in conductores:		
                    index+=index
                    listaConductores.insert(index, conductor[1] + ' '+conductor[2]+' '+conductor[3]+' '+str(conductor[4])+' '+conductor[5])

          def LeerCamiones():
               listaCamiones.delete(0, END)
               index = 0
               camiones = consultas.SelectCamion()
               for camion in camiones:
                    index += index
                    listaCamiones.insert(index, camion[0]+' '+str(camion[1])+' '+camion[2]+' '+str(camion[3])+' '+str(camion[4]))

          def LeerViajes():
               listaViajes.delete(0, END)
               index = 0
               viajes = consultas.SelectViaje()
               for viaje in viajes:
                    index += index
                    listaViajes.insert(index, viaje[1]+' '+viaje[2]+' '+str(viaje[3])+' '+viaje[4])
     
          def Guardarconductor():
               nombre = NombreBox.get()
               apellidos = ApellidosBox.get()
               curp = CurpBox.get()
               edad = EdadBox.get()
               sexo = SexoBox.get()
               consultas.InsertConductor(nombre, apellidos, curp, edad, sexo)               
               messagebox.showinfo(message=(nombre, apellidos, curp, edad, sexo, ' Guardado con exito'), title="Título")
               LeerConductores()
          
          btnInsertConductor = tk.Button(registerConductorWindow, text='Guardar Conductor', command=(Guardarconductor))
          btnInsertConductor.place(x=0,y=100)          
     def RegistroCamion():
          registerViajeWindow=ventanaDatos          
          labelAsientos = tk.Label(registerViajeWindow, text='Asientos')
          labelAsientos.place(x=250, y=40)          
          AsientosBox = tk.Entry(registerViajeWindow)
          AsientosBox.place(x=300, y=40)
          labelAbordaje = tk.Label(registerViajeWindow, text='Hora Ab')
          labelAbordaje.place(x=250, y=60)
          abordajeBox = tk.Entry(registerViajeWindow)
          abordajeBox.place(x=300, y=60)
          labelSalida = tk.Label(registerViajeWindow, text='Hora Sal')
          labelSalida.place(x=250, y=80)
          SalidaBox = tk.Entry(registerViajeWindow)
          SalidaBox.place(x=300, y=80)
          labelModelo = tk.Label(registerViajeWindow, text='Modelo')
          labelModelo.place(x=250, y=100)
          modeloBox = tk.Entry(registerViajeWindow)
          modeloBox.place(x=300, y=100)
          labelplacas = tk.Label(registerViajeWindow, text='Placas')
          labelplacas.place(x=250, y=120)
          placasBox = tk.Entry(registerViajeWindow)
          placasBox.place(x=300, y=120)
          def GuardarAutobus():
               def itemSelect():
                    for item in listaConductores.curselection():
                         i =listaConductores.get(item)                    
                    cadena = i.split()                                      
                    id =str(consultas.id_conductor(cadena[-3]))
                    id = id[1:5]                    
                    placas = str(placasBox.get()  )
                    horaab = str(abordajeBox.get())
                    modelo = str(modeloBox.get())
                    horaSal = str(SalidaBox.get())
                    capacidad = int(AsientosBox.get())
                    consultas.InsertCamion(placas, horaab,  horaSal, modelo, capacidad, id)
                    #InsertCamion('GRL212','2021-10-12 14:30:00:00','2021-10-12 14:40:00:00', 'Mercedez', 45,10)
               ventanaSelecConductor = tk.Tk()
               ventanaSelecConductor.title("Selecciona el conductor para este bus")
               ventanaSelecConductor.geometry("300x300")
               listaConductores = tk.Listbox(ventanaSelecConductor, width=200, height=200)
               btnSelectConductor = tk.Button(ventanaSelecConductor, text='Guardar Conductor', command=(itemSelect))
               listaConductores.delete(0,END)
               index = 0
               conductores = consultas.SelectConductor()               
               for conductor in conductores:		
                    index+=index
                    listaConductores.insert(index, conductor[1] + ' '+conductor[2]+' '+conductor[3]+' '+str(conductor[4])+' '+conductor[5])
               listaConductores.place(x=0,y=0)
               btnSelectConductor.place(x=150, y=180)
               ventanaSelecConductor.mainloop()
          btnInsertConductor = tk.Button(registerConductorWindow, text='Guardar Autobus', command=(GuardarAutobus))
          btnInsertConductor.place(x=300, y=140)
     def RegistroViaje():
          registerViajeWindow=ventanaDatos
          labelOrigen = tk.Label(registerViajeWindow, text='Origen')
          labelOrigen.place(x=425, y=0)
          OrigenBox = tk.Entry(registerViajeWindow)
          OrigenBox.place(x=475, y=0)
          labelDestino = tk.Label(registerViajeWindow, text='Destino')
          labelDestino.place(x=425, y=20)
          DestinoBox = tk.Entry(registerViajeWindow)
          DestinoBox.place(x=475, y=20)
          def guardarViaje():
               lc = consultas.SelectCamion()
               listaCamiones = tkinter.Listbox(ventanaDatos)
               origen = OrigenBox.get()
               destino = DestinoBox.get()
               for item in listaCamiones.curselection():
                    i = listaCamiones.get(item)
               cadena = i.split()                                      
               id =str(consultas.id_conductor(cadena[-3]))
               #consultas.InsertViaje(origen,destino,cadena[4],cadena[0])               
               def itemSelectViaje():
                    index = 0
                    camiones = consultas.SelectCamion()
                    for camion in lc:
                         index += index
                         listaCamiones.insert(index, camion[0]+' '+str(camion[1])+' '+camion[2]+' '+str(camion[3])+' '+str(camion[4]))          
               ventanaSelecCamion = tk.Tk()
               ventanaSelecCamion.title("Selecciona el bus para este viaje")
               ventanaSelecCamion.geometry("300x300")
               listaCamiones = tk.Listbox(ventanaSelecCamion, width=200, height=200)               
               btnSelectConductor = tk.Button(ventanaSelecCamion, text='Guardar viaje', command=(itemSelectViaje))
               listaCamiones.delete(0,END)
               index = 0               
               conductores = consultas.SelectCamion()               
               for conductor in conductores:		
                    index+=index
                    listaCamiones.insert(index, conductor[0] + ' '+str(conductor[1])+' '+str(conductor[2])+' '+str(conductor[4])+' '+str(conductor[5]))
               listaCamiones.place(x=0,y=0)
               btnSelectConductor.place(x=150, y=180)
               ventanaSelecCamion.mainloop()

          btnInsertConductor = tk.Button(registerConductorWindow, text='Guardar Viaje', command=(guardarViaje))
          btnInsertConductor.place(x=300, y=140)
          
     
     RegistroConductor()
     RegistroCamion()
     RegistroViaje()
     #btnSelecConductor = tkinter.Button(ventanaDatos, text="Seleccionar conductor", command=ConductorSeleccionado)
     
def VenderBoletos():
     ventanaDatos = tk.Tk()
     ventanaDatos.title("Ingresando informacion")
     ventanaDatos. geometry("1200x420")
     ventanaDatos.resizable(0,0)
     cabezera = tk.Label(ventanaDatos, text="Central de autobuses CEPBus, Bienvenido a bordo").pack()

def PantallaInicio():
     ventana = tk.Tk()
     ventana.title("Bienvenido a CEPBus")
     ventana. geometry("240x240")
     ventana.resizable(0,0)
     cabezera = tk.Label(ventana, text="Selecciona un modo").pack()
     btnActualizarDatos = tk.Button(ventana, text='Actualizar Datos', command= ActualizarDatos)
     btnActualizarDatos.place(x=50 ,y=150)     
     btnVenderBoletos = tk.Button(ventana, text="Vender Boletos", command=VenderBoletos)     
     btnVenderBoletos.place(x=50, y=50)
     ventana.mainloop()

PantallaInicio()
#2021-10-10 14:05:00