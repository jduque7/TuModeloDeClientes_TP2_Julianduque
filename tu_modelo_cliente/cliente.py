class Cliente:
    total_clientes = 0

    def __init__(self, nombre, apellido, dni, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        Cliente.total_clientes += 1

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} | DNI: {self.dni} | Tel: {self.telefono} | Email: {self.email}"

    
    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

    @classmethod
    def registrar_cliente_interactivo(cls):
        print("=== Registrar Nuevo Cliente ===")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        return cls(nombre, apellido, dni, telefono, email)
