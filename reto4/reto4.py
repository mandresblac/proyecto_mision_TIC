import os #Importamos modulo os
import time #Importamos modulo time
import math

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


#funcion para medir distancia reto 4
def distancia(lat1, lat2, lon1, lon2):
    #Paso de grados a radianes
    lat1r= lat1*(math.pi/180)
    lat2r= lat2*(math.pi/180)
    lon1r= lon1*(math.pi/180)
    lon2r= lon2*(math.pi/180)
    #Calcuo deltas
    Dlat= lat2r - lat1r
    Dlon= lon2r - lon1r
    #calculo ecuacion por partes
    a= math.sin(Dlat/2)**2
    b= math.cos(lat1r)
    c= math.cos(lat2r)
    d= math.sin(Dlon/2)**2
    r= 6372.795477598 #Radi de la tierra en Km
    distancia = 2*r*math.asin(math.sqrt(a + b * c * d))
    return distancia

#Funcion de tiempo reto 4
def tiempo(n1, n2):
	t= n1 / n2
	return t 

#Creamos una lista con cada opción del menú reto1.
menu= ["Cambiar contraseña", 
       "Ingresar coordenadas actuales", 
       "Ubicar zona wifi más cercana", 
       "Guardar archivo con ubicación cercana", 
       "Actualizar registros de zonas wifi desde archivo", 
       "Elegir opción de menú favorita", 
       "Cerrar sesión"]

