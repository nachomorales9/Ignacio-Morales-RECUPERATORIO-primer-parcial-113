
import os
import json
import random

def get_path_actual(nombre_archivo):
    '''
    ruta del archivo del directorio actual

    Parameters:
    nombre_archivo (str): nombre del archivo

    Returns:
    str: ruta completa del archivo en el directorio actual
    '''
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_archivo_csv(archivo):
    '''
    carga csv y lo pasa a diccionario

    Parameters:
    archivo (str): nombre del archivo csv

    Returns:
    list: lista de diccionarios con los datos del archivo csv
    '''
    posts = []
    path = get_path_actual(archivo)
    if not os.path.exists(path):
        print(f"El archivo {archivo} no existe en la ruta {path}")
        return posts

    with open(path, 'r', encoding='utf-8') as archivo_csv:
        encabezados = archivo_csv.readline().strip().split(',')

        for linea in archivo_csv:
            valores = linea.strip().split(',')
            post = {encabezado: int(valor) if encabezado in ['id', 'likes', 'dislikes', 'followers'] else valor 
                    for encabezado, valor in zip(encabezados, valores)}
            posts.append(post)
    
    return posts


def filtrar_por_mejores_posts(posts):
    '''
    filtra los posts donde hay más de 2000 likes y los guarda en un archivo csv

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts

    Returns:
    str: nombre del archivo csv guardado con los mejores posts
    '''
    mejores_posts = []
    for post in posts:
        if post['likes'] > 2000:
            mejores_posts.append(post)
    
    nombre_archivo_csv = "mejores_posts.csv"

    with open(nombre_archivo_csv, 'w', encoding='utf-8') as archivo_csv:
        archivo_csv.write('id,user,likes,dislikes,followers\n')
        for post in mejores_posts:
            linea = f"{post['id']},{post['user']},{post['likes']},{post['dislikes']},{post['followers']}\n"
            archivo_csv.write(linea)
    
    return nombre_archivo_csv


def filtrar_por_haters(posts):
    '''
    filtra los posts donde hay más dislikes que likes y los guarda en un archivo csv

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts

    Returns:
    str: nombre del archivo csv guardado con los posts de haters
    '''
    haters_posts = []
    for post in posts:
        if post['dislikes'] > post['likes']:
            haters_posts.append(post)
    
    nombre_archivo = "haters_posts.csv"

    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_csv:
        archivo_csv.write('id,user,likes,dislikes,followers\n')

        for post in haters_posts:
            linea = f"{post['id']},{post['user']},{post['likes']},{post['dislikes']},{post['followers']}\n"
            archivo_csv.write(linea)
    
    return nombre_archivo

def imprimir_lista(posts):
    '''
    le pasas un parametro(posts) y te imprime la lista

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts
    '''
    for post in posts:
        print(f"ID: {post['id']}, User: {post['user']}, Likes: {post['likes']}, Dislikes: {post['dislikes']}, Followers: {post['followers']}")

def asignar_estadisticas(posts):
    '''
    se le da una estadistica a cada post

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts

    Returns:
    list: lista de diccionarios con los datos de los posts actualizados con estadísticas
    '''
    for post in posts:
        post['likes'] = random.randint(500, 3000)
        post['dislikes'] = random.randint(300, 3500)
        post['followers'] = random.randint(10000, 20000)
    return posts



def informar_promedio_followers(posts):
    '''
    calcula el total de followers y el promedio de followers de una lista de posts

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts
    '''
    total_followers = 0
    contador = len(posts)

    for post in posts:
        total_followers += post['followers']

    promedio = calcular_promedio(total_followers, contador)
    print(f"El promedio de followers es: {promedio}")

def ordenar_por_nombre(posts):
    '''
    ordena por orden ascendente el usuario y guarda en json

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts

    Returns:
    str: nombre del archivo json guardado con los posts ordenados
    '''
    posts_ordenados = sorted(posts, key=lambda x: x['user'])
    nombre_archivo = "posts_ordenados.json"
    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
        json.dump(posts_ordenados, archivo_json, ensure_ascii=False, indent=4)
    
    return nombre_archivo

def mostrar_mas_popular(posts):
    '''
    muestra el post más likeado

    Parameters:
    posts (list): lista de diccionarios con los datos de los posts
    '''
    max_likes = -1
    max_users = []
    for post in posts:
        if post['likes'] > max_likes:
            max_likes = post['likes']
            max_users = [post['user']]
        elif post['likes'] == max_likes:
            max_users.append(post['user'])

    if len(max_users) == 1:
        print(f"El usuario que más likes tiene ({max_likes}) es: {max_users[0]}")
    else:
        print(f"Los usuarios que más likes tienen ({max_likes}) son:")
        for user in max_users:
            print(user)

def calcular_promedio(a, b):
    '''
    se le pasan dos valores, los transforma a int y los promedia

    Parameters:
    a (int): primer valor
    b (int): segundo valor

    Returns:
    float: promedio de los dos valores
    '''
    return (a + b) / 2
