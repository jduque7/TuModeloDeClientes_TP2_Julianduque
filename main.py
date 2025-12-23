from tu_modelo_cliente import Cliente
from tu_modelo_cliente.login import registrar_usuario, login


def mostrar_menu():
    print("\n MENÚ PRINCIPAL ")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Editar cliente")
    print("4. Salir")
    return input("Seleccione una opción: ").strip()


def main():
    clientes = []

    print("=== MENÚ INICIAL ===")
    print("1. Registrar usuario")
    print("2. Ir al inicio de sesión")
    opcion_inicio = input("Seleccione una opción: ").strip()

    if opcion_inicio == "1":
        registrar_usuario()
        if not login():
            print("Acceso denegado.")
            return

    elif opcion_inicio == "2":
        if not login():
            print("Acceso denegado.")
            return

    else:
        print("Opción inválida.")
        return

    # MENÚ PRINCIPAL
    while True:
        opcion = mostrar_menu()

       
        if opcion == "1":
            nuevo = Cliente.registrar_cliente_interactivo()
            clientes.append(nuevo)
            print("Cliente registrado.")

        
        elif opcion == "2":
            if not clientes:
                print("No hay clientes registrados.")
            else:
                print("\nLISTA DE CLIENTES")
                for idx, c in enumerate(clientes, start=1):
                    print(f"{idx}. {c}")
                    print("--------------------")

        
        elif opcion == "3":
            if not clientes:
                print("No hay clientes para editar.")
                continue

            print("\nSeleccione el cliente a editar:")
            for idx, c in enumerate(clientes, start=1):
                print(f"{idx}. {c.nombre} {c.apellido}")

            seleccion = input("Número del cliente: ").strip()

            if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(clientes)):
                print("Selección inválida.")
                continue

            cliente = clientes[int(seleccion) - 1]

            print("\n¿Qué desea editar?")
            print("1. Teléfono")
            print("2. Email")
            opcion_edit = input("Seleccione: ").strip()

            if opcion_edit == "1":
                nuevo_tel = input("Nuevo teléfono: ").strip()
                cliente.actualizar_telefono(nuevo_tel)
                print("Teléfono actualizado.")

            elif opcion_edit == "2":
                nuevo_email = input("Nuevo email: ").strip()
                cliente.actualizar_email(nuevo_email)
                print("Email actualizado.")

            else:
                print("Opción invalida.")

        
        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
