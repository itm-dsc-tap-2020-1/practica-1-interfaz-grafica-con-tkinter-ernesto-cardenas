import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
def funcion_acerca():
    mBox.showinfo("Acerca","Carlos Ernesto Cárdenas Hernández\nIng. Sistemas Computacionales\nCuarto Semestre\nInstituto Tecnológico de Morelia")
def impimir_per():
    if nombre.get()=="" or apellidop.get()=="" or apellidom.get()=="" or direccion.get()=="":
        nom.configure(foreground='red')
        apep.configure(foreground='red')
        apem.configure(foreground='red')
        dire.configure(foreground='red')
        colo.configure(foreground='red')
        ci.configure(foreground='red')
        muni.configure(foreground='red')
    else :
        nom.configure(foreground='green')
        apep.configure(foreground='green')
        apem.configure(foreground='green')
        dire.configure(foreground='green')
        colo.configure(foreground='green')
        ci.configure(foreground='green')
        muni.configure(foreground='green')
        ventaux1=tk.Tk()
        ventaux1.title("Datos personales")
        nomx=ttk.Label(ventaux1, text="Nombre: "+nombre.get())
        nomx.grid(column=0, row=0)
        apepx=ttk.Label(ventaux1, text="Apellido Paterno: "+apellidop.get())
        apepx.grid(column=0, row=1)
        apemx=ttk.Label(ventaux1, text="Apellido Materno: "+apellidom.get())
        apemx.grid(column=0, row=2)
        direx=ttk.Label(ventaux1, text="Dirección: "+direccion.get())
        direx.grid(column=0, row=3)
        colox=ttk.Label(ventaux1, text="Colonia: "+colonia.get())
        colox.grid(column=0, row=4)
        cix=ttk.Label(ventaux1, text="Ciudad: "+ciudad.get())
        cix.grid(column=0, row=5)
        munix=ttk.Label(ventaux1, text="Municipio: "+ciudad.get())
        munix.grid(column=0, row=6)
def impimir_ex():
    if opcion_2.get()==0 or caja.get('1.0', 'end-1c')=="":
        obj.configure(foreground='red')
        estado.configure(foreground='red')
    else:
        obj.configure(foreground='green')
        estado.configure(foreground='green')
        ventaux2=tk.Tk()
        ventaux2.title("Datos extras")
        pasat=""
        if opcion_1a.get()==1:
            pasat+="Futbol"
        if opcion_2a.get()==1:
            if pasat=="": pasat+="Leer"
            else: pasat+=" - Leer"
        if opcion_3a.get()==1:     
            if pasat=="": pasat+="Correr"
            else: pasat+=" - Correr"
        if opcion_4a.get()==1:     
            if pasat=="": pasat+="Bailar"
            else: pasat+=" - Bailar"    
        if opcion_5a.get()==1:     
            if pasat=="": pasat+="Cantar"
            else: pasat+=" - Cantar"
        if pasat!="":
            pasax=ttk.Label(ventaux2, text="Pasatiempos: "+pasat)
            pasax.grid(column=0, row=0)
            estat=""
            if opcion_2.get()==1:
                estat="Soltero"
            if opcion_2.get()==2:
                estat="Viudo"
            if opcion_2.get()==3:
                estat="Casado"
            estadox=ttk.Label(ventaux2, text="Estado civil: "+estat)
            estadox.grid(column=0, row=1)
            objx=ttk.Label(ventaux2, text="Objetivo en la vida: "+caja.get('1.0', 'end-1c'))
            objx.grid(column=0, row=2) 
        else:
            estat=""
            if opcion_2.get()==1:
                estat="Soltero"
            if opcion_2.get()==2:
                estat="Viudo"
            if opcion_2.get()==3:
                estat="Casado"
            estadox=ttk.Label(ventaux2, text="Estado civil: "+estat)
            estadox.grid(column=0, row=1)
            objx=ttk.Label(ventaux2, text="Objetivo en la vida: "+caja.get('1.0', 'end-1c'))
            objx.grid(column=0, row=2)     
def imprimir_ge():
    if nombre.get()=="" or apellidop.get()=="" or apellidom.get()=="" or direccion.get()=="" or opcion_2.get()==0 or caja.get('1.0', 'end-1c')=="":
        mBox.showerror('Faltante', 'Hacen falta datos en alguna pestaña')
    else:
        ventaux3=tk.Tk()
        ventaux3.title("Datos en general")
        nomx=ttk.Label(ventaux3, text="Nombre: "+nombre.get())
        nomx.grid(column=0, row=0)
        apepx=ttk.Label(ventaux3, text="Apellido Paterno: "+apellidop.get())
        apepx.grid(column=0, row=1)
        apemx=ttk.Label(ventaux3, text="Apellido Materno: "+apellidom.get())
        apemx.grid(column=0, row=2)
        direx=ttk.Label(ventaux3, text="Dirección: "+direccion.get())
        direx.grid(column=0, row=3)
        colox=ttk.Label(ventaux3, text="Colonia: "+colonia.get())
        colox.grid(column=0, row=4)
        cix=ttk.Label(ventaux3, text="Ciudad: "+ciudad.get())
        cix.grid(column=0, row=5)
        munix=ttk.Label(ventaux3, text="Municipio: "+ciudad.get())
        munix.grid(column=0, row=6)
        pasat2=""
        if opcion_1a.get()==1:
            pasat2+="Futbol"
        if opcion_2a.get()==1:
            if pasat2=="": pasat2+="Leer"
            else: pasat2+=" - Leer"
        if opcion_3a.get()==1:     
            if pasat2=="": pasat2+="Correr"
            else: pasat2+=" - Correr"
        if opcion_4a.get()==1:     
            if pasat2=="": pasat2+="Bailar"
            else: pasat2+=" - Bailar"    
        if opcion_5a.get()==1:     
            if pasat2=="": pasat2+="Cantar"
            else: pasat2+=" - Cantar"
        if pasat2!="":
            pasax=ttk.Label(ventaux3, text="Pasatiempos: "+pasat2)
            pasax.grid(column=0, row=7)
            estat2=""
            if opcion_2.get()==1:
                estat2="Soltero"
            if opcion_2.get()==2:
                estat2="Viudo"
            if opcion_2.get()==3:
                estat2="Casado"
            estadox=ttk.Label(ventaux3, text="Estado civil: "+estat2)
            estadox.grid(column=0, row=8)
            objx=ttk.Label(ventaux3, text="Objetivo en la vida: "+caja.get('1.0', 'end-1c'))
            objx.grid(column=0, row=9) 
        else:
            estat2=""
            if opcion_2.get()==1:
                estat2="Soltero"
            if opcion_2.get()==2:
                estat2="Viudo"
            if opcion_2.get()==3:
                estat2="Casado"
            estadox=ttk.Label(ventaux3, text="Estado civil: "+estat)
            estadox.grid(column=0, row=6)
            objx=ttk.Label(ventaux3, text="Objetivo en la vida: "+caja.get('1.0', 'end-1c'))
            objx.grid(column=0, row=7)                  

ventana=tk.Tk()
ventana.title("Sistema Escolar")


barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir", command=imprimir_ge)
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir", command=funcion_salir)
opciones_menu.add_separator()
barra_menu.add_cascade(label="Sistema", menu=opciones_menu)
menu_ayuda=Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=funcion_acerca)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text='Datos Personales')
tabControl.pack(expand=1, fill="both")
nom=ttk.Label(tab1, text="Nombre: ")
nom.grid(column=0, row=0)
nombre=tk.StringVar()
nombreCapturado=ttk.Entry(tab1, width=12, textvariable=nombre)
nombreCapturado.grid(column=2, row=0)
apep=ttk.Label(tab1, text="Apellido Paterno: ")
apep.grid(column=0, row=1)
apellidop=tk.StringVar()
apellidoCapturado=ttk.Entry(tab1, width=12, textvariable=apellidop)
apellidoCapturado.grid(column=2, row=1)
apem=ttk.Label(tab1, text="Apellido Materno: ")
apem.grid(column=0, row=2)
apellidom=tk.StringVar()
apellidomCapturado=ttk.Entry(tab1, width=12, textvariable=apellidom)
apellidomCapturado.grid(column=2, row=2)
dire=ttk.Label(tab1, text="Dirección: ")
dire.grid(column=0, row=3)
direccion=tk.StringVar()
direccionCapturado=ttk.Entry(tab1, width=12, textvariable=direccion)
direccionCapturado.grid(column=2, row=3)
colo=ttk.Label(tab1, text="Colonia: ")
colo.grid(column=0, row=4)
colonia=tk.StringVar()
coloniaSeleccionado=ttk.Combobox(tab1, width=12, textvariable=colonia)
coloniaSeleccionado['values']=("Indeco", "Realito", "Villas del Sol", "Villas de la loma", "López Mateos")
coloniaSeleccionado.grid(column=2, row=4)
coloniaSeleccionado.current(0)
ci=ttk.Label(tab1, text="Ciudad: ")
ci.grid(column=0, row=5)
ciudad=tk.StringVar()
ciudadSeleccionado=ttk.Combobox(tab1, width=12, textvariable=ciudad)
ciudadSeleccionado['values']=("Morelia", "CDMX", "Monterrey", "Durango", "Vice city")
ciudadSeleccionado.grid(column=2, row=5)
ciudadSeleccionado.current(0)
muni=ttk.Label(tab1, text="Municipio: ")
muni.grid(column=0, row=6)
municipio=tk.StringVar()
municipioSeleccionado=ttk.Combobox(tab1, width=12, textvariable=municipio)
municipioSeleccionado['values']=("Morelia", "Patzcuaro", "Tarimbaro", "Municipio chiquito", "Municipio grande")
municipioSeleccionado.grid(column=2, row=6)
municipioSeleccionado.current(0)
impriper=ttk.Button(tab1, text="Imprimir datos personales", command=impimir_per)
impriper.grid(column=2, row=8)


tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text='Datos Extras')
opcion_1a=tk.IntVar()
casilla_1a=tk.Checkbutton(tab2, text="Futbol", variable=opcion_1a)
casilla_1a.deselect()
casilla_1a.grid(column=0, row=1, sticky=tk.W)
opcion_2a=tk.IntVar()
casilla_2a=tk.Checkbutton(tab2, text="Leer", variable=opcion_2a)
casilla_2a.deselect()
casilla_2a.grid(column=1, row=1, sticky=tk.W)
opcion_3a=tk.IntVar()
casilla_3a=tk.Checkbutton(tab2, text="Correr", variable=opcion_3a)
casilla_3a.deselect()
casilla_3a.grid(column=2, row=1, sticky=tk.W)
opcion_4a=tk.IntVar()
casilla_4a=tk.Checkbutton(tab2, text="Bailar", variable=opcion_4a)
casilla_4a.deselect()
casilla_4a.grid(column=3, row=1, sticky=tk.W)
opcion_5a=tk.IntVar()
casilla_5a=tk.Checkbutton(tab2, text="Cantar", variable=opcion_5a)
casilla_5a.deselect()
casilla_5a.grid(column=4, row=1, sticky=tk.W)
pasa=ttk.Label(tab2, text="Pasatiempos:")
pasa.grid(column=0, row=0)
estado=ttk.Label(tab2, text="Estado civil")
estado.grid(column=0, row=3)   
opcion_2=tk.IntVar()
radio1=tk.Radiobutton(tab2, text="Soltero", variable=opcion_2, value=1)
radio1.grid(column=0, row=4, sticky=tk.W)
radio2=tk.Radiobutton(tab2, text="Viudo", variable=opcion_2, value=2)
radio2.grid(column=1, row=4, sticky=tk.W)
radio3=tk.Radiobutton(tab2, text="Casado", variable=opcion_2, value=3)
radio3.grid(column=2, row=4, sticky=tk.W)
obj=ttk.Label(tab2, text="Objetivo en la vida:")
obj.grid(column=0, row=5)
scroll_ancho=30
scroll_alto=3
caja=scrolledtext.ScrolledText(tab2, width=scroll_ancho, height=scroll_alto, wrap=tk.WORD)
caja.grid(column=1, row=5, columnspan=3)
impriex=ttk.Button(tab2, text="Imprimir datos extras", command=impimir_ex)
impriex.grid(column=2, row=7)

ventana.mainloop()