import os #Importamos modulo os
import time #Importamos modulo time

#Funcion para limpiar pantalla dependiendo del Sistema operativo
def borra_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

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
password_saved= 90225
captcha1= 209
captcha2= int((2*2)+5-9) #Resultado 9
captcha_suma= captcha1 + captcha2 #Resultado de la suma 209 + 0 = 209

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
user_logged= int(input('Ingrese su usuario: '))
if user_logged == user_saved:
    password_inserted= int(input("Ingrese su contraseña: "))
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
                        time.sleep(1)#Retarda ejecucion programa
                        borra_pantalla()#Llamada a funcion para limpiar la pantalla
                        exit()
                    elif option == 2:
                        print("Usted ha elegido la opción 2")
                        time.sleep(1)#Retarda ejecucion programa
                        borra_pantalla()#Llamada a funcion para limpiar la pantalla
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