#Matris reto 4
zonas_wifi= [[-3.777, -70.302, 91],
             [-4.134, -69.983, 233],
             [-4.006, -70.132, 149],
             [-3.846, -70.222, 211]]

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
                        borra_pantalla()
                        if veces == 0:
                            print("Error sin registro de coordenadas")
                            exit()
                        else:
                            #time.sleep(1)#Retarda ejecucion programa
                            #borra_pantalla()
                            print("coordenada [latitud, longitud] 1: [{}, {}]".format(coor[0][0], coor[0][1]))
                            print("coordenada [latitud, longitud] 2: [{}, {}]".format(coor[1][0], coor[1][1]))
                            print("coordenada [latitud, longitud] 3: [{}, {}]".format(coor[2][0], coor[2][1]))
                            ubicacion_actual= int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
                            time.sleep(1)#Retarda ejecucion programa
                            borra_pantalla()
                            if ubicacion_actual == 1:
                                dt1= []
                                da1= distancia(coor[0][0], zonas_wifi[0][0] , coor[0][1], zonas_wifi[0][1])
                                dt1.append([da1, 91, 1])
                                da2= distancia(coor[0][0], zonas_wifi[1][0] , coor[0][1], zonas_wifi[1][1])
                                dt1.append([da2, 233, 2])
                                da3= distancia(coor[0][0], zonas_wifi[2][0] , coor[0][1], zonas_wifi[2][1])
                                dt1.append([da3, 149, 3])
                                da4= distancia(coor[0][0], zonas_wifi[3][0] , coor[0][1], zonas_wifi[3][1])
                                dt1.append([da4, 211, 4])
                                dt1.sort()
                                #print(dt1)
                                print("Zonas wifi cercanas con menos usuarios:")
                                print(f"La zona wifi {dt1[0][2]}: esta a {round(dt1[0][0], 2)} kilometros, tiene en promedio {dt1[0][1]} usuarios.")
                                print(f"La zona wifi {dt1[1][2]}: esta a {round(dt1[1][0], 2)} kilometros, tiene en promedio {dt1[1][1]} usuarios.")
                                indicaciones= int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
                                time.sleep(1)#Retarda ejecucion programa
                                borra_pantalla()
                                if indicaciones == 1:
                                    if zonas_wifi[0][0] > coor[0][0] and zonas_wifi[0][1] > coor[0][1]:
                                        print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt1[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt1[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                    else:
                                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt1[0][0], 20.83), 1)} horas \nTiempo promedio en bicicleta: {round(tiempo(dt1[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                elif indicaciones == 2:
                                    if zonas_wifi[1][0] > coor[1][0] and zonas_wifi[1][1] > coor[1][1]:
                                        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt1[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt1[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                        time.sleep(10)#Retarda ejecucion programa
                                        borra_pantalla()
                                    else:
                                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt1[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt1[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                        time.sleep(10)#Retarda ejecucion programa
                                        borra_pantalla()
                                else:
                                    print("Error zona wifi")
                                    exit()
                                time.sleep(20)#Retarda ejecucion programa
                                borra_pantalla()
                                continue
                            elif ubicacion_actual == 2:
                                dt2= []
                                db1= distancia(coor[1][0], zonas_wifi[0][0] , coor[1][1], zonas_wifi[0][1])
                                dt2.append([db1, 91, 1])
                                db2= distancia(coor[1][0], zonas_wifi[1][0] , coor[1][1], zonas_wifi[1][1])
                                dt2.append([db2, 233, 2])
                                db3= distancia(coor[1][0], zonas_wifi[2][0] , coor[1][1], zonas_wifi[2][1])
                                dt2.append([db3, 149, 3])
                                db4= distancia(coor[1][0], zonas_wifi[3][0] , coor[1][1], zonas_wifi[3][1])
                                dt2.append([db4, 211, 4])
                                dt2.sort()
                                print("Zonas wifi cercanas con menos usuarios:")
                                print(f"La zona wifi {dt2[0][2]}: esta a {round(dt2[0][0], 2)} kilometros, tiene en promedio {dt2[0][1]} usuarios.")
                                print(f"La zona wifi {dt2[1][2]}: esta a {round(dt2[1][0], 2)} kilometros, tiene en promedio {dt2[1][1]} usuarios.")
                                indicaciones= int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
                                time.sleep(1)#Retarda ejecucion programa
                                borra_pantalla()
                                if indicaciones == 1:
                                    if zonas_wifi[0][0] > coor[0][0] and zonas_wifi[0][1] > coor[0][1]:
                                        print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt2[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt2[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                    else:
                                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt2[0][0], 20.83), 1)} horas \nTiempo promedio en bicicleta: {round(tiempo(dt2[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                elif indicaciones == 2:
                                    if zonas_wifi[1][0] > coor[1][0] and zonas_wifi[1][1] > coor[1][1]:
                                        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt2[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt2[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                        time.sleep(10)#Retarda ejecucion programa
                                        borra_pantalla()
                                    else:
                                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt2[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt2[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                        time.sleep(10)#Retarda ejecucion programa
                                        borra_pantalla()
                                else:
                                    print("Error zona wifi")
                                    exit()
                                time.sleep(20)#Retarda ejecucion programa
                                borra_pantalla()
                                continue
                            elif ubicacion_actual == 3:
                                dt3= []
                                dc1= distancia(coor[2][0], zonas_wifi[0][0] , coor[2][1], zonas_wifi[0][1])
                                dt3.append([dc1, 91, 1])
                                dc2= distancia(coor[2][0], zonas_wifi[1][0] , coor[2][1], zonas_wifi[1][1])
                                dt3.append([dc2, 233, 2])
                                dc3= distancia(coor[2][0], zonas_wifi[2][0] , coor[2][1], zonas_wifi[2][1])
                                dt3.append([dc3, 149, 3])
                                dc4= distancia(coor[2][0], zonas_wifi[3][0] , coor[2][1], zonas_wifi[3][1])
                                dt3.append([dc4, 211, 4])
                                dt3.sort()
                                print(f"La zona wifi {dt3[0][2]}: esta a {round(dt3[0][0], 2)} kilometros, tiene en promedio {dt3[0][1]} usuarios.")
                                print(f"La zona wifi {dt3[1][2]}: esta a {round(dt3[1][0], 2)} kilometros, tiene en promedio {dt3[1][1]} usuarios.")
                                indicaciones= int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
                                time.sleep(1)#Retarda ejecucion programa
                                borra_pantalla()
                                if indicaciones == 1:
                                    if zonas_wifi[0][0] > coor[0][0] and zonas_wifi[0][1] > coor[0][1]:
                                        print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt3[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt3[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                    else:
                                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt3[0][0], 20.83), 1)} horas \nTiempo promedio en bicicleta: {round(tiempo(dt3[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                elif indicaciones == 2:
                                    if zonas_wifi[1][0] > coor[1][0] and zonas_wifi[1][1] > coor[1][1]:
                                        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt3[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt3[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                        time.sleep(10)#Retarda ejecucion programa
                                        borra_pantalla()
                                    else:
                                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte.")
                                        print(f"Tiempo promedio en auto: {round(tiempo(dt3[0][0], 20.83), 0)} horas. \nTiempo promedio en bicicleta: {round(tiempo(dt3[0][0], 3.33), 1)} horas.")
                                        salir= int(input("Presione 0 para salir: "))
                                        if salir == 0:
                                            continue
                                        time.sleep(10)#Retarda ejecucion programa
                                        borra_pantalla()
                                else:
                                    print("Error zona wifi")
                                    exit()
                                time.sleep(20)#Retarda ejecucion programa
                                borra_pantalla()
                                continue
                            else:
                                print("Error ubicación")
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
