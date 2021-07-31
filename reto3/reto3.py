import os #Importamos modulo os
import time #Importamos modulo time

#Funcion para limpiar pantalla dependiendo del Sistema operativo
def borra_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

#Funcion para ingresar coordenadas
def ingresa_coordenadas():
    coor= []
    for val in range(3):
        print("Sitio", (val+1))
        lat = float(input('Ingrese latitud: '))
        if lat >= -4.227 and lat <= -3.002:
            lat2= lat
        else:
            print("Error coordenada")
            exit()
        lon= float(input('Ingrese longitud: '))
        if lon >= -70.365 and lon <= -69.714:
            lon2= lon
        else:
            print("Error coordenada")
            exit()
        coor.append([lat2, lon2])
    comprobar= "Datos ingresados corectamente"  
    borra_pantalla()
    return comprobar, coor
    time.sleep(1)#Retarda ejecucion programa

#Creamos una lista con cada opción del menú.
menu= ["Cambiar contraseña", 
       "Ingresar coordenadas actuales", 
       "Ubicar zona wifi más cercana", 
       "Guardar archivo con ubicación cercana", 
       "Actualizar registros de zonas wifi desde archivo", 
       "Elegir opción de menú favorita", 
       "Cerrar sesión"]

#Variable que contará los errores en caso de opción equivocada.
contador_errores= 0

