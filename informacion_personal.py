# 1. Crear un Diccionario
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# 2. Acceder y Modificar Valores
# Accedemos a la clave "ciudad" y luego la modificamos
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"

# Agregamos/modificamos la clave "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# 3. Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# 4. Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 5. Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)
