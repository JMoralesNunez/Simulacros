from funcionesGestion import *

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

Menu=True
students = {"4568": {"fullname": "Jhonatan Morales", "age":"17", "grade": 3.8},
            "4679": {"fullname": "Nicolas Vallejo", "age":"16", "grade": 4.5},
            "5412": {"fullname": "Manuel Ramirez", "age":"16", "grade": 3.5},
            "2418": {"fullname": "Juan Pupo", "age":"17", "grade": 2.7},
            "7488": {"fullname": "Manuela Cespedes", "age":"15", "grade": 2.9}
            }
while Menu:
    print("="*50)
    print("Bienvenido a tu base de datos!")
    print("1. Añade estudiantes")
    print("2. Busca un estudiante")
    print("3. Actualiza la información de un estudiante")
    print("4. Elimina un estudiante")
    print("5. Promedio de notas")
    print("6. Listar estudiantes con notas por debajo de 3.0")
    print("7. Salir")
    print("="*50)
    while True:
        option = input("Selecciona una opción: 1/2/3/4/5/6/7: ")
        if option.isdigit() and int(option) >= 1 and int(option) <=7:
            break
        else:
            print(WARNING+"Por favor ingresa una opción válida"+RESET)
    if option == "1":
        while True:
            while True:
                iD = input("Ingresa el ID del estudiante: ")
                if iD.isdigit() and int(iD) > 0 and iD not in students.keys():
                    break
                else:
                    print(WARNING+"ID inválido o ya registrado en la base de datos"+RESET)
            while True:
                name = input("Ingresa el nombre del estudiante: ")
                if name.isalpha():
                    break
                else:
                    print(WARNING+"Nombre inválido"+RESET)
            while True:
                lastname = input("Ingresa el apellido del estudiante: ")
                if lastname.isalpha():
                    break
                else:
                    print(WARNING+"Apellido inválido"+RESET)
            fullname = f"{name} {lastname}"
            while True:
                age = input("Ingresa la edad del estudiante: ")
                if age.isdigit() and int(age) > 0:
                    break
                else:
                    print(WARNING+"Edad inválida"+RESET)
            while True:
                try:
                    grade = float(input("Ingresa la nota del estudiante: "))
                    if grade >= 0.0 and grade <= 5.0:
                        break
                    else:
                        print(WARNING+"Nota inválida"+RESET)
                except:
                    print(WARNING+"Ingrese una nota valida"+RESET)
                
            add(iD,fullname,age,grade,students)
            while True:
                reset = input("¿Quieres añadir otro estudiante? ingresa un número 1.SI/2.NO: ")
                if reset.isdigit()==False:
                    print(WARNING+"Por favor ingresa una opción válida(1/2)"+RESET)
                elif int(reset) != 1 and int(reset) != 2:
                    print(WARNING+"Por favor ingresa una opción válida(1/2)"+RESET)
                else:
                    break
            if int(reset) == 2:
                break
    if option == "2":
        while True:
            search_method = input("¿Cómo quieres buscar al estudiante, por ID o por su nombre? 1.ID / 2.Nombre: ")
            if search_method.isdigit() and search_method == "1" or  search_method == "2":
                break
            else:
                print(WARNING+"Ingresa una opción válida"+RESET)
        if search_method == "1":
            while True:
                id_search = input("Ingresa el ID del estudiante: ")
                if id_search.isdigit() and int(id_search) > 0:
                    break
                else:
                    print(WARNING+"ID inválido"+RESET)
            Student=search_id(id_search, students)
        if search_method == "2":
            while True:
                name2 = input("Ingresa el nombre del estudiante: ")
                if name2.isalpha():
                    break
                else:
                    print(WARNING+"Nombre inválido"+RESET)
            while True:
                lastname2 = input("Ingresa el apellido del estudiante: ")
                if lastname2.isalpha():
                    break
                else:
                    print(WARNING+"Apellido inválido"+RESET)
            name_search = f"{name2} {lastname2}"
            search_name(name_search, students)
    if option == "3":
        while True:
            id_search = input("Ingresa el ID del estudiante al que deseas editar su información: ")
            if id_search.isdigit() and int(id_search) > 0 and id_search in students:
                break
            else:
                print(WARNING+"ID inválido o estudiante no encontrado en la base de datos"+RESET)
        while True:
            change = input("¿Qué deseas cambiar, su edad o su nota? 1.edad / 2.nota: ")
            if change.isdigit() and change == "1" or  change == "2":
                break
            else:
                print(WARNING+"Ingresa una opción válida"+RESET)
        if change == "1":
            while True:
                new_age = input("Ingresa la nueva edad del estudiante: ")
                if new_age.isdigit() and int(new_age) > 0:
                    break
                else:
                    print(WARNING+"Edad inválida"+RESET)
            update_age(id_search,new_age,students)
        if change == "2":
            while True:
                try:
                    new_grade = float(input("Ingresa la nueva nota del estudiante: "))
                    if new_grade >= 0.0 and new_grade <= 5.0:
                        break
                    else:
                        print(WARNING+"Nota inválida"+RESET)
                except:
                    print(WARNING+"Ingrese una nota valida"+RESET)
            update_grade(id_search,new_grade,students)
    if option == "4":
        for k,v in students.items():
            print(f"ID: {k}................ Nombre: {v["fullname"]} | Edad: {v["age"]} | Nota: {v["grade"]}")
            print("="*75)
        while True:
            delete_id = input("Ingresa el ID del estudiante que deseas eliminar: ")
            if delete_id.isdigit() and int(delete_id) > 0 and delete_id in students:
                break
            else:
                print(WARNING+"ID inválido o estudiante no encontrado en la base de datos"+RESET)
        delete(delete_id, students)
    if option == "5":
        promedio=average(students)
        if promedio >= 3.0:
            print(f"El promedio de los estudiantes es de: {SUCCESS}{promedio:.2f}"+RESET)
        else:
            print(f"El promedio de los estudiantes es de: {DANGER}{promedio:.2f}"+RESET)
    if option == "6":
        print("Estudiantes con notas por debajo de 3.0: ")
        below_average(students)
    if option == "7":
        print(SUCCESS+"Gracias por usar la base de datos"+RESET)
        Menu=False
