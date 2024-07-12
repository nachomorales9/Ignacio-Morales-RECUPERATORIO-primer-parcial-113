from funciones import *

def mostrar_menu():
    """
    Muestra el menú de opciones del programa.
    """
    print("\nMenú de Opciones:")
    print("1) Cargar archivo CSV")
    print("2) Imprimir lista")
    print("3) Asignar estadísticas")
    print("4) Filtrar por mejores posts")
    print("5) Filtrar por haters")
    print("6) Informar promedio de followers")
    print("7) Ordenar los datos por nombre de usuario en orden ascendente")
    print("8) Mostrar más popular")
    print("9) Salir")

def menu_principal():
    posts = []
    archivo_cargado = False
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if not archivo_cargado and opcion != '1' and opcion != '9':
            print("Debe cargar un archivo CSV antes de realizar cualquier otra acción.")
            continue

        match opcion:
            case '1':
                archivo = input("Ingrese el nombre del archivo CSV: ")
                posts = cargar_archivo_csv(archivo)
                if posts:
                    archivo_cargado = True
            case '2':
                imprimir_lista(posts)
            case '3':
                posts = asignar_estadisticas(posts)
                imprimir_lista(posts)
            case '4':
                nombre_archivo = filtrar_por_mejores_posts(posts)
                print(f"Archivo guardado como {nombre_archivo}")
            case '5':
                nombre_archivo = filtrar_por_haters(posts)
                print(f"Archivo guardado como {nombre_archivo}")
            case '6':
                informar_promedio_followers(posts)
            case '7':
                nombre_archivo = ordenar_por_nombre(posts)
                print(f"Archivo guardado como {nombre_archivo}")
            case '8':
                mostrar_mas_popular(posts)
            case '9':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()
