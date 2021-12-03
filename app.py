from re import split
from tkinter import *
import tkinter
from babel.dates import datetime_
from tkcalendar import *
import tkinter as tk
import consultas
from datetime import datetime


def GenerarViaje():
     GenerarViajeVentana = Tk()
     GenerarViajeVentana.title("Proyecto Final")
     GenerarViajeVentana.geometry("1200x420")
     GenerarViajeVentana.resizable(0, 0)
     GenerarViajeVentana.config(bg="#cd950c")
     hour_string = StringVar()
     min_string = StringVar()
     last_value_sec = ""
     last_value = ""
     f = ('Times', 20)
     def display_msg():
          date = cal.get_date()
          m = min_sb.get()
          h = sec_hour.get()
          s = sec.get()
          t = f"Your appointment is booked for {date} at {m}:{h}:{s}."
          msg_display.config(text=t)
     if last_value == "59" and min_string.get() == "0":
          hour_string.set(int(hour_string.get()) +
                         1 if hour_string.get() != "23" else 0)
          last_value = min_string.get()
     if last_value_sec == "59" and sec_hour.get() == "0":
          min_string.set(int(min_string.get())+1 if min_string.get() != "59" else 0)
     if last_value == "59":
          hour_string.set(int(hour_string.get()) +
                         1 if hour_string.get() != "23" else 0)
          last_value_sec = sec_hour.get()
     fone = Frame(GenerarViajeVentana)
     ftwo = Frame(GenerarViajeVentana)
     fone.place(x=900,y=50)
     ftwo.place(x=945, y=250)
     cal = Calendar(
          fone,
          selectmode="day",
          year=2021,
          month=12,
          day=2
     )
     cal.pack()
     min_sb = Spinbox(
          ftwo,
          from_=0,
          to=23,
          wrap=True,
          textvariable=hour_string,
          width=2,
          state="readonly",
          font=f,
          justify=CENTER
     )
     sec_hour = Spinbox(
          ftwo,
          from_=0,
          to=59,
          wrap=True,
          textvariable=min_string,
          font=f,
          width=2,
          justify=CENTER
     )
     sec = Spinbox(
          ftwo,
          from_=0,
          to=59,
          wrap=True,
          textvariable=sec_hour,
          width=2,
          font=f,
          justify=CENTER
     )
     min_sb.pack(side=LEFT, fill=X, expand=True)
     sec_hour.pack(side=LEFT, fill=X, expand=True)
     sec.pack(side=LEFT, fill=X, expand=True)
     msg = Label(
          GenerarViajeVentana,
          text="Hour  Minute  Seconds",
          font=("Times", 12),
          bg="#cd950c"
     )
     msg.place(x=945,y=290)
     
     msg_display = Label(
          GenerarViajeVentana,
          text="",
          bg="#cd950c"
     )
     msg_display.pack(pady=10)
     ########################################Lista Camion########################################
     ventana = GenerarViajeVentana
     listaCamiones = tkinter.Listbox(ventana)
     
     listaCamiones.delete(0, END)
     index = 0
     camiones = consultas.SelectCamion()
     for camion in camiones:
          index += index
          print(camion)
          listaCamiones.insert(index, camion[0]+' '+str(camion[1])+' '+str(camion[2]))
     
     mensajelistaCamiones = tk.Label(ventana, text="Selecciona el camion que se encarga del traslado")
     listaCamiones.place(x=50,y=50)
     mensajelistaCamiones.place(x=0,y=20)
     labelOrigen = tk.Label(ventana, text='Origen')
     labelOrigen.place(x=200, y=50)
     OrigenBox = tk.Entry(ventana)
     OrigenBox.place(x=250, y=50)
     labelDestino = tk.Label(ventana, text='Destino')
     labelDestino.place(x=200, y=80)
     DestinoBox = tk.Entry(ventana)
     DestinoBox.place(x=250, y=80)
     def itemSelect():
          for item in listaCamiones.curselection():
               i = listaCamiones.get(item)
          print(i, 'Seleccionado')
          p = i.split(' ')
          placas = p[0]
          print(placas)
          salida = OrigenBox.get()
          llegada = DestinoBox.get()          
          date = cal.get_date()
          fecha = date.split('/')
          m = min_sb.get()
          h = sec_hour.get()
          s = sec.get()
          salidahora = datetime(int(fecha[2])+2000, int(fecha[1]), int(fecha[0]), int(m), int(h), int(s), 00)
          print(fecha)
          print(salidahora)          
          lugares = int(consultas.get_LugaresDisponibles(placas))
          print('Salida ',type(salida))
          print('llegada ',type(llegada))
          print('lugares ',type(salidahora))
          placaas = str(consultas.get_id_conductor(placas))
          plc = placaas[1]
          print(plc)
          consultas.InsertViaje(salida,llegada, lugares,salidahora,plc)
          
          
     def guardarviaje():
          itemSelect()
          print()
     actionBtn = Button(
          GenerarViajeVentana,
          text="Guardar Viaje",
          padx=10,
          pady=10,
          command=guardarviaje
     )
     actionBtn.place(x=950, y=310)
     GenerarViajeVentana.mainloop()

def IngresarConductor():
     ventanaDatos = tk.Tk()          
     ventanaDatos.title("Ingresando Datos")
     ventanaDatos.geometry("240x240")
     ventanaDatos.resizable(0,0)     
     registerConductorWindow = ventanaDatos          
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
     labelPlacas = tk.Label(registerConductorWindow, text='Placas')
     labelPlacas.place(x=0, y=100)
     PlacasBox = tk.Entry(registerConductorWindow)
     PlacasBox.place(x=45, y=100)
     def SendData():
          nombre = NombreBox.get()
          apellidos = ApellidosBox.get()
          curp = CurpBox.get()
          edad = EdadBox.get()
          sexo = SexoBox.get()
          placas = PlacasBox.get()
          if (placas == ''):
               placas = 'NULL'
          consultas.InsertConductor(nombre, apellidos, curp, edad, sexo, placas)
          ventanaDatos.destroy()

     btnEnviarDatos = tk.Button(ventanaDatos, text='Guardar conductor', command= SendData)
     btnEnviarDatos.place(x=45, y = 120)

def IngresarCamion():
     registerViajeWindow = tk.Tk()
     registerViajeWindow.title("Ingresando Datos")
     registerViajeWindow.geometry("240x240")
     registerViajeWindow.resizable(0, 0)
     labelplacas = tk.Label(registerViajeWindow, text='Placas')
     labelplacas.place(x=0, y=20)
     placasBox = tk.Entry(registerViajeWindow)
     placasBox.place(x=50, y=20)
     labelAsientos = tk.Label(registerViajeWindow, text='Asientos')
     labelAsientos.place(x=0, y=40)          
     AsientosBox = tk.Entry(registerViajeWindow)
     AsientosBox.place(x=50, y=40)     
     labelModelo = tk.Label(registerViajeWindow, text='Modelo')
     labelModelo.place(x=0, y=60)
     modeloBox = tk.Entry(registerViajeWindow)
     modeloBox.place(x=50, y=60)          
     def SendData():
          placas = str(placasBox.get()  )          
          modelo = str(modeloBox.get())          
          capacidad = int(AsientosBox.get())
          consultas.InsertCamion(placas, modelo, capacidad)
          registerViajeWindow.destroy()
     btnSendData = tk.Button(registerViajeWindow, text='Guardar Camion', command=SendData)
     btnSendData.place(x= 50, y = 80)

def Venderboletos():
     ventana = tk.Tk()
     ventana.title("Vendiendo")
     ventana.geometry("480x300")
     ventana.resizable(0, 0)
     listaViajes = tkinter.Listbox(ventana, width=40, height=10)
     listaViajes.delete(0, END)
     index = 0
     viajes = consultas.SelectViaje()
     for viaje in viajes:
          index += index
          print(viaje)
          listaViajes.insert(index, viaje[1]+' '+viaje[2]+' '+str(viaje[3])+' '+str(viaje[4]))
          #listaCamiones.insert(index, camion[0]+' '+str(camion[1])+' '+str(camion[2]))
     listaViajes.place(x=50, y=50)
     labelCliente = tk.Label(ventana, text='Nombre')
     labelCliente.place(x=300, y=50)
     ClienteBox = tk.Entry(ventana)
     ClienteBox.place(x=350, y=50)
     labeledad = tk.Label(ventana, text='Edad')
     labeledad.place(x=300, y=70)
     EdadBox = tk.Entry(ventana)
     EdadBox.place(x=350, y=70)
     def vender():
          for item in listaViajes.curselection():
               i = listaViajes.get(item)
          estados = i.split(' ')
          print(estados[0], estados[1])
          edad = EdadBox.get()
          nombre = ClienteBox.get()
          consultas.InsertCliente(nombre, edad)
          idc = str(consultas.get_Id_Cliente(nombre))
          c = idc[1]
          print(c)
          idv = str(consultas.get_Id_viaje(estados[0], estados[1]))
          v = idv[1:3]
          print(v)
          consultas.InsertInfoViaje(c, int(v))

     btnVender = tk.Button(ventana,text='Vender boleto', command = vender)
     btnVender.place(x=350, y = 200)
     ventana.mainloop()

def ActualizarDatos():
     ventanaDatos = tk.Tk()          
     ventanaDatos.title("Ingresando Datos")
     ventanaDatos.geometry("120x120")
     ventanaDatos.resizable(0,0)
     btnConductor = tk.Button(ventanaDatos, text='Conductor', command= IngresarConductor)
     btnCamion = tk.Button(ventanaDatos, text='Camion', command= IngresarCamion)
     btnConductor.place(x=30,y=40)
     btnCamion.place(x=30,y=80)

def Inicio():
     ventana = tk.Tk()
     ventana.title("Bienvenido a CEPBus")
     ventana. geometry("240x240")
     ventana.resizable(0,0)
     cabezera = tk.Label(ventana, text="Selecciona un modo").pack()
     btnActualizarDatos = tk.Button(ventana, text='Actualizar Datos', command= ActualizarDatos)
     btnActualizarDatos.place(x=50 ,y=150)     
     btnVenderBoletos = tk.Button(ventana, text="Programar viaje", command=GenerarViaje)     
     btnVenderBoletos.place(x=50, y=100)
     btnVenderBoletos = tk.Button(ventana, text="Vender Boletos", command=Venderboletos)     
     btnVenderBoletos.place(x=50, y=50)
     ventana.mainloop()

def generarViaje():
     Inicio()

if __name__ == '__main__':
     #GenerarViaje()
     Inicio()
     
