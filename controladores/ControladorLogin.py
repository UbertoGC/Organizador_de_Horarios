def comprobar_login(cur,correo,password):
    obtener_info = []
    cur.execute("SELECT * from usuarios WHERE Correo = %d",(correo))
    obtener_info = cur.fetchall()
    if(len(obtener_info) == 0):
        print("No existe dicho Usuario")
    else:
        if(password != obtener_info[0][2]):
            print("Contraseña Incorrecta")
        else:
            print("Contraseña Correcta")
    print(obtener_info)