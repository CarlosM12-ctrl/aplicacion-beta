import mysql.connector
from mysql.connector import errorcode

class Conexion:
    def conectar (self):
        try:
            self.conexion = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='cbta')
            print("conectado a la base de datos ʕ•́ᴥ•̀ʔっ")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error De Usuario Y Contraseña (ง︡'-'︠)ง")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de datos no existe ( ˘︹˘ )") 
            else:
                print(err)
    
    def desconectar(self):
        print("CERRANDO SESIÓN... 👋≧◉ᴥ◉≦")
        self.conexion.close()
        print("SESIÓN CERRADA CON ÉXITO")
    def insertar(self, isbn, autor, editorial, titulo, categoria):
        self.conectar()
        cursor= self.conexion.cursor()
        cursor.execute("INSERT INTO busca VALUES (null, "+str(isbn)+", '"+autor+"', '"+editorial+"', '"+titulo+"', '"+categoria+"'  ) ")
        self.conexion.commit()
        self.desconectar()
    
    def consultar (self):
        self.conectar()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT isbn, autor, editorial, titulo, categoria FROM busca;")
        resultado = cursor.fetchall()
        self.desconectar()
        return resultado


    def buscar(self,cat):
        self.conectar()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT isbn, autor, editorial, titulo, categoria FROM busca WHERE categoria LIKE '%"+cat+"%';" )
        resultado = cursor.fetchall()
        self.desconectar()
        return resultado

    def buscar1(self, isbn):
        self.conectar()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT isbn, autor, editorial, titulo, categoria FROM busca WHERE titulo LIKE '%"+isbn+"%';" )
        resultado = cursor.fetchall()
        self.desconectar()
        return resultado  
