#  Hicimos una petición al servidor de httpbin.org,     metodo GET
#  con parametros enviados en un diccionario al metodo get (params = diccionario).

# **Esta url nos devuelve un archivo Json**, 
# Podemos utilizar con él el modulo Json de Python. 
 
import requests
import json

if __name__=='__main__':
    url = 'https://httpbin.org/get'
    args ={ 'nombre':'Paola', 'curso':'Python', 'nivel':'Intermedio'}
    
    response = requests.get(url, params= args)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)

# Utilizamos el modulo Json de Python, llamamos los valores con las key del dicc.
# #devuelve el contenido de origin, que es el valor contenido en el key 'origin'

#es una forma de trabajar los objetos json que el servidor envie. 




