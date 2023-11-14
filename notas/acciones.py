import notas.producto as modelo

class Acciones:

    def Crear(self, usuario):
        print("Okey, Creemos tu nuevo producto... ")

        titulo = input("Introduce el nombre de tu producto: ")
        descripcion = input("Describe tu producto: ")

        producto = modelo.Producto(usuario[0], titulo, descripcion)
        guardar = producto.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto haz guardado tu producto: {producto.titulo}")
        else:
            print("No se ha guardado el producto, lo siento")

    def Mostrar(self, usuario):
        print("A continuacion se muestran tus productos: ")

        producto = modelo.Producto(usuario[0])
        productos = producto.listar()

        for producto in productos:
            print("\n---------------------------------------------------")
            print(f"id: {producto[0]}")
            print(producto[2])
            print(producto[3])
            print("---------------------------------------------------")

    def Borrar(self, usuario):
        producto = modelo.Producto(usuario[0])
        eliminar = producto.Eliminar()

        if eliminar[0] >= 0:
            print(f"Hemos borrado el producto # {eliminar[2]}")
        else:
            print("Error: No se ha borrado nada")




    
    



