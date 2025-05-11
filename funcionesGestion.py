DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

def add(id,name,age,grade, dict):
    info = {"fullname":name, "age":age, "grade":grade}
    dict[id]=info
    print(SUCCESS+f"{name}, con ID: {id}, ha sido añadido exitosamente!"+RESET)

def search_id(id, dict):
    format=dict.get(id)
    if format == None:
        print(DANGER+"Estudiante no encontrado"+RESET)
    else:
        print(SUCCESS+"Nombre Completo: {fullname}, Edad: {age}, Nota: {grade}".format_map(format)+RESET)
    
def search_name(name,dict):
    for v in dict.values():
        if name in v["fullname"]:
            print(SUCCESS+"Estudiante encontrado:"+RESET)
            print(f"Nombre completo: {v["fullname"]} Edad: {v["age"]} Nota: {v["grade"]}")
            print("="*50)
        else:
            continue

def update_age(id, age, dict):
    dict[id]["age"]=age
    format=dict.get(id)
    print(SUCCESS+"Cambio realizado exitosamente!"+RESET)
    print("Nombre Completo: {fullname}, Edad: {age}, Nota: {grade}".format_map(format))

def update_grade(id, grade, dict):
    dict[id]["grade"]=grade
    format=dict.get(id)
    print(SUCCESS+"Cambio realizado exitosamente!"+RESET)
    print("Nombre Completo: {fullname}, Edad: {age}, Nota: {grade}".format_map(format))
    
def delete(id, dict): 
    dict.pop(id)
    print(SUCCESS+f"{id} ha sido eliminado exitosamente"+RESET)

def average(dict):
    promedio = []
    for v in dict.values():
        promedio.append(v["grade"])
    promedio = sum(promedio)/len(promedio)
    return promedio

def below_average(dict):
    below = {}
    for k,v in dict.items():
        if v["grade"] < 3.0:
            below[k] = v
    for k,v in below.items():
        print(f"Nombre: {v['fullname']}, Edad: {v['age']}, Nota: {v['grade']}")
