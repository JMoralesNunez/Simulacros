def add(id,name,age,grade, dict):
    info = {"fullname":name, "age":age, "grade":grade}
    dict[id]=info
    print(f"{name}, with id: {id}, has been successfully added!")

def search_id(id, dict):
    format=dict.get(id)
    if format == None:
        print("Estudiante no encontrado")
    else:
        print("Nombre Completo: {fullname}, Edad: {age}, Nota: {grade}".format_map(format))
    
def search_name(name,dict):
    for k,v in dict.items():
        if name == v["fullname"]:
            print("Estudiante encontrado:")
            print(f"ID: {k}....... Nombre completo: {v["fullname"]} Edad: {v["age"]} Nota: {v["grade"]}")
            break
        else:
            print("Estudiante no encontrado")
            break

def update_age(id, age, dict):
    dict[id]["age"]=age
    format=dict.get(id)
    print("Cambio realizado exitosamente!")
    print("Nombre Completo: {fullname}, Edad: {age}, Nota: {grade}".format_map(format))

def update_grade(id, grade, dict):
    dict[id]["grade"]=grade
    format=dict.get(id)
    print("Cambio realizado exitosamente!")
    print("Nombre Completo: {fullname}, Edad: {age}, Nota: {grade}".format_map(format))
