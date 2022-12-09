from pyravendb.store import document_store

store = document_store.DocumentStore(urls=["http://127.0.0.1:8080"], database="Test")
store.initialize()
#Crear un objeto
class Cliente(object):
   def __init__(self, name, key = None):
       self.name = name
       self.key = key

   def __repr__(self):
       return str(self.__dict__)

#Herencias de objetos
class Vehiculos(object):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.acelera = False
        self.frena = False
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

#Hereda de Vehiculos
class Moto(Vehiculos):
    def truquitos(self, truco):
        self.truco = truco
        if (self.truco):
            return "Voy haciendo willy pa"
        else:
            return "Te cagaste pa"


    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)

#Saca los datos
# miMoto.estado()

class Contacto(object):
    def __init__(self, numero):
        self.numero = numero

#Continente objetos dentro de objetos
class Alumno(object):
    def __init__(self, name, apellido, Contacto):
        self.name = name
        self.apellido = apellido
        self.contacto = Contacto


with store.open_session() as session:

    #Modificaciones del Objeto cliente.
    print("1. Crear   2.Editar   3.Borrar   4.Leer  5.Buscar por Nombre  6. Buscar Por iniciales")
    print("7. Guardar una moto (Herencias)  8.Guardar Alumno (Continente)"  )
    a = int(input("Que desea realizar? "))
    while a != 0:
        print(a)
        if a == 1:
            nmb = input("Inserte el nombre del cliente: ")
            cla = input("Inserte una clave para el cliente: ")
            # Guardar dentro del objeto
            cliente = Cliente(nmb, cla)
            session.store(cliente)
            session.save_changes()
        if a == 2:
            id = input("Inserte el ID del Cliente: ")
            # Actualizar por ID
            cliente = session.load("clientes/1-A")
            nmb = input("Inserte un nombre: ")
            cla = input("Inserte una clave: ")
            cliente.name = nmb
            cliente.key = cla
            session.store(cliente)
            session.save_changes()
        if a == 3:
            id = input("Inserte el ID: ")
            cliente = session.delete(id)
            session.save_changes()
        if a == 4:
            id = input("Inserte el ID: ")
            cliente = session.load(id)
            print("Nombre: ",cliente.name, "Clave: ", cliente.key)
        if a == 5:
            nmb = input("Inserte un nombre: ")
            query_result = list(session.query().where_equals("name", nmb))
            clientes = query_result
            print("Clientes encontrados: ", len(clientes))
            for i in range(len(clientes)):
                clientes = query_result[i]
                print("Numero: ", i + 1, "Nombre: ", clientes.name, "Clave: ", clientes.key)
            print("Clave con ese nombre: ", cliente.key)
        if a == 6:
            a = input("Inserte una inicial: ")
            query_result = list(session.query(object_type=Cliente).where_starts_with("name", a))
            # Se puede hacer lo mismo pero con la letra final
            #query_result = list(session.query(object_type=Cliente).where_ends_with("name", "t"))
            clientes = query_result
            print("Clientes encontrados: ", len(clientes))
            for i in range(len(clientes)):
                clientes = query_result[i]
                #print(clientes)
                print("Numero: ", i+1, "Nombre: ", clientes.name, "Clave: ", clientes.key)
        if a == 7:
            mar = input("Inserte una marca: ")
            mod = input("Inserte el modelo: ")
            # Creando instancia y pasando datos
            b = int(input("Pinta un willy?: (1. Si 2. No): "))
            if b == 1:
                miMoto = Moto(mar, mod)
                miMoto.acelerar()
                miMoto.truquitos(True)
                miMoto.estado()
                print(miMoto.truquitos(True))
                session.store(miMoto)
                session.save_changes()
            if b == 2:
                miMoto = Moto(mar, mod)
                miMoto.estado()
                print(miMoto.truquitos(False))
                session.store(miMoto)
                session.save_changes()
        if a == 8:
            nmb = input("Inserte un nombre: ")
            ape = input("Inserte apellido: ")
            num = input("Inserte su numero: ")
            # Guardar dentro del objeto
            b = Contacto(num)
            a= Alumno(nmb, ape, Contacto(num))
            #contacto = alumno.Contacto(num)
            session.store(a)
            session.save_changes()
        #Repite Bucle
        print("1. Crear   2.Editar   3.Borrar   4.Leer  5.Buscar por Nombre  6.Por iniciales")
        print("7. Guardar una moto (Herencias)  8.Guardar Alumno (Continente)")
        a = int(input("Que desea realizar? "))











