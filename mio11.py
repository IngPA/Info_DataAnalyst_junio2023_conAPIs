#    metodo POST - encabezados
#  Con este metodo no se puede pasar información desde el navegador, si no desde un programa (nuestro script)
# Tanto cliente como servidor deben enviar encabezados, para una correcta comunicación. 
# Cuando programamos podemos mandar datos en los encabezados.
# No queremos mandar datos importantes en url, o en los parmetros, por seguridad. 
# Para trabajar los encabezados se usan diccionarios. 

#  Haremos una petición al servidor de httpbin.org, 
# **La url httpbin.org nos devuelve un archivo Json**, que vamos a utilizar con él el modulo Json de Python. 
 
import requests
import json

if __name__=='__main__':
    url = 'https://httpbin.org/post' 
    # para el metodo post el diccionario que lleva los datos a data, lo llamamos 'payload'
    payload ={ 'nombre':'Paola', 'curso':'Python', 'nivel':'Intermedio'} #pasamos argumentos en un diccionario
    # Para el encabezado agregamos el diccionario 'headeres':
    headers = { 'Content-Type': 'application/json', 'access-token' : '12345' }

    # Dentro del request pasamos los diccionario como objetos de json
    response = requests.post(url, data = json.dumps(payload), headers= headers)  #utilizamos post para esta consulta ya que enviamos datos. 

    print(response.url)
    print(response.status_code)
    if response.status_code == 200:
        print(response.content)

# Si observamos el contenido de la respuesta, vemos los valores enviados en headers, y los enviados en data. 