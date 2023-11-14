from usuarios import acciones

print("""Bienvenido a Diamond 
\nAcciones disponibles:
      - Registrarse como proveedor (Oprima 1)
      - Iniciar sesion (Oprima 2)
""")

hazEL = acciones.Acciones()

accion = input("¿Que quieres realizar?  ")

if accion == "1":
    hazEL.registro()
    
elif accion == "2":
    hazEL.login()

    