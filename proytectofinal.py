import json
import os
from datetime import datetime

#  cargar tareas
def cargar_tareas():
    if os.path.exists("tareas.json"):
        with open("tareas.json", "r") as file:
            return json.load(file)
    else:
        return {"pendientes": [], "completadas": []}

#  guardar las tareas 
def guardar_tareas(tareas):
    with open("tareas.json", "w") as file:
        json.dump(tareas, file)

# agregar una nueva tarea
def agregar_tarea(tareas):
    titulo = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha = input("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
    costo = float(input("Ingrese el costo de la tarea ($): "))
    nueva_tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha": fecha,
        "costo": costo,
        "completada": False
    }
    tareas["pendientes"].append(nueva_tarea)
    print("Tarea pendiente agregada exitosamente.")
    guardar_tareas(tareas)  
    guardar_en_archivo(nueva_tarea) 

#  guardar una nueva tarea 
def guardar_en_archivo(tarea):
    with open("C:\\Users\\joshu\\Downloads\\tareas.txt", "a") as file:
        file.write(f"Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Fecha: {tarea['fecha']}, Costo: ${tarea['costo']}\n")

#  ver las tareas pendientes o completadas
def ver_tareas(tareas, completadas=False):
    tipo = "Completadas" if completadas else "Pendientes"
    print(f"Tareas {tipo}:")
    lista_tareas = tareas["completadas" if completadas else "pendientes"]
    for tarea in lista_tareas:
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"Título: {tarea['titulo']}, Descripcion: {tarea['descripcion']}, Fecha: {tarea['fecha']}, Costo: ${tarea['costo']}, Estado: {estado}")

#  marcar una tarea como completada
def marcar_completada(tareas):
    ver_tareas(tareas)
    index = int(input("Ingrese el numero de la tarea que desea marcar como completada: ")) - 1
    tareas["pendientes"][index]["completada"] = True
    tareas["completadas"].append(tareas["pendientes"].pop(index))
    print("Tarea marcada como completada.")
    guardar_tareas(tareas)  # Guardar tareas después de marcar como completada

#  editar una tarea
def editar_tarea(tareas):
    ver_tareas(tareas)
    index = int(input("Ingrese el numero de la tarea que desea editar: ")) - 1
    tarea = tareas["pendientes"][index]
    tarea["titulo"] = input(f"Nuevo título ({tarea['titulo']}): ") or tarea["titulo"]
    tarea["descripcion"] = input(f"Nueva descripción ({tarea['descripcion']}): ") or tarea["descripcion"]
    tarea["fecha"] = input(f"Nueva fecha ({tarea['fecha']}): ") or tarea["fecha"]
    tarea["costo"] = float(input(f"Nuevo costo (${tarea['costo']}): ")) or tarea["costo"]
    print("Tarea editada exitosamente.")
    guardar_tareas(tareas)  # Guardar tareas después de editar

# borrar una tarea
def borrar_tarea(tareas):
    ver_tareas(tareas)
    index = int(input("Ingrese el numero de la tarea que desea borrar: ")) - 1
    del tareas["pendientes"][index]
    print("Tarea borrada exitosamente.")
    guardar_tareas(tareas)  # Guardar tareas después de borrar

# Menu
def main():
    tareas = cargar_tareas()
    while True:
        print("\nSeleccione una opcion del menu")
        print("1. Agregar Tarea")
        print("2. Ver Tareas Pendientes")
        print("3. Ver Tareas Completadas")
        print("4. Marcar Tarea como Completada")
        print("5. Editar Tarea")
        print("6. Borrar Tarea")
        print("7. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            ver_tareas(tareas, completadas=True)
        elif opcion == "4":
            marcar_completada(tareas)
        elif opcion == "5":
            editar_tarea(tareas)
        elif opcion == "6":
            borrar_tarea(tareas)
        elif opcion == "7":
            guardar_tareas(tareas)
            print("nos vemos")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opción valida.")

if __name__ == "__main__":
    main()

       

