import tkinter as tk
import tkinter
from tkinter.constants import END
import consultas

ventana = tkinter.Tk()
ventana.title("CEP Bus Rodrigo Bazán Proyecto Final")
ventana. geometry("1200x420")
ventana.resizable(0,0)
cabezera = tkinter.Label(ventana, text="Central de autobuses CEPBus, Bienvenido a bordo").pack()


listaConductores = tkinter.Listbox(ventana)
listaCamiones = tkinter.Listbox(ventana)
listaViajes = tkinter.Listbox(ventana)
def LeerConductores():
	listaConductores.delete(0,END)
	index = 0
	conductores = consultas.SelectConductor()
	for conductor in conductores:		
		index+=index
		listaConductores.insert(index, conductor[1] + ' '+conductor[2]+' '+conductor[3]+' '+str(conductor[4])+' '+conductor[5])
LeerConductores()

def LeerCamiones():
	listaCamiones.delete(0, END)
	index = 0
	camiones = consultas.SelectCamion()
	for camion in camiones:
		index += index
		listaCamiones.insert(
			index, camion[0]+' '+str(camion[1])+' '+camion[2]+' '+str(camion[3])+' '+str(camion[4]))
LeerCamiones()

def LeerViajes():
	listaViajes.delete(0, END)
	index = 0
	viajes = consultas.SelectViaje()
	for viaje in viajes:
		index += index
		listaViajes.insert(
			index, viaje[1]+' '+viaje[2]+' '+str(viaje[3])+' '+viaje[4])
LeerViajes()

def ConductorSeleccionado():
	for item in listaConductores.curselection():		
		stringg = (listaConductores.get(item)).split()				
		#LB = tkinter.Label(ventana, text=stringg[2]).pack()
	return(stringg[2])

def CamionSeleccionado():
	for item in listaCamiones.curselection():
		#LB = tkinter.Label(ventana, text=listaCamiones.get(item)).pack()
		stringg = (listaCamiones.get(item)).split()
		print(stringg[0],' ajsdja caminocito select')
	return(stringg[0])

def RegistroConductor():
	registerConductorWindow = tk.Toplevel(ventana)
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
	def Insert():
		nombre = NombreBox.get()
		apellidos = ApellidosBox.get()
		curp = CurpBox.get()
		edad = EdadBox.get()
		sexo = SexoBox.get()
		consultas.InsertConductor(nombre, apellidos, curp, edad, sexo)
		registerConductorWindow.destroy()		
		LeerConductores()
	btnInsertConductor = tk.Button(registerConductorWindow, text='Guardar Conductor', command=(Insert))
	btnInsertConductor.place(x=0,y=100)

def RegistroViaje():
	placas = CamionSeleccionado()
	registerViajeWindow = tk.Toplevel(ventana)
	labelNombre = tk.Label(registerViajeWindow, text='Origen')
	labelNombre.place(x=0, y=0)
	NombreBox = tk.Entry(registerViajeWindow)
	NombreBox.place(x=60, y=0)
	labelApellidos = tk.Label(registerViajeWindow, text='Destino')
	labelApellidos.place(x=0, y=20)
	ApellidosBox = tk.Entry(registerViajeWindow)
	ApellidosBox.place(x=65, y=20)
	labelCurp = tk.Label(registerViajeWindow, text='Lugares Disponibles')
	labelCurp.place(x=0, y=40)
	CurpBox = tk.Entry(registerViajeWindow)
	CurpBox.place(x=45, y=40)
	
	def Insert():
		origen = NombreBox.get()
		destino = ApellidosBox.get()
		lugaresd = CurpBox.get()		
		print(placas)

		consultas.InsertViaje(origen, destino, lugaresd, placas)
		registerViajeWindow.destroy()
		LeerViajes()
	btnInsertConductor = tk.Button(
		registerViajeWindow, text='GuardarViaje', command=(Insert))
	btnInsertConductor.place(x=0, y=100)

def EnviandoDatos():
	RegistroConductor()


btnRegisterConductor = tk.Button(ventana, text='Registrar Conductor', command= RegistroConductor)
btnSelecConductor = tkinter.Button(ventana, text="Seleccionar conductor", command=ConductorSeleccionado)
btnSelecConductor.place(x=75 ,y=160)
btnRegisterConductor.place(x=75 ,y=190)
btnRegisterCamion = tk.Button(ventana, text='Registrar Camion', command= RegistroConductor)
btnSelecCamion = tkinter.Button(ventana, text="Seleccionar camion", command=CamionSeleccionado)
btnSelecCamion.place(x=400 ,y=160)
btnRegisterCamion.place(x=400 ,y=190)
btnRegisterViaje = tk.Button(ventana, text='Registrar Viaje', command= RegistroViaje)
btnRegisterViaje.place(x=800 ,y=190)
listaConductores.place(x=0,y=60, width=250, height=100)
listaCamiones.place(x=275, y=60, width=350, height=100)
listaViajes.place(x=625, y=60, width=350, height=100)
ventana.mainloop()