class Menu:
    def__init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self .opciones:
            print(opcion)
            opc=input("Elija opcion[1...{}]:".formt(len(self.opciones)))
            return opc
        
    men = Menu ("Menu Principal",["1) Calculadora","2) Numeros ","3) Listas","4) Cadenas","5)
    opc = men.menu()
    if opc == "1":
       men1= Menu("Menu Calculadora",["1) Suma","2) Resta","3)Multiplicacion","4) Division"])
       opc1 = men1.menu()
       
       
    elif opc == "2":
             men2 = Menu("Menu Numeros",["1) Perfecto",2") Primo","3) Salir"])
             opc2 = men2.menu()
             
             if opc1 == "1":
             print("Suma de dos numeros")
             n1 = int(input("Ingrese numero1:  "))
             n2 = int(input("Ingrese numero2:  "))
             print(n1+n1)
             
             if opc1 == "2"
             print("Resta de dos numeros")
             
             if opc1 == "3":
             print("Multiplicacion de dos numeros")
             n1 = int(input("Ingrese numero1: "))
             n2 =int(input("Ingrese numero2:  "))
             print(n1*n2)
             
             
             if opc2 == "1":
               print("Numeros Perfectos")
               num= int(input("Ingrese Numeros:  "))
               # llamar el metodo perfecto
               print("El numero es perfecto")
            elif opc == "3":
                    print("Listas")
                    
            elif opc == "4":
                     print("Cadenas")
                     