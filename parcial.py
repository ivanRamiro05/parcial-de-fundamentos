from tkinter import*
import random
#Funciones
def salir():
    ventana.destroy()

def buscar():

   print("") 
def graficar():
    for i in range(N):
        matriz=c.create_rectangle(10,10, Base-10, 10 ,Base-10, ALTURA-10, 10,ALTURA-10 )

Base=1000
ALTURA=500
ventana =Tk()


ventana.title("Parcial de Fundamentos")

ventana.config(bg ="green")

ventana.resizable(0,0)

ventana.geometry("1000x500")

matriz = StringVar()
   
matriz_label = Label(text="Matriz cuadrada", bg="blue")
matriz_label.place(x=22, y=35)

matriz_entry= Entry(textvariable=matriz, width="40")

matriz_entry.place(x=22, y=70)

boton =Button(ventana(text= "graficar", COMMAND = graficar()))
boton.place(x=22 , y = 110)
#numero de columnas y filas que tenga la matriz
c = Canvas(principal , width=base , height=altura)
c.place(x=10 , y=10)

u=0
uu=600/n
p=0
pp=600/n

x=20+uu/2
y=20+uu/2

for i in (0,n+1):
    while u<600:
        texto = c.create_text(x+u,y+p, anchor="center", text=random.randint(0, 9), font=("Arial","30", "bold"), fill="blue",activefill="red")
        u=u+uu
    p=p+pp
ventana.mainloop()