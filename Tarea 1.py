import os
class nodo:
    def __init__ (self,nombre,apellido,carnet):
        self.nombre=nombre
        self.apellido=apellido
        self.carnet=carnet
class lista:
    def __init__(self):
        self.inicio=None
    def agregar (self,nombre,apellido,carnet):
        nuevo_nodo=nodo(nombre,apellido,carnet)
        nuevo_nodo.siguiente=self.inicio
        self.inicio=nuevo_nodo
    def listar(self):
        temp=self.inicio
        while temp!=None:
            print(">. "+temp.nombre+" "+temp.apellido+" \nCarnet: "+temp.carnet)
            temp=temp.siguiente
        def borrar_todo(self):
            self.inicio=None
objetoNodo=lista()
class MenuTarea:
    @staticmethod
    def menu_principal():
        """
        muestra el menu principal
        """
        print("Bienvenido a la tarea No 1")
        print("----------------------------------------------------------")
        print("Por favor seleccione que desea hacer:")
        print("----------------------------------------------------------")
        print("1) Insertar al principio")
        print("2) Insertar al final")
        print("3) Eliminar por valor")
        print("4) Mostrar lista")
        print("5) Salir")

    @staticmethod
    def pausar():
        """
        Pausa entre acciones
        """
        input("\nPresiona enter para continuar...")
    @staticmethod
    def opcion1():
        """
        Insertar al principio
        """
        os.system('cls')
        print("Ingrese el Nombre")
        nombre=input()
        print("Ingrese el Apellido")
        apellido=input()
        print("Ingrese el Carnet")
        carnet=input()
        objetoNodo.agregar(nombre=nombre,apellido=apellido,carnet=carnet)
    @staticmethod
    def opcion2():
        """
        Insertar al final
        """
        os.system('cls')
        objetoNodo.agregar(nombre=input(),apellido=input(),carnet=input())
    @staticmethod
    def opcion3():
        """
        Eliminar por valor
        """
        os.system('cls')
        print("esta es la opcion 3")
    @staticmethod
    def opcion4():
        """
        Mostrar lista
        """
        os.system('cls')
        objetoNodo.listar()
        print(objetoNodo.inicio.nombre)
    @staticmethod
    def opcion5():
        """
        Opcion 5
        """
        os.system('cls')
        print("esta es la opcion 5")
        exit()
    @staticmethod
    def menu():
        """
        Seleccion de Menu
        """
        while True:
            MenuTarea.menu_principal()
            seleccion = input("Seleccione una opcion (1-5): ")
            if seleccion == '1':
                MenuTarea.opcion1()
            elif seleccion == '2':
                MenuTarea.opcion2()
            elif seleccion=='3':
                MenuTarea.opcion3()
            elif seleccion == '4':
                MenuTarea.opcion4()
            elif seleccion == '5':
                MenuTarea.opcion5()
            else:
                os.system('cls')
                print("Por favor seleccione una opcion valida.")
            MenuTarea.pausar()
            os.system('cls')
if __name__ == "__main__":
    MenuTarea.menu()
