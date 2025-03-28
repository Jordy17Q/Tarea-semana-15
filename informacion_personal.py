# Crear un diccionario inicial con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"  # Cambiar la ciudad a Guayaquil

# Agregar una nueva clave-valor para el teléfono
informacion_personal["telefono"] = "0987654321"  # Agregar un número de teléfono ficticio

# Verificar si la clave "telefono" ya existe (aunque ya se agregó anteriormente)
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "1234567890"  # Esto no se ejecutará en este caso

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]  # Ya que no es necesaria

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)