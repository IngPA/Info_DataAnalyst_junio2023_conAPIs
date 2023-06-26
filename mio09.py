#    metodo POST
#  Con este metodo no se puede pasar información desde el navegador, si no desde un programa (nuestro script)

#  Haremos una petición al servidor de httpbin.org, 
#  Con el metodo POST vamos a crear un recurso dentro del servidor, con GET lo obteniamos. 
# con el metodo get enviamos los parametros dentro de la url.
#  con post vamos a enviar parametros dentro de un atributo. 

# **La url httpbin.org nos devuelve un archivo Json**, que vamos a utilizar con él el modulo Json de Python. 
 
import requests
import json

if __name__=='__main__':
    url = 'https://httpbin.org/post' #ponemos post en la url
    #para el metodo post el diccionario lo llamamos 'payload'
    payload ={ 'nombre':'Paola', 'curso':'Python', 'nivel':'Intermedio'} #pasamos argumentos en un diccionario
    
    #dentro del request pasamos el diccionario a objeto json (lo serializamos)
    response = requests.post(url, json=payload)  #utilizamos post para esta consulta

    # podriamos enviar estos parametros al atributo data
    # response = request.post(url, data=payload) #--> devolvera los parametros en el atributo 'form'

    # podriamos enviar estos parametros al atributo data, convirtiendolo a json (serializandolo)
    # response = request.post(url, data=json.dumps(payload)) #--> devolvera los parametros en el atributo 'data'


    if response.status_code == 200:
        print(response.content)

# Si observamos el contenido de la respuesta, vemos que visualizamos mas valores que con cuando utilizamos GET
# y además los parametros ahora se encuentran en el atributo "data"

# podemos ademas decir, que si enviamos el diccionario como json, el modulo json post se encarga de serializarlo. 
# si enviamos el diccionario a data, debemos serializar nosotros el diccionario. 
