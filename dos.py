notas = [{"dni":"29915165","codigo":"MAT01234","nota":"15","periodo": "1-2023"},
       {"dni":"29915165","codigo":"MAT00123","nota":"17","periodo": "2-2023"},
       {"dni":"13890908","codigo":"MAT01234","nota":"15","periodo": "1-2023"},
       {"dni":"13890908","codigo":"MAT00123","nota":"17","periodo": "2-2023"}
       ] 
    
estudiantes = [{"dni":"29915165","nombre":"Anjiver","apellido":"Vasquez"},
       {"dni":"13890908","nombre":"Ana","apellido":"Herrera"}]

materias = [{"codigo":"MAT01234","nombre":"Anjiver","uc":"3"},
       {"codigo":"MAT01234","nombre":"Ana","uc":"3"},
       {"codigo":"MAT00123","nombre":"Anjiver", "uc":"4"},
       {"codigo":"MAT00123","nombre":"Ana","uc":"4"}]
#definición de notas, estudiantes y materias (contiene la información variada de estudiantes)

def nombre(dni): #definición de la función nombre
    for item in estudiantes: #recorre la lista de estudiantes
        if item["dni"]== dni: #si coincide con el numero de cedula actual
            return item["nombre"] #retorna el nombre del estudiante
        
def apellido(dni):
    for item in estudiantes:
        if item["dni"]== dni:
            return item["apellido"]
    
def periodo(dni): #definicion de periodo
    periodos = [] #inicia la lista
    for item in notas: #recorre la lista
        if item["dni"]== dni: #coincidencia del numero de cedula
            periodos.append(item["periodo"]) #se agrega el periodo 
    return periodos #retornar

def promedio():
    cedula = input("Ingrese el número de cédula: ")
    nota = 0
    ucs = 0

    for item in notas:
        if item["dni"] == cedula:
            for row in materias:
                if row["codigo"] == item["codigo"]: #evaluacion del codigo de la materia si coincide con el nuevo
                    nota += int(item["nota"]) * int(row["uc"])
                    ucs += int(row["uc"]) #calculos

    if ucs != 0: #verificacion si el estudiante ha pasado materias
        promedio = nota / ucs #calculo del promedio
        nombre_estudiante = nombre(cedula)
        print(f"El promedio de {nombre_estudiante} es de: {promedio:.2f}")
    else: # si no 
        print("No se encontraron notas para el estudiante con esa cédula.") #impresion de mensaje al usuario

def agregar_estudiante(): #definicion de la funcion
    #solicitud de datos para el registro
    dni = input("Ingrese el número de cédula del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")

    estudiantes.append({"dni": dni, "nombre": nombre, "apellido": apellido}) #creacion del nuevo registro (diccionario)
    #solicitudes para ingresar los datos del estudiante nuevo
    codigo = input("Ingrese el código de la materia: ")
    nota = input("Ingrese la nota de la materia: ")
    periodo = input("Ingrese el período de la materia (ej. 1-2023): ")
    uc = input("Ingrese las unidades de crédito de la materia: ")

    notas.append({"dni": dni, "codigo": codigo, "nota": nota, "periodo": periodo}) #creacion del nuevo registro de informacion (diccionario)

    if not any(materia["codigo"] == codigo for materia in materias): #verifica si existe una meteria con el codigo ingresado en la lista
        materias.append({"codigo": codigo, "nombre": nombre, "uc": uc})

def eliminar_estudiante():
    dni = input("Ingrese el número de cédula del estudiante a eliminar: ")
    
    estudiantes[:] = [estudiante for estudiante in estudiantes if estudiante.get("dni") != dni] #creacion de nueva lista eliminando el seleccionado para eliminar
    
    notas[:] = [nota for nota in notas if nota.get("dni") != dni] #eliminar notas del seleccionado (eliminacion de informacion)