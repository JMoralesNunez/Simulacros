def add(id,name,age,grade, dict):
    info = {"fullname":name, "age":age, "grade":grade}
    dict[id]=info
    print(f"{name}, with id: {id}, has been successfully added!")

def search_id(id, dict):
    return dict.get(id)
    
def search_name(name,dict):
    for k,v in dict.items():
        if name == v["fullname"]:
            print("Estudiante encontrado:")
            print(f"{k}....... Nombre completo: {v["fullname"]} Edad: {v["age"]} Nota: {v["grade"]}")
            break
        else:
            print("Estudiante no encontrado")
            break