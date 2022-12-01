ventana =Tk()


ventana.title("Parcial de Fundamentos")

ventana.config(bg ="green")

ventana.resizable(0,0)

ventana.geometry("1000x500")

frame_de_graficador=Frame(ventana)

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