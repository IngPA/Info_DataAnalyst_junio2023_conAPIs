#  Hicimos una petición al servidor de httpbin.org,     metodo GET
#  con parametros enviados en un diccionario al  
# metodo get (params = diccionario).
# **Esta url nos devuelve un archivo Json**, 
# podemos pues llamar a un contenido mediante un diccionario:
 
import requests

if __name__=='__main__':
    url = 'https://httpbin.org/get'
    args ={ 'nombre':'Paola', 'curso':'Python', 'nivel':'Intermedio'}
    response = requests.get(url, params= args)

    if response.status_code == 200:
        #content = response.content
        response_json = response.json() #nos responde con un diccionario(formato json)
        origin = response_json['origin'] # utilizo metodo de diccionario para llamar al
        #valor de mi interes (origin es la clave, me trae el valor)
        print(origin)
        #print(content)

#devuelve el contenido de origin, que es el valor contenido en el key 'origin'
# Si utilizamos el modulo Json de Python, tendremos mas funcionalidades



