#trabajadores iniciales
jordiurna = 1
jorvespertina = 1
jornocturna = 1

#se mostrará el total de trabajadores para evaluar si se añade o retira algún trabajador
print ("Hay un total de:", jordiurna, "en el turno diurno")
print ("Hay un total de:", jorvespertina, "en el turno vespertino")
print ("Hay un total de:", jornocturna, "en el turno nocturna")
print ("¿Desea agregar o extraer personas a la estación de servicio")
print ("1.Agregar")
print ("2.Extraer")
print ("3.Ninguna")

seleccion = int(input("Seleccione la opción que desea: "))

#AGREGAR PERSONAL
while seleccion == 1:
            print("1.Jornada diurna")
            print("12:00 a.m. - 8:00 a.m.")
            print("Q14.00 quetzales por hora")
            print("2.Jornada vespertina")
            print ("8:00 a.m. - 4:00 p.m.")
            print ("Q14.50 quetzales por hora")
            print("3.Jornada nocturna")
            print ("4:00 p.m. - 12 a.m.")
            print ("Q15.50 quetzales por hora")
            segseleccion = int(input("Seleccione la jornada en la que desea agregar personal: "))
            if segseleccion == 1:
                agd = int(input("Ingrese la cantidad de personas a agregar: "))
                totald = (agd) + (jordiurna)
                print ("La cantidad de trabajadores para esta jornada es de: ", totald)
            if segseleccion == 2:
                agv = int(input("Ingrese la cantidad de personas a agregar: "))
                totalv = (agv) + (jorvespertina)
                print ("La cantidad de trabajadores para esta jornada es de: ", totalv)
            if segseleccion == 3:
                agn= int(input("Ingrese la cantidad de personas a agregar: "))
                totaln = (agn) + (jornocturna)
                print ("La cantidad de trabajadores para esta jornada es de: ", totaln)
            break
        #EXTRAER PERSONAL
while seleccion == 2:
            print("1.Jornada diurna")
            print("12:00 a.m. - 8:00 a.m.")
            print("Q14.00 quetzales por hora")
            print("2.Jornada vespertina")
            print ("8:00 a.m. - 4:00 p.m.")
            print ("Q14.50 quetzales por hora")
            print("3.Jornada nocturna")
            print ("4:00 p.m. - 12 a.m.")
            print ("Q15.50 quetzales por hora")
            segseleccion = int(input("Ingrese la jornada en la que desea extraer personal: "))
            if segseleccion == 1:
                exd = int(input("Ingrese la cantidad de personas a extraer: "))
                totald = (exd) - (jordiurna)
                if totald < 1:
                    print("No se puede realizar la siguiente acción, debe haber mínimo un trabajador en este turno")
                else:
                    print ("La cantidad de trabajadores para esta jornada es de: ", totald)
            if segseleccion == 2:
                exv = int(input("Ingrese la cantidad de personas a extraer: "))
                totalv = (exv) - (jorvespertina)
                if totalv < 1:
                    print("No se puede realizar la siguiente acción, debe haber mínimo un trabajador en este turno")
                else:
                    print ("La cantidad de trabajadores para esta jornada es de: ", totalv)
            if segseleccion == 3:
                exn= int(input("Ingrese la cantidad de personas a extraer: "))
                totaln = (exn) - (jornocturna)
                if totaln < 1:
                    print("No se puede realizar la siguiente acción, debe haber mínimo un trabajador en este turno")
                else:
                    print ("La cantidad de trabajadores para esta jornada es de: ", totalv)
            break