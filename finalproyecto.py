from tkinter import Entry, Label, Tk, ttk, Text
from tkinter import *


test=Tk()

test.title("Eso tilin")
test.geometry("500x500")

ubicacion=StringVar()  #El string Var sirve para obtener los datos

marca1=Label(test, text="Escribe aqui el archivo")
marca1.place(x=10,y=10)
direccion=Entry(test, textvariable=ubicacion)#text variable es para capturar la informacion
direccion.place(x=170,y=10)
test.resizable(1,1)
marca10=Label(test, text="Todas las diagonales a la derecha /")
marca10.place(x=300,y=10)

cuadrito=Text(test, width=50, height=50)
cuadrito.place(x=50,y=200)
#cuadrito.insert(INSERT,"Holis")

#impresión de datos personales

def meusdados():
    class meunome:
        def __init__(self, name, email, carnet):
            self.name = name
            self.email = email
            self.carnet = carnet

    customer = meunome("Fernando Omar Lopez Morales", "flopezm23@gmail.com", "7690-21-20755")

    marca3=Label(test,text=customer.name)
    marca3.place(x=10,y=30)
    marca4=Label(test,text=customer.email)
    marca4.place(x=10,y=50)
    marca5=Label(test,text=customer.carnet)
    marca5.place(x=10,y=70)

    #lugardearchivo=ubicacion.get()
    

def mostrar():#parte del 26-10-2021 
    lugardearchivo=ubicacion.get()            #esta seccion es para agarrar el dato de la primer barra de entrada e imprimirlo en el cuadro de texto
    lecturamuestra=StringVar()
    lecturamuestra.set(lugardearchivo)
        #lectura=Entry(test, textvariable=lecturamuestra)
        #lectura.place(x=20,y=300)
    gente=str
    gente=lecturamuestra.get()

        #capturar informacion de un archivo
    arquivo='C:/Users/Elder/Desktop/examenes Universidad 2/examen algoritmos/Proyecto final/pruebasfinal.txt'
    
    #cambie arquivo por gente para probar
        
    dados=[]
    with open(gente) as fname:
        lineas=fname.readlines()
        for linea in lineas:
            dados.append(linea.strip("\n"))
        #print (dados)

        #cuadrito.insert(INSERT,gente)
    cuadrito.insert(INSERT,dados)
        
        #para capturar los valores del cuadro de texto
    def salvar():
        captura=str
        captura=cuadrito.get(1.0,"end-1c") #para capturar cuadro de texto
        print(captura)
            

            #para escrever novamente no arquivo
            #esto sirve para escribir una lista en un archivo
        #Cambie arquivo por gente para probar
        with open(gente, 'w') as bro:
            for tudo in captura:
                bro.write('%s'%tudo)
 
    ttk.Button(test, text='Guardar', command=salvar).place(x=50,y=150)
def limpa():
    cuadrito.delete("1.0","end") #este comando sirve para borrar los datos

ttk.Button(test, text='Ver', command=mostrar).place(x=240,y=100)
    

ttk.Button(test, text='Datos', command=meusdados).place(x=50,y=100)
ttk.Button(test, text='Cerrar', command=quit).place(x=240,y=150)
ttk.Button(test, text='Limpiar', command=limpa).place(x=140,y=150)

test.mainloop()