user_saved= 52209 #Codigo del grupo
password_saved= "90225"
captcha1= 209
captcha2= int((2*2)+5-9) #Resultado 9
captcha_suma= captcha1 + captcha2 #Resultado de la suma 209 + 0 = 209
veces= 0

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
user_logged= int(input('Ingrese su usuario: '))
if user_logged == user_saved:
    password_inserted= input("Ingrese su contraseña: ")
    if password_inserted == password_saved:
        verificacion= int(input(f"Ingrese el resultado de sumar {captcha1} + {captcha2}: "))
        if verificacion == captcha_suma:
            borra_pantalla()#Llamada a funcion para limpiar la pantalla
            print("Sesión iniciada")
            time.sleep(1)#Retarda ejecucion programa
            #Creamos un ciclo while, éste se encargará de que el menú sea recurrente.
            #Éste ciclo se ejecutara mientras el contador de errores sea menor a 3.
            while contador_errores < 3:
                borra_pantalla()
                for i in range(len(menu)): #función len() devuelve longitud de cadena
                    print(i + 1, "-",  menu[i])
                option= int(input("Elija una opción: "))
                if option > 0 and option < 8:
                    if option == 1:
                        print("Usted ha elegido la opción 1")
                        current_password= input("Ingrese su contraseña actual: ")
                        if current_password == password_saved:
                            borra_pantalla()
                            new_password= input("Ingrese nueva contraseña: ")
                            if new_password != password_saved:
                                password_saved= new_password
                                print("Su contraseña ha sido modificada")
                                time.sleep(2)#Retarda ejecucion programa
                            else:
                                borra_pantalla()
                                print("Error")
                                time.sleep(1)#Retarda ejecucion programa
                                continue
                        else:
                            borra_pantalla()
                            print("Error")
                            time.sleep(1)#Retarda ejecucion programa
                            exit()
                    elif option == 2:
                        print("Usted ha elegido la opción 2")
                        if veces == 0:
                            time.sleep(1)#Retarda ejecucion programa
                            borra_pantalla()
                            comprobar, coor = ingresa_coordenadas()
                            print(comprobar)
                            veces+=1
                            time.sleep(1)#Retarda ejecucion programa
                        else:
                            veces > 1
                            time.sleep(1)#Retarda ejecucion programa
                            borra_pantalla()
                            print("coordenada [latitud, longitud] 1: [{}, {}]".format(coor[0][0], coor[0][1]))
                            print("coordenada [latitud, longitud] 2: [{}, {}]".format(coor[1][0], coor[1][1]))
                            print("coordenada [latitud, longitud] 3: [{}, {}]".format(coor[2][0], coor[2][1]))
                            actualiza= int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada \nPresione 0 para regresar al menú: "))
                            if actualiza == 0:
                                continue
                            elif actualiza == 1:
                                for i in range(2):
                                    lat = float(input('Ingrese latitud: '))
                                    if lat >= -4.227 and lat <= -3.002:
                                        lat1= lat
                                    else:
                                        print("Error coordenada")
                                        exit()
                                    lon= float(input('Ingrese longitud: '))
                                    if lon >= -70.365 and lon <= -69.714:
                                        lon1= lon
                                    else:
                                        print("Error coordenada")
                                        exit()
                                    coor.pop(0)
                                    coor.insert(0, lat1)
                                    coor.insert(1, lon1)
                                    break
                            elif actualiza == 2:
                                for i in range(2):
                                    lat = float(input('Ingrese latitud: '))
                                    if lat >= -4.227 and lat <= -3.002:
                                        lat2= lat
                                    else:
                                        print("Error coordenada")
                                        exit()
                                    lon= float(input('Ingrese longitud: '))
                                    if lon >= -70.365 and lon <= -69.714:
                                        lon2= lon
                                    else:
                                        print("Error coordenada")
                                        exit()
                                    coor.pop(1)
                                    coor.insert(2, lat2)
                                    coor.insert(3, lon2)
                                    break
                            elif actualiza == 3:
                                for i in range(2):
                                    lat = float(input('Ingrese latitud: '))
                                    if lat >= -4.227 and lat <= -3.002:
                                        lat3= lat
                                    else:
                                        print("Error coordenada")
                                        exit()
                                    lon= float(input('Ingrese longitud: '))
                                    if lon >= -70.365 and lon <= -69.714:
                                        lon3= lon
                                    else:
                                        print("Error coordenada")
                                        exit()
                                    coor.pop(2)
                                    coor.insert(4, lat3)
                                    coor.insert(5, lon3)
                                    break
                            else:
                                print("“Error actualización”")
                                exit()
                    elif option == 3:
                        print("Usted ha elegido la opción 3")
                        time.sleep(1)#Retarda ejecucion programa
                        borra_pantalla()#Llamada a funcion para limpiar la pantalla
                        exit()
                    elif option == 4:
                        print("Usted ha elegido la opción 4")
                        time.sleep(1)#Retarda ejecucion programa
                        borra_pantalla()#Llamada a funcion para limpiar la pantalla
                        exit()
                    elif option == 5:
                        print("Usted ha elegido la opción 5")
                        time.sleep(1)#Retarda ejecucion programa
                        borra_pantalla()#Llamada a funcion para limpiar la pantalla
                        exit()
                    elif option == 6:
                        print("Usted ha elegido la opción 6")
                        opcion_elegida= int(input("Seleccione opción favorita: "))
                        if opcion_elegida == 1 or opcion_elegida == 2 or opcion_elegida == 3 or opcion_elegida == 4 or opcion_elegida == 5:
                            borra_pantalla()#Llamada a funcion para limpiar la pantalla
                            print("Usted a elegido la opción", opcion_elegida)
                            time.sleep(1)#Retarda ejecucion programa
                            borra_pantalla()
                            adivina1= int(input("Para confirmar por favor responda: Redondo soy y es cosa anunciada que a la derecha algo valgo, pero a la izquierda nada, la respuesta es: "))
                            if adivina1 == 0:
                                adivina2=int(input("Para confirmar por favor responda: Tengo forma de serpiente, y entre el dos y el cuatro siempre estoy cuando me buscas, la respuesta es: "))   
                                if adivina2 == 3:
                                    #guardamos en la variable mover, el elemento de la lista elegido por el usuario.
                                    mover= menu[opcion_elegida - 1] #restamos 1
                                    menu.remove(mover)#eliminamos el objeto de la lista
                                    menu.insert(0, mover)# Lo agregamos de nuevo en la posicion inicial
                                else:
                                    borra_pantalla()#Llamada a funcion para limpiar la pantalla
                                    print("Error")
                                    time.sleep(1)#Retarda ejecucion programa
                                    borra_pantalla()
                            else:
                                borra_pantalla()#Llamada a funcion para limpiar la pantalla
                                print("Error")
                                time.sleep(1)#Retarda ejecucion programa
                                borra_pantalla()
                        else:
                            borra_pantalla()#Llamada a funcion para limpiar la pantalla
                            print("Usted a elegido la opción", opcion_elegida)
                            time.sleep(1)#Retarda ejecucion programa
                            borra_pantalla()#Llamada a funcion para limpiar la pantalla
                            print("Error")
                            time.sleep(1)#Retarda ejecucion programa
                            exit()
                    else:
                        option == 7
                        borra_pantalla()#Llamada a funcion para limpiar la pantalla
                        print("Hasta pronto")
                        time.sleep(1)#Retarda ejecucion programa
                        exit()
                else:
                    contador_errores += 1
                    borra_pantalla()#Llamada a funcion para limpiar la pantalla
                    print("Error")
                    time.sleep(1)#Retarda ejecucion programa
                    continue
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
