import os
import csv


def guardarcsv(guardar="guardar.csv"):
    from app import inventario
    os.makedirs("DataBase", exist_ok=True)
    rutacsv=os.path.join("DataBase",guardar)

    with open(rutacsv,"w",newline="",encoding="utf-8") as archivo:
        write=csv.DictWriter(archivo,fieldnames=inventario[0].keys())
        write.writeheader()
        write.writerows(inventario)
        print("Guardado correctamente")
        return
    
def cargarcsv(guardar="guardar.csv"):
    from app import inventario

    os.makedirs("DataBase", exist_ok=True)
    rutacsv=os.path.join("DataBase",guardar)

    with open(rutacsv, "r", newline="", encoding="utf-8") as archivo:
        read= csv.DictReader(archivo)
        print("si no sobre escribe el inventario se remplazara el producto con el mismo nombre guardado en el csv")
        usuario = input("Quieres sobre escribir el inventario actual:(s/n) ") 
        if usuario == "s": 
            inventario.clear()
            for fila in read:
                producto = {
                    "Nombre": fila.get("Nombre"),
                    "Precio": float(fila.get("Precio", 0)),
                    "Cantidad": int(fila.get("Cantidad", 0))
                }
                inventario.append(producto)
                print(producto)
        if usuario == "n": 
            new_invenario = []
            for fila in read:
                producto = {
                    "Nombre": fila.get("Nombre"),
                    "Precio": float(fila.get("Precio", 0)),
                    "Cantidad": int(fila.get("Cantidad", 0))
                }
                new_invenario.append(producto) 
            nombres_existentes = set(p['Nombre'] for p in new_invenario) 
            productos_add = 0
            productos_repetidos = 0
            for p in inventario : 
                if p['Nombre']  in nombres_existentes: 
                    inventario.remove(p) 
                    productos_repetidos += 1
                else : 
                    productos_add += 1
            inventario.extend(new_invenario)
            print(f"productos añadidos {productos_add} | productos repetidos {productos_repetidos}") 
                    
            


    
