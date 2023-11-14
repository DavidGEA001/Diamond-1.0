import datetime
import hashlib
import usuarios.conexion 

conn = usuarios.conexion.conectar()
database = conn[0]
cursor = conn[1]



class Usuario:

    def __init__(self, nombre, apellido, email, password,):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrando contraseñas
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result

    
    def identificar(self):
        #consulta para verificar si existe el usuario

        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrando contraseñas
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result