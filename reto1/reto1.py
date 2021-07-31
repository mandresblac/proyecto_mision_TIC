"""
Reqisitos:
- El programa debe arrojar un mensaje de bienvenida en la primera línea "Bienvenido al sistema de ubicación para zonas  públicas WIFI".
- Debe haber un usario guardado internamente y sera el número 51593
- Debe haber una contraseña guardada internamente y sera inversa al número de usuario 39515
- Se le pedira al usuario el ingreso de usuario y contraseña.
- Se solicitara un captcha que debe ser generado con las siguientes partes:
- El primer termino del captcha seran los tres ultimos digitos del usuario (593)
- El segundo termino del captcha sera el penultimo número del usuario (9) y este debera hallarse a través del resultado de aplicar varias operaciones aritméticas con los otros números del código, debe guardarse en una variable  y calcularse internamente por el sistema.
- El resultado del captcha sera la suma de los dos terminos anteriores.
- Si el nombre del usuario es correcto se validara, de lo contrario se mostrara el mesaje "Error" y finalizara el programa.
- Si la contraseña es correcta se validara, de lo contrario se mostrara el mesaje "Error" y finalizara el programa.
- Si la respuesta al captcha no es correcto mostrara el mensaje "Error", de los contrario mostrara el mensaje "Sesion iniciada".
- Si los tres datos estan bien ingresados mostrara el mensaje "Sesión iniciada"
"""

user_saved= 52209 #Codigo del grupo
password_saved= 90225
captcha1= 209
captcha2= int((2*2)+5-9) #Resultado 9
captcha_suma= captcha1 + captcha2 #Resultado de la suma 209 + 0 = 602

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

user_logged= int(input('Ingrese su usuario: '))
if user_logged == user_saved:
    password_inserted= int(input("Ingrese su contraseña: "))
    if password_inserted == password_saved:
        verificacion= int(input(f"Ingrese el resultado de sumar {captcha1} + {captcha2}: "))
        if verificacion == captcha_suma:
            print("Sesión iniciada")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")