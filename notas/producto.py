import usuarios.conexion

conn = usuarios.conexion.conectar()
database = conn[0]
cursor = conn[1]

class Producto:
    
    def __init__(self, id_usuarios, titulo = "", descripcion = ""):
        self.id_usuarios = id_usuarios
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO productos VALUES(null, %s, %s, %s, NOW())"
        producto = (self.id_usuarios, self.titulo, self.descripcion)

        cursor.execute(sql, producto)
        database.commit()

        return[cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM productos WHERE id_usuarios = {self.id_usuarios}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def Eliminar(self):
        seleccion = input("Ingresa el id del producto que deseas eliminar (Si no conoces el id de tu producto puedes ir a la opcion Mostrar Producstos): ")
        num_seleccion = int(seleccion)
        sql = f"DELETE FROM productos WHERE id_usuarios = {self.id_usuarios} AND id_productos = {num_seleccion}"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self, num_seleccion]

