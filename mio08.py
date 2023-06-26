#    metodo POST
#  Haremos una petición al servidor de httpbin.org, 
#  Con el metodo POST vamos a crear un recurso dentro del servidor, 
#  Con este metodo no se puede pasar información desde el navegador, si no desde un programa (nuestro script)
# **La url httpbin.org nos devuelve un archivo Json**, que vamos a utilizar con él el modulo Json de Python. 
 
import requests
import json

if __name__=='__main__':
    url = 'https://httpbin.org/post' #ponemos post en la url
    args ={ 'nombre':'Paola', 'curso':'Python', 'nivel':'Intermedio'} #pasamos argumentos en un diccionario
    
    response = requests.post(url, params= args)  #utilizamos post para esta consulta

    if response.status_code == 200:
        print(response.content)

# Si observamos el contenido de la respuesta, vemos que visualizamos mas valores que con cuando utilizamos GET
# al igual que con get, los datos estan guardados en "args"
