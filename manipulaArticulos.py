import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql


def muestra():
    #recupera Artículos
    def recupera_articulos():
        #se crea un objeto de coneccion a la BD
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='Ferretería')
        #se crea un cursos para ejecutar la consulta sobre la tabla de categoría
        cursor = conn.cursor()
        # se utiliza el cursor para ejecutar la consulta sobre la tabla categoría
        cursor.execute('select claveArticulo, descripcion, costo, precioMayoreo, precioMenudeo, existenciaAlmacen, existenciaPisoVenta from articulo')
        #se crea una lista para contener las categorías extraidas en la base de datos
        articulos = cursor.fetchall()
        print(articulos)
        conn.close()
        return articulos
    
    def recupera_tipos():
        #se crea un objeto de coneccion a la BD
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='Ferretería')
        #se crea un cursor para ejecutar consultas a la base de datos
        cursor = conn.cursor()
        cursor.execute('select descripcion from tipoArticulo')
        tipos = cursor.fetchall()
        print(tipos)
        conn.close()
        return tipos
    
    #                                                    def recupera_unidades():
    def recupera_Unidades():
        # se crea un objeto de conexión a la BD
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='Ferretería')
        # se crea un cursor para ejecutar consultas a la base de datos
        cursor = conn.cursor()
        cursor.execute('select descripcion from tipounidad')  
        unidades = cursor.fetchall()  
        print(unidades)
        conn.close()
        return unidades


    def recCveTipoArticulo():
        print(selTipos.get())


    def alta_articulos():
        #se crea un objeto de coneccion a la BD
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='Ferretería')
        #se crea un cursor para ejecutar consultas a la base de datos
        cursor = conn.cursor()
        #se utiliza el cursor para ejecutar la consulta sobre la tabla de categorías
        cursor.execute('select claveTipoArticulo from tipoArticulo where descripcion=%s', selTipos.get())
        tipo = cursor.fetchone()
        cursor.execute('select claveTipoUnidad from tipounidad where descripcion=%s', selUnidades.get())
        unidad = cursor.fetchone()
        print(des.get(), cos.get(), may.get(), men.get(), alm.get(), piso.get(), tipo[0], unidad[0] )
        cursor.execute('INSERT INTO articulo (claveArticulo, descripcion, costo, precioMayoreo, precioMenudeo, existenciaAlmacen, claveTipoArticulo, claveTipoUnidad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(des.get(), cos.get(), may.get(), men.get(), alm.get(), piso.get(), tipo, unidad))
        conn.commit()
        #se crea una lista para contener las categorías extraidas de la base de datos
        #articulos = cursor.fetchall()
        #print(articulos)
        conn.close()
        listaArticulos()

    def modifica_articulo():
        global keySelect
        #se crea un objeto de coneccion a la BD
        conn = pymysql.conect(host='localhost', user='root', passwd='', db='Ferretería')
        #se crea un cursor para ejecutar consultas a la BD
        cursor = conn.cursor()
        #se utiliza el cursor para ejecutar la consulta sobre la tabla de categoría
        cursor.execute('select claveTipoArticulo from tipoArticulo where descripcion=%s', selTipos.get())
        tipo = cursor.fetchone()
        cursor.execute('select claveTipoUnidad from tipoUnidad where descripcion=%s', selUnidades.get())
        unidad = cursor.fetchone()
        print(des.get(), cos.get(), may.get(), men.get(), alm.get(), piso.get(), tipo[0], unidad[0])
        cursor.execute('update articulo set descripcion=%s, costo=%s, precioMayoreo=%s, precioMenudeo=%s, existenciaAlmacen=%s, existenciaPisoVenta=%s, claveTipoArticulo=%s, claveTipoUnidad=%s where claveArticulo', (des.get(), cos.get(), may.get(), men.get(), alm.get(), piso.get(), tipo, unidad, keySelect))
        conn.comnit()
        #se crea una lista para contener las categorias extraidas de la base de datos
        #articulos = cursor.fetchall()
        #print(articulos)
        conn.close()
        listaArticulos()


    #función para manejar el evento de selección en el Treeview
    def mostrar_indice_seleccionado():
        global tree
        global keySelect
        seleccion = tree.selection() #obtiene los identificadores de los elementos seleccionados
        if seleccion:
            indice = tree.index(seleccion[0]) # obtiene el índice del primer elemento seleccionado
            print ("Elemento seleccionado en el índice:", indice)
            item = tree.item(seleccion[0]) #obtiene el diccionario de valores del primer elemento seleccionado
            valores = item ['values']
            valores = item ['values']
            print(valores)
#################################################################################################################################
            conn = pymysql.connect(host='localhost', user='root', passwd='', db='Ferretería')
            # se crea un cursor para ejecutar consultas a la BD
            des.delete(0, tk.END)  # Borra el contenido actual del Entry
            cos.delete(0, tk.END)
            may.delete(0, tk.END)
            men.delete(0, tk.END)
            alm.delete(0, tk.END)
            piso.delete(0, tk.END)
            selTipos.delete(0, tk.END)
            selUnidades.delete(0, tk.END)

            des.insert(0, valores[1])  # Inserta el nuevo valor en el Entry
            cos.insert(0, valores[2])
            may.insert(0, valores[3])
            men.insert(0, valores[4])
            alm.insert(0, valores[5])
            piso.insert(0, valores[6])
            selTipos.insert(0, valores[7])
            selUnidades.insert(0, valores[8])
            keySelect = valores[0]
            winArt.update()
            print(valores)
        else:
            print("Ningún elemento seleccionado")


    def borrar_treeview(tree):
        # elimina todos los elementos dentro del Treeview
        for item in tree.get_children():
            tree.delete(item)


    def listaArticulos():
        global tree
        filas = recupera_articulos()
        #limpiar el treeview
        tree.delete(*tree.get_children())
        #configurar los encabezados de las columnas
        for encabezado in encabezados:
            tree.heading(encabezado, text=encabezado)
            if encabezado == 'descripcion':
                tree.column(encabezado, width=100) #ajustar el ancho de las columnas según sea necesario
            else:
                tree.column(encabezado, width=100) #ajustar el ancho de las columnas según sea necesario

        #insertar los datos en el treeview
        for fila in filas:
            tree.insert("", "end", values=fila)

        #colocar el treeview en la ventana
        tree.pack(padx=10, pady=10)
        #configurar la función para manejar el evento de selección
        tree.bind("<<TreeviewSelect>>", lambda event: mostrar_indice_seleccionado())

    #main del procedimiento
    global tree 
    keySelect = -1
    winArt = tk.Tk()
    winArt.resizable(1,1)
    winArt.geometry("1200x700")
    winArt.config(bg="green")
    winArt.title("Artículos")
    strDescripcion = StringVar()
    strCosto = StringVar()
    strMayoreo = StringVar()
    strMenudeo = StringVar()
    strAlmacen = StringVar()
    strPisoVenta = StringVar()
    strTipoArticulo = StringVar()
    strUnidad = StringVar()

    #crea un frame para contener el treeview y la barra de desplazamiento
    frame = tk.Frame(winArt, width=100, height=500, bg="orange")
    frame.pack()

    #crear una conexión a la BD
    encabezados = ('clave', 'descripcion', 'Mayoreo', 'Menudeo', 'Almacén', 'PisoVenta', 'TipoArticulo', 'Unidad' )
    tree = ttk.Treeview(frame, columns=encabezados, show="headings")

    listaArticulos()

    alta = Button(winArt, text="      Alta     ", command=alta_articulos, font='helvetica 14 bold', bg="white")
    alta.place(x=300, y=250)
    modifica = Button(winArt, text="   Modificación   ", command=modifica_articulo, font='helvetica 14 bold', bg="white")
    modifica.place(x=500, y=250)
    baja = Button(winArt, text="     Baja     ", command=recCveTipoArticulo, font='helvetica 14 bold', bg="white")
    baja.place(x=700, y=250)
    #definir entrada para la respuesta 

    etiDes=Label(winArt, bg='light sky blue', text="Descripción", font='helvetica 18 bold')
    etiDes.place(x=10, y=300)
    strDescripcion.set("")
    des=Entry(winArt, textvariable=strDescripcion, font='helvetica 18 bold', bg='white', width=70)
    des.place(x=170, y=300)

    etiCosto=Label(winArt, bg='light sky blue', text="Costo", font='helvetica 18 bold')
    etiCosto.place(x=10, y=340)
    strCosto.set("0")
    cos=Entry(winArt, textvariable=strCosto, font='helvetica 18 bold', bg='white', width=10)
    cos.place(x=170, y=340)

    etiMayoreo=Label(winArt, bg='ligth sky blue', text="Mayoreo", font='helvetica 18 bold')
    etiMayoreo.place(x=420, y=340)
    strMayoreo.set("0")
    may=Entry(winArt, textvariable=strMayoreo, font='helvetica 18 bold', bg='white', width=10)
    may.place(x=530, y=340)

    etiMenudeo=Label(winArt, bg='black', text="Menudeo", font='helvetica 18 bold')
    etiMenudeo.place(x=720, y=340)
    strMenudeo.set("0")
    men=Entry(winArt,textvariable=strMenudeo, font='helvetica 18 bold', bg='white', width=10)
    men.place(x=840, y=340)

    etiAlmacen=Label(winArt, bg='black', text="Almacen", font='helvetica 18 bold')
    etiAlmacen.place(x=10, y=380)
    strAlmacen.set("0")
    alm=Entry(winArt, textvariable=strAlmacen, font='helvetica 18 bold', bg='white', width=10)
    alm.place(x=170, y=380)

    etiPiso=Label(winArt, bg='black', text="Piso", font='helvetica 18 bold')
    etiPiso.place(x=420, y=380)
    strPisoVenta.set("0")
    piso=Entry(winArt, textvariable=strPisoVenta, font='helvetica 18 bold', bg='white', width=10)
    piso.place(x=530, y=380)


    #recupera tipo artículo
    tipos=recupera_tipos()
    print(tipos)
    #definir entrada para tipo de unidad
    eti=Label(winArt, text="Tipo de Artículo", font='helvetica 18 bold', bg='black')
    eti.place(x=10, y=420)
    selTipos=ttk.Combobox(winArt, font='helvetica 18 bold')
    selTipos['values']=tipos
    selTipos.place(x=200, y=420)
    #selTipos.bind("<<ComboboxSelected>>", recCveTipoArticulo)
    #recupera tipo unidad
    unidades=recupera_Unidades()
    print(unidades)
    #definir entrada para tipo de unidad
    etiUnidades=Label(winArt,text="Tipo de Unidad", font='helvetica 18 bold', bg='black')
    etiUnidades.place(x=10, y=460)
    selUnidades=ttk.Combobox(winArt, font='helvetica 18 bold')
    selUnidades['values']=unidades
    selUnidades.place(x=200, y=460)
    #selTipos.bind("<<ComboboxSelected>>", preguntas)
    winArt.mainloop()
        

