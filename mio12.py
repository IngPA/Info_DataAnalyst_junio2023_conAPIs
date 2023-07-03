#    metodo POST - encabezados
# El servidor tambien necesita enviar encabezados, y 
# como clientes podemos leerlos, mediante response.headers 

#  Haremos una petición al servidor de httpbin.org, 
# **La url httpbin.org nos devuelve un archivo Json**, que vamos a utilizar con él el modulo Json de Python. 
 
import requests
import json

if __name__=='__main__':
    url = 'https://httpbin.org/post' 

    # para el metodo post el diccionario que lleva los datos a data, lo llamamos 'payload'
    payload ={ 'nombre':'Paola', 
              'curso':'Python', 
              'nivel':'Intermedio'} #pasamos argumentos en un diccionario
    
    # Para el encabezado agregamos el diccionario 'headeres':
    headers = { 'Content-Type': 'application/json', 
               'access-token' : '12345' }

    # Dentro del request pasamos los diccionario como objetos de json
    response = requests.post(url, data = json.dumps(payload), headers= headers)  #utilizamos post para esta consulta ya que enviamos datos. 

    print(response.url)
    print(response.status_code)
    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers  # esto nos devuelve un diccionario. 
        print(headers_response)

# En la respuesta vemos el contenido de headers que envia el servidor, donde estan algunos valores del diccionario que le enviamos. 
#  'access-token' : '12345' no está
# Una vez que veo el headers que envia el servidor, puedo acceder a sus valores, por ej, puedo acceder a 'Server'
# Cómo lo hago?:
        server = headers_response['Server'] # tomo el valor del diccionario en una variable
        print(server)
#       