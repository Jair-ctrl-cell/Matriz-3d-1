# Escritura de Archivo de Texto
# Se crea (o sobrescribe) un archivo llamado "my_notes.txt"
# y se escriben tres líneas de notas personales

with open("my_notes.txt", "w") as file:
    file.write("Primera nota: La práctica constante mejora mis habilidades en programación.\n")
    file.write("Segunda nota: Es importante organizar el tiempo de estudio.\n")
    file.write("Tercera nota: Revisar los errores me ayuda a aprender más.\n")

# Lectura de Archivo de Texto
# Se abre el archivo en modo lectura y se leen las líneas una por una

with open("my_notes.txt", "r") as file:
    line = file.readline()  # lee la primera línea
    while line:
        print(line.strip())  # muestra la línea sin saltos extra
        line = file.readline()  # lee la siguiente línea

# Nota: El uso de 'with' asegura que el archivo se cierre automáticamente
# después de completar las operaciones de lectura o escritura.
