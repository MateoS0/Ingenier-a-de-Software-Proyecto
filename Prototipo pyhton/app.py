import os
import json

# Rutas de los archivos
instituciones_path = "instituciones.txt"
malla_curricular_path = "malla_curricular.txt"

# Función para registrar una nueva institución
def registrar_institucion():
    nombre = input("Nombre de la institución: ")
    direccion = input("Dirección: ")
    contacto = input("Contacto: ")
    
    # Crear un diccionario con la información de la institución
    institucion = {
        "nombre": nombre,
        "direccion": direccion,
        "contacto": contacto
    }
    
    # Guardar la institución en un archivo de texto
    with open(instituciones_path, "a") as file:
        file.write(json.dumps(institucion) + "\n")
    
    print("Institución registrada con éxito.")

# Función para editar la información de una institución
def editar_institucion():
    nombre = input("Nombre de la institución a editar: ")
    
    # Leer las instituciones del archivo
    instituciones = []
    with open(instituciones_path, "r") as file:
        instituciones = [json.loads(line) for line in file]
    
    # Buscar y editar la institución
    for institucion in instituciones:
        if institucion["nombre"] == nombre:
            institucion["direccion"] = input("Nueva dirección: ")
            institucion["contacto"] = input("Nuevo contacto: ")
            break
    else:
        print("Institución no encontrada.")
        return
    
    # Guardar los cambios
    with open(instituciones_path, "w") as file:
        for institucion in instituciones:
            file.write(json.dumps(institucion) + "\n")
    
    print("Información de la institución actualizada con éxito.")

# Función para borrar una institución
def borrar_institucion():
    nombre = input("Nombre de la institución a borrar: ")
    
    # Leer las instituciones del archivo
    instituciones = []
    with open(instituciones_path, "r") as file:
        instituciones = [json.loads(line) for line in file]
    
    # Filtrar la institución a borrar
    instituciones = [inst for inst in instituciones if inst["nombre"] != nombre]
    
    # Guardar los cambios
    with open(instituciones_path, "w") as file:
        for institucion in instituciones:
            file.write(json.dumps(institucion) + "\n")
    
    print("Institución borrada con éxito.")

# Función para ver la lista de instituciones inscritas
def ver_instituciones():
    if not os.path.exists(instituciones_path):
        print("No hay instituciones registradas.")
        return
    
    with open(instituciones_path, "r") as file:
        instituciones = [json.loads(line) for line in file]
    
    if not instituciones:
        print("No hay instituciones registradas.")
    else:
        print("Instituciones registradas:")
        for institucion in instituciones:
            print(f"Nombre: {institucion['nombre']}, Dirección: {institucion['direccion']}, Contacto: {institucion['contacto']}")

# Función para gestionar la malla curricular
def gestionar_malla_curricular():
    institucion = input("Nombre de la institución: ")
    
    # Crear o abrir el archivo de malla curricular
    if os.path.exists(malla_curricular_path):
        with open(malla_curricular_path, "r") as file:
            lines = file.readlines()
    else:
        lines = []
    
    # Buscar la sección correspondiente a la institución
    section_found = False
    new_lines = []
    for line in lines:
        if line.strip() == f"[{institucion}]":
            section_found = True
            new_lines.append(line)
            while True:
                materia = input("Nombre de la materia (o 'salir' para terminar): ")
                if materia.lower() == 'salir':
                    break
                descripcion = input("Descripción de la materia: ")
                
                # Agregar materia y descripción
                new_lines.append(f"{materia}: {descripcion}\n")
            continue
        
        # Si encontramos una nueva sección, añadimos la antigua
        if section_found and line.startswith('['):
            section_found = False
            new_lines.append(f"[{institucion}]\n")
        new_lines.append(line)
    
    if not section_found:
        # Añadir una nueva sección para la institución si no existe
        new_lines.append(f"\n[{institucion}]\n")
        while True:
            materia = input("Nombre de la materia (o 'salir' para terminar): ")
            if materia.lower() == 'salir':
                break
            descripcion = input("Descripción de la materia: ")
            new_lines.append(f"{materia}: {descripcion}\n")
    
    # Guardar el archivo de malla curricular
    with open(malla_curricular_path, "w") as file:
        file.writelines(new_lines)
    
    print("Malla curricular guardada con éxito.")

# Función para borrar una materia de la malla curricular
def borrar_materia():
    institucion = input("Nombre de la institución: ")
    materia_a_borrar = input("Nombre de la materia a borrar: ")
    
    if not os.path.exists(malla_curricular_path):
        print("No se ha encontrado la malla curricular.")
        return
    
    with open(malla_curricular_path, "r") as file:
        lines = file.readlines()
    
    section_found = False
    new_lines = []
    for line in lines:
        if line.strip() == f"[{institucion}]":
            section_found = True
            new_lines.append(line)
            continue
        
        if section_found and line.startswith('['):
            section_found = False
            new_lines.append(line)
        
        if section_found and materia_a_borrar in line:
            print(f"Materia '{materia_a_borrar}' borrada con éxito.")
            continue
        
        new_lines.append(line)
    
    if not section_found:
        print("Institución no encontrada en la malla curricular.")
        return
    
    with open(malla_curricular_path, "w") as file:
        file.writelines(new_lines)
    
    print("Malla curricular actualizada con éxito.")

# Menú principal
def menu():
    while True:
        print("\nPrototipo de Sistema")
        print("1. Registrar nueva institución")
        print("2. Editar información de institución")
        print("3. Borrar institución")
        print("4. Ver lista de instituciones")
        print("5. Gestionar malla curricular")
        print("6. Borrar materia de la malla curricular")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_institucion()
        elif opcion == "2":
            editar_institucion()
        elif opcion == "3":
            borrar_institucion()
        elif opcion == "4":
            ver_instituciones()
        elif opcion == "5":
            gestionar_malla_curricular()
        elif opcion == "6":
            borrar_materia()
        elif opcion == "7":
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
menu()



