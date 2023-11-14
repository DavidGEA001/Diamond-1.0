import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nPor favor complete la informacion con sus datos para completar el registro")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Correo electronico: ")
        password = input("Por favor cree una contraseña: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} {registro[1].apellido}, te haz registrado correctamente")
        else:
            print("\nno te haz registrado correctamente")

    def login(self):
        print("\nPor favor coloque sus datos para ingresar al sistema")
        try:
            verificacion_usuario = input("Ingrese su correo electronico: ")
            verificacion_password = input("Ingrese su contraseña: ")

            usuario = modelo.Usuario('','', verificacion_usuario, verificacion_password)
            login = usuario.identificar()

            if verificacion_usuario == login[3]:
                print(f"\nBienvenido {login[1]}, te haz registrado en el sistema el {login[5]}")
                self.proximasacciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Datos incorrectos, por favor intentelo de nuevo \n--Recuerde que si ingresa mal los datos mas de 3 veces se bloqueara su usuario--")

    def proximasacciones(self, usuario):
        print("""
            Acciones disponibles:
            - Crear Producto (1)
            - Ver tus Productos (2)
            - Eliminar un Producto (3)
            - Salir (4)    
                        
            """)

        Accion2 = input("¿Que quieres hacer a continuacion? ")
        hazEl = notas.acciones.Acciones()

        if Accion2 == "1":
            print("Muy bien, a continuacion ingresa los datos de tu nuevo producto para crearlo")
            hazEl.Crear(usuario)
            self.proximasacciones(usuario)

        elif Accion2 == "2":
            hazEl.Mostrar(usuario)
            self.proximasacciones(usuario)

        elif Accion2 == "3":
            hazEl.Borrar(usuario)
            self.proximasacciones(usuario)

        elif Accion2 == "4":
            print("Haz seleccionado Salir. Gracias por usar nuestro sistema")
            exit()

        else:
            print("Haz seleccionado una opcion incorreccta o inexistente, por favor selecciona una opcion disponible")
            self.proximasacciones(usuario)
