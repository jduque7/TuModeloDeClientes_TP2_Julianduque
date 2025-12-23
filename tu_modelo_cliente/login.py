BD_USUARIOS = {}

def registrar_usuario():
    print("Registro de Usuario ")
    usuario = input("Cree un usuario: ").strip()

    while usuario in BD_USUARIOS:
        print("Ese usuario ya existe. Intente otro.")
        usuario = input("Cree un usuario: ").strip()

    contraseña = input("Cree una contraseña: ").strip()
    BD_USUARIOS[usuario] = contraseña

    print("Usuario registrado correctamente.")
    return usuario


def login():
    print("\nInicio de Sesión")
    print("1. Ingresar con usuario registrado")
    print("2. Ingresar como invitado")

    opcion = input("Seleccione una opción: ").strip()

    
    if opcion == "1":
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        if BD_USUARIOS.get(usuario) == contraseña:
            print("Acceso concedido.")
            return True

        print("Credenciales incorrectas.")
        return False

   
    elif opcion == "2":
        print("Ingresaste como invitado.")
        return True

    else:
        print("Opción inválida.")
        return False
