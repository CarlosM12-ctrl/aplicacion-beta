from tkinter import *
from random import randint
import tkinter
#import pruebas as c

class consul(tkinter.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state('zoomed')
        self.resizable(1,1)
        #self.isbn= IntVar()
        #self.autor = StringVar()
        #self.editorial = StringVar()
        #self.titu =  StringVar()
        self.dibujarComponentes()
    
    def dibujarComponentes(self):
        Button(self, bg="red", text="Hola mundo", font=('nunito', 25, 'normal')).place(x=100, y=100)

    

class Interfaz():
    
    #def de arranque
    def __init__(self,ventana):
       
        self.ventana = ventana
        ventana.state('zoomed')
        self.ventana.resizable(1,1)
        
        self.dibujarComponentes()
    
    def dibujarComponentes(self):
        #canvas = Canvas(width=400, height=300, border=0, bg='white')
        #canvas.pack(expand=YES, fill=BOTH)
        #canvas.create_rectangle(0, 0, 750, 700, width=5, fill='#2E276C')
        
        self.ventana.config(background="white")

        self.ventana.title("Biblioteca CBTa195" )
       
      
        #self.ventana.iconbitmap("")
        
        #labels y entrys 
        
        Label(self.ventana, bg="#2E276C" ).place(x=0, y=0, width=750, height=700)
        
        Label(self.ventana,text="Bienvenidx", bg="white", font=('Nunito', 40, "normal") ).place(x=880, y=30)
        Button(self.ventana,text="Solicitar Libro",bg="white",  border=0,font=('Nunito', 40, "normal") ).place(x=850,y=130)
        Button(self.ventana,text="Buscar Libro",bg="white", command=self.nv, border=0, font=('Nunito', 40, "normal") ).place(x=850,y=300)
        Button(self.ventana,text="Información",bg="white",  border=0, font=('Nunito', 40, "normal") ).place(x=850,y=480)
        Button(self.ventana,text="Información",bg="white",  border=0, font=('Nunito', 40, "normal") ).place(x=850,y=480)
        
        #Text(self.ventana,text="Información",bg="white",  border=0, font=('Nunito', 40, "normal")).place(x=100,y=480)
      
        #img = PhotoImage(file="log.png")
       # self.image = PhotoImage(file="log.png")
       # lbl_img = Label(self.ventana, image=img).place(x=10, y=100)
        #self.image = self.image.subsample(3)
        #Label(self.ventana, bg="#2E276C", image=self.image).place(x=150, y=50)
    def nv(self):
        self.nventana: consul()


  
        
        

  


obj = Interfaz(Tk())
obj.ventana.mainloop()