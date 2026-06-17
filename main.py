#Trabajo práctico integrador - Programación I

#Lee el archivo CSV y carga los datos de los países en una lista de diccionarios.
def leer_csv():
    paises = []
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()
        #Se omite la primera línea que corresponde a los encabezados.
        for linea in lineas[1:]:
            datos_paises = linea.strip().split(",")

            paises.append({
                "nombre": datos_paises[0],
                "poblacion": int(datos_paises[1]),
                "superficie": int(datos_paises[2]),
                "continente": datos_paises[3],
            })
    return paises

#Reescribe el archivo csv con los datos actualizados almacenados en memoria.
def actualizar_csv(paises):
    with open("paises.csv", "w") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")

#Función principal. Controla el menú y la ejecución de cada función.
def main():
    paises = leer_csv()
    print("Bienvenido al sistema de gestión de datos de países")
    #Menú principal interactivo persistente hasta que el usuario selecciona la opción para salir.
    while True:
        mostrar_menu()
        #Validación de la opción ingresada por el usuario.
        try:
            seleccion_menu=int((input(" Opción número: ")))
            print()
            if seleccion_menu < 1 or seleccion_menu >7:
                raise ValueError
        except ValueError:
            print("La opción ingresada es inválida, intente nuevamente")
            continue

        if seleccion_menu==1:
            agregar_pais(paises)
        elif seleccion_menu==2:
            actualizar_datos_pais(paises)
        elif seleccion_menu==3:
            buscar_pais(paises)
        elif seleccion_menu==4:
            filtrar_paises(paises)
        elif seleccion_menu==5:
            ordenar_paises(paises)
        elif seleccion_menu==6:
            estadisticas_paises(paises)
        elif seleccion_menu==7:
            print("Gracias por utilizar el sistema de gestión de datos de países. Hasta luego!")
            break

#Muestra las opciones del menú principal.
def mostrar_menu():
    print()
    print("""Ingrese el número correspondiente para seleccionar una opción del menú:
        1. Agregar país
        2. Actualizar datos de Población o Superficie de un país
        3. Buscar país  
        4. Filtrar países por:
          - Continente
          - Rango de población
          - Rango de superficie
        5. Ordenar países por:
          - Nombre
          - Población
          - Superficie
        6. Estadísticas de países
        7. Salir
        """)

#Permite agregar un nuevo país verificando la validez de los datos ingresados.
def agregar_pais(paises):
    while True:
        nuevo_pais = input(f"Ingrese el país a agregar: ").strip().title() 
        pais_existente = False
        #Se valida que el país no exista en la lista.
        for pais in paises:
            if pais["nombre"] == nuevo_pais:
                pais_existente = True
                break

        if nuevo_pais == "" or pais_existente == True:
            if nuevo_pais=="":
                print("Nombre de país inválido (No puede quedar vacío).")
                continue
            elif pais_existente == True:
                print("Dato existente, el país ya se encuentra en la lista.")
                continue
        #Se valida que el número ingresado sea un entero positivo.
        try:
            poblacion_nuevo_pais = int(input(f"Ingrese la población de {nuevo_pais}: "))
            if poblacion_nuevo_pais <= 0:
                    raise ValueError
        except ValueError:
            print("La opción ingresada es inválida")
            continue
        try:
            superficie_nuevo_pais = int(input(f"Ingrese la superficie en km2 de {nuevo_pais}: "))
            if superficie_nuevo_pais <= 0:
                    raise ValueError
        except ValueError:
            print("La opción ingresada es inválida")
            continue
        
        continente_nuevo_pais = input(f"""Ingrese el continente de {nuevo_pais}: 
            Las opciones son:
            - África
            - América
            - Asia
            - Europa
            - Oceanía
            """).strip().title()
        if continente_nuevo_pais == "África":
            continente_nuevo_pais = "Africa"
        elif continente_nuevo_pais == "América":
            continente_nuevo_pais = "America"
        elif continente_nuevo_pais == "Oceanía":
            continente_nuevo_pais = "Oceania"

        if continente_nuevo_pais not in ["Africa", "America", "Asia", "Europa", "Oceania"]:
            print("La opción ingresada es inválida")
            continue

        paises.append({"nombre":nuevo_pais ,"poblacion":poblacion_nuevo_pais,"superficie":superficie_nuevo_pais,"continente":continente_nuevo_pais})
        #Se guardan los cambios realizados en el CSV.
        actualizar_csv(paises)
        print(f"País agregado con éxito")
        break

#Actualiza la población o superficie de un país existente.
def actualizar_datos_pais(paises):
    while True:
        pais_a_actualizar = input(f"Ingrese el país a actualizar: ").strip().title() 
        pais_existente = False
        #Se busca en la lista el país ingresado por el usuario.
        for pais in paises:
            if pais["nombre"] == pais_a_actualizar:
                pais_existente = True
                pais_encontrado = pais
                break

        if pais_a_actualizar == "" or pais_existente != True:
            if pais_a_actualizar=="":
                print("Nombre de país inválido (No puede quedar vacío).")
                continue
            elif pais_existente != True:
                print("El país no se encuentra en la lista. Primero debe incluirlo")
                continue
        #Menú para seleccionar que dato se desea actualizar.
        while True:
            try:
                opcion_a_actualizar= int(input("""Ingrese el número correspondiente para seleccionar una opción: 
                    1. Actualizar la población del país.
                    2. Actualizar la superficie del país.
                    : """))
                if opcion_a_actualizar not in (1, 2):
                    raise ValueError
                break
            except ValueError:
                print("La opción ingresada es inválida, intente nuevamente")
                continue
        
        if opcion_a_actualizar == 1:
            try:
                actualizar_poblacion_pais = int(input(f"Ingrese la nueva población de {pais_a_actualizar}: "))
                if actualizar_poblacion_pais <= 0:
                        raise ValueError
            except ValueError:
                print("La opción ingresada es inválida")
                continue
            else:
                pais_encontrado["poblacion"] = actualizar_poblacion_pais
                actualizar_csv(paises)
                print(f"Población de {pais_a_actualizar} actualizada con éxito.")
                break

        elif opcion_a_actualizar == 2:
            try:
                actualizar_superficie_pais = int(input(f"Ingrese la nueva superficie en km2 de {pais_a_actualizar}: "))
                if actualizar_superficie_pais <= 0:
                        raise ValueError
            except ValueError:
                print("La opción ingresada es inválida")
                continue
            else:
                pais_encontrado["superficie"] = actualizar_superficie_pais
                actualizar_csv(paises)
                print(f"Superficie de {pais_a_actualizar} actualizada con éxito.")
                break

#Busca un país permitiendo coincidencias parciales o exactas.
def buscar_pais(paises):
    while True:
        pais_a_buscar = input(f"Ingrese el país a buscar: ").strip().title() 

        if pais_a_buscar=="":
            print("Nombre de país inválido (No puede quedar vacío).")
            continue
        
        if len(pais_a_buscar) < 3:
            print("Ingrese al menos 3 letras para realizar la búsqueda")
            continue
        
        pais_existente = False

        print("Resultados de la búsqueda:")
        for pais in paises:
            if pais_a_buscar.lower() in pais["nombre"].lower():
                pais_existente = True
                print(f"""
                País: {pais["nombre"]}
                Población: {pais["poblacion"]}
                Superficie: {pais["superficie"]} km2
                Continente: {pais["continente"]}
                    """)

        if pais_existente == False:
            print("El país no se encuentra en la lista.")
            continue
        break

#Filtra los países según continente, población o superficie.
def filtrar_paises(paises):
    #Solicita al usuario el indicador para filtrar.
    while True:
        try:
            opcion_a_filtrar= int(input("""Ingrese el número correspondiente para seleccionar una opción: 
                1. Filtrar por continente.
                2. Filtrar por rango de población.
                3. Filtrar por rango de superficie.
                : """))
            if opcion_a_filtrar not in (1, 2, 3):
                raise ValueError
            break
        except ValueError:
            print("La opción ingresada es inválida, intente nuevamente")
            continue
    #En las 3 opciones se recorre la lista mostrando únicamente los países que cumplen la condición elegida.
    if opcion_a_filtrar == 1:
        while True:
            filtrar_continente = input(f"""Ingrese el continente a filtrar: 
                Las opciones son:
                - África
                - América
                - Asia
                - Europa
                - Oceanía
                """).strip().title()
            if filtrar_continente == "África":
                filtrar_continente = "Africa"
            elif filtrar_continente == "América":
                filtrar_continente = "America"
            elif filtrar_continente == "Oceanía":
                filtrar_continente = "Oceania"

            if filtrar_continente not in ["Africa", "America", "Asia", "Europa", "Oceania"]:
                print("La opción ingresada es inválida")
                continue
                       
            break 
        
        pais_encontrado = False
        print("Resultados del filtro:")
        print()
        for pais in paises:
            if pais["continente"] == filtrar_continente:
                pais_encontrado = True
                print(f"{pais['nombre']}")
        if pais_encontrado == False:
            print("No se encontraron países para el continente seleccionado")

    elif opcion_a_filtrar == 2:
        while True:
            try:
                poblacion_minima_filtro = int(input("Ingrese el valor de población mínima: "))
                poblacion_maxima_filtro = int(input("Ingrese el valor de población máxima: "))
                if poblacion_minima_filtro <= 0 or poblacion_maxima_filtro < poblacion_minima_filtro:
                    raise ValueError
            except ValueError:
                print("La opción ingresada es inválida. El número no puede ser cero ni la población mínima puede superar a la máxima. Intente nuevamente")
                continue
            break
        pais_encontrado = False
        print("Resultados del filtro:")
        print()
        for pais in paises:
            if poblacion_minima_filtro <= pais["poblacion"] <= poblacion_maxima_filtro:
                pais_encontrado = True
                print(f"{pais['nombre']} - Población: {pais['poblacion']}")
        if pais_encontrado == False:
            print("No se encontraron países para el rango filtrado")

    elif opcion_a_filtrar == 3:
        while True:
            try:
                superficie_minima_filtro = int(input("Ingrese el valor de superficie en km2 mínima: "))
                superficie_maxima_filtro = int(input("Ingrese el valor de superficie en km2 máxima: "))
                if superficie_minima_filtro <= 0 or superficie_maxima_filtro < superficie_minima_filtro:
                    raise ValueError
            except ValueError:
                print("La opción ingresada es inválida. El número no puede ser cero ni la superficie mínima puede superar a la máxima. Intente nuevamente")
                continue
            break
        pais_encontrado = False
        print("Resultados del filtro:")
        print()
        for pais in paises:
            if superficie_minima_filtro <= pais["superficie"] <= superficie_maxima_filtro:
                pais_encontrado = True
                print(f"{pais['nombre']} - Superficie: {pais['superficie']} km2")
        if pais_encontrado == False:
            print("No se encontraron países para el rango filtrado")

#Devuelve la población del país para utilizarla como criterio para ordenar.
def ordenar_por_poblacion(pais):
    return pais["poblacion"]

#Devuelve la superficie del país para utilizarla como criterio para ordenar.
def ordenar_por_superficie(pais):
    return pais["superficie"]

#Ordena los países por nombre, población o superficie.
def ordenar_paises(paises):
    while True:
        try:
            opcion_a_ordenar= int(input("""Ingrese el número correspondiente para seleccionar una opción: 
                1. Ordenar por nombre.
                2. Ordenar por población.
                3. Ordenar por superficie.
                : """))
            if opcion_a_ordenar not in (1, 2, 3):
                raise ValueError
            break
        except ValueError:
            print("La opción ingresada es inválida, intente nuevamente")
            continue
    
    if opcion_a_ordenar == 1:
        nombres_paises = []
        for pais in paises:
            nombres_paises.append(pais["nombre"])
        #Se utiliza sorted para devolver una nueva lista sin modificar la original. 
        paises_ordenados = sorted(nombres_paises)
        print("Países ordenados alfabéticamente:")
        print()
        for pais in paises_ordenados:
            print(f"País: {pais}")

    elif opcion_a_ordenar == 2:
        #Se utiliza key como parámetro para ordenar la lista según la población.
        poblacion_ordenada = sorted(paises, key=ordenar_por_poblacion)
        print("Países ordenados por población de menor a mayor:")
        print()
        for pais in poblacion_ordenada:
            print(f"País: {pais['nombre']} - Población: {pais['poblacion']}")

        print()
        print("Países ordenados por población de mayor a menor:")
        print()
        for pais in sorted(paises, key=ordenar_por_poblacion, reverse=True):
            print(f"País: {pais['nombre']} - Población: {pais['poblacion']}")

    elif opcion_a_ordenar == 3:
        #Se utiliza key como parámetro para ordenar la lista según la superficie.
        superficie_ordenada = sorted(paises, key=ordenar_por_superficie)
        print("Países ordenados por superficie de menor a mayor:")
        print()
        for pais in superficie_ordenada:
            print(f"País: {pais['nombre']} - Superficie: {pais['superficie']} km2")

        print()
        print("Países ordenados por superficie de mayor a menor:")
        print()
        for pais in sorted(paises, key=ordenar_por_superficie, reverse=True):
            print(f"País: {pais['nombre']} - Superficie: {pais['superficie']} km2")

#Calcula y muestra estadísticas utilizando los datos del CSV.
def estadisticas_paises(paises):
    while True:
        try:
            opcion_estadisticas= int(input("""Ingrese el número correspondiente para ver estadísticas: 
                1. País con mayor y menor población.
                2. Promedio de población entre los países cargados.
                3. Promedio de superficie entre los países cargados.
                4. Cantidad de países por continente.
                : """))
            if opcion_estadisticas not in (1, 2, 3, 4):
                raise ValueError
            break
        except ValueError:
            print("La opción ingresada es inválida, intente nuevamente")
            continue

    if opcion_estadisticas == 1:
        print("País con mayor población:")
        mayor_poblacion = sorted(paises, key=ordenar_por_poblacion, reverse=True)
        print(f"País: {mayor_poblacion[0]['nombre']} - Población: {mayor_poblacion[0]['poblacion']}")
        print()
        print("País con menor población:")
        menor_poblacion = sorted(paises, key=ordenar_por_poblacion)
        print(f"País: {menor_poblacion[0]['nombre']} - Población: {menor_poblacion[0]['poblacion']}")
    
    elif opcion_estadisticas == 2:
        #Acumula la población total para calcular el promedio.
        suma_poblacion = 0
        for pais in paises:
           suma_poblacion += pais["poblacion"]
        promedio_poblacion = suma_poblacion / len(paises)
        print(f"Promedio de población entre los países cargados: {promedio_poblacion:.2f}")

    elif opcion_estadisticas == 3:
        #Acumula la superficie total para calcular el promedio.
        suma_superficie = 0
        for pais in paises:
           suma_superficie += pais["superficie"]
        promedio_superficie = suma_superficie / len(paises)
        print(f"Promedio de superficie entre los países cargados: {promedio_superficie:.2f} km2")
    
    elif opcion_estadisticas == 4:
        #Contadores por continente para calcular cuantos países pertenecen a cada uno.
        paises_africa = 0
        paises_america = 0
        paises_asia = 0
        paises_europa = 0
        paises_oceania = 0
        for pais in paises:
            if pais["continente"] == "Africa":
                paises_africa+=1
            elif pais["continente"] == "America":
                paises_america+=1
            elif pais["continente"] == "Asia":
                paises_asia+=1
            elif pais["continente"] == "Europa":
                paises_europa+=1
            elif pais["continente"] == "Oceania":
                paises_oceania+=1
        print(f"""Cantidad de países por continente:
              África: {paises_africa}
              América: {paises_america}
              Asia: {paises_asia}
              Europa: {paises_europa}
              Oceanía: {paises_oceania}
              """)

main()