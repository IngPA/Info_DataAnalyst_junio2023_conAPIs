#    metodo PUT & DELETE
#DELETE
# put permitirá actualizar un recuso del Servidor
# delete permitira borrar un recurso del Servidor

#  Haremos una petición al servidor de httpbin.org, en su slach delete
# **La url httpbin.org nos devuelve un archivo Json**, que vamos a utilizar con él el modulo Json de Python. 
# cambiamos la url a slach delete, y el metodo request a request.delete y ejecutamos
 
import requests
import json

if __name__=='__main__':
    url = 'https://httpbin.org/delete' 

    # para el metodo post el diccionario que lleva los datos a data, lo llamamos 'payload'
    payload ={ 'nombre':'Paola', 
              'curso':'Python', 
              'nivel':'Intermedio'} #pasamos argumentos en un diccionario
    
    # Para el encabezado agregamos el diccionario 'headeres':
    headers = { 'Content-Type': 'application/json', 
               'access-token' : '12345' }

    # Dentro del request pasamos los diccionario como objetos de json
    response = requests.delete(url, data = json.dumps(payload), headers= headers)  #utilizamos post para esta consulta ya que enviamos datos. 

    print(response.url)
    #print(response.status_code)
    if response.status_code == 200:
        headers_response = response.headers  # esto nos devuelve un diccionario. 
        print(headers_response)
        server = headers_response['Server'] # tomo el valor del diccionario en una variable
        print(server)
        #investigo un poco más ¿que me da el header del servidor con put?
        print(headers_response)
        # encontraré en la respuesta lo enviado en data?
        print(response.content)
# compruebo al cambiar put por delete que no ocurre gran cosa (no se ven cambios en lo que retorna)
# entonces como usarlo? qué está ocurriendo?