from servicios import * 
from archivos import * 
inventario = []
def menu () : 
    print("--------bienvenido---------")       
    check = True
    while check : 
        print("1. Crear producto \n2. actualizar  \n3. eliminar  \n4. mirar lista de productos \n5. calcular estadisticas \n6. cargar csv  \n7. guardar csv \n8. salir \n")
        try :
            select = int(input("elecciona: "))
        except : 
            print("opcion no valida") 
        if select == 1: 
            add(inventario) 
        elif select == 2: 
            update(inventario) 
        elif select == 3: 
            delete(inventario) 
        elif select == 4: 
            view(inventario) 
        elif select == 5: 
            calcularEstadistica(inventario)              
        elif select == 6:  
            cargarcsv()
        elif select == 7:    
            guardarcsv()
        elif select == 8: 
            break
            
 
menu()           