def agregar_alumno():
    alumnos = []

    while True:
        nombre = input("Ingrese el nombre del alumno ('fin' para salir, 'mostrar' para ver los datos): ")
        if nombre.lower() == "fin":
            break
        elif nombre.lower() == "mostrar":
            if alumnos:
                print("\nRegistro de alumnos:")
                for i, alumno in enumerate(alumnos, 1):
                    print(f"Alumno {i}: {alumno}")
            else:
                print("No se han ingresado alumnos aún.")
            continue  # Regresa al inicio del ciclo sin guardar los datos si se elige 'mostrar'

        apellido = input("Ingrese el apellido del alumno: ")
        
        # Manejo de errores para el ingreso del DNI
        while True:
            try:
                dni = input("Ingrese el DNI del alumno (solo números): ")
                dni = int(dni) 
                break  
            except ValueError:
                print("Error: El DNI debe contener solo números.")
        
        # Manejo de errores para el ingreso del nombre y apellido
        while True:
            if any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
                print("Error: El nombre y apellido no pueden contener números.")
                nombre = input("Ingrese el nombre del alumno nuevamente: ")
                apellido = input("Ingrese el apellido del alumno nuevamente: ")
            else:
                break
        
        # Ingreso de las notas del alumno
        notas = []
        for i in range(3):
            nota = input(f"Ingrese la nota {i+1} del alumno: ")
            notas.append(nota)
        
        # Ingreso de las faltas y amonestaciones
        faltas = int(input("Ingrese la cantidad de faltas del alumno: "))
        amonestaciones = int(input("Ingrese la cantidad de amonestaciones del alumno: "))
        
        
        
        alumno = {"Nombre": nombre, "Apellido": apellido, "DNI": dni, "Notas": notas,
                  "Faltas": faltas, "Amonestaciones": amonestaciones}
        alumnos.append(alumno)

    return alumnos

registro_alumnos = agregar_alumno()
