#gestionar inventario 
#submenu opición gestionar inventario
print ("Opciones:")
print ("1. Agregar combustible.")
print ("2. No deseoagregar combustible")
#agregar combustible 
opcion = int(input ("Ingrese la opción deseada: "))
if opcion == 1: 
    print ("Actualmente tiene 40 galones de REGULAR")
    print ("Actualmente tiene 40 galones de SUPER")
    print ("Actualmente tiene 40 galones de DIESEL")
    galre= int (input ("Ingrese la cantidad (en galones) que desea de Regular: "))
    cantidaddetanquere= 40+ galre
    if cantidaddetanquere <= 80: 
        print (cantidaddetanquere, "galones de gasolina REGULAR, ahora")
        galsup= int (input ("Ingrese la cantidad (en galones) que desea de SUPER: "))    
    else: 
        print ("Operación inválida, superó la capacidad máxima")
        galsup= int (input ("Ingrese la cantidad (en galones) que desea de SUPER: "))       
        canttanquesup= 40+ galsup
    if  galsup <= 40:   
        canttanquesup= 40+ galsup
        print ("La cantidad del tanque SUPER es: ", canttanquesup)
        gald= int (input ("Ingrese la cantidad (en galones) que desea de DIESEL: "))
    else: 
        print ("Operación inválida, superó la capacidad máxima de tanque SUPER")
        gald= int (input ("Ingrese la cantidad (en galones) que desea de DIESEL: "))

    if gald <= 40:   
        canttanqued= 40 + gald
        print ("La cantidad de este tanque ahora es: ", canttanqued, "galones")
    else: 
        print ("Operación inválida, superó la capacidad máxima de tanque DIESEL")
else: 
    print ("Vuelva pronto")
    