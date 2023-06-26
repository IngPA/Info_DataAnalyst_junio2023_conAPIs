#  Creamos una petición al servidor de google.   metodo GET
# Además obtenemos los atributos de interes de esa respuesta. 

import requests

if __name__=='__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

# si el status devuelto es 200,  la solicitud ha tenido éxito y 
# la respuesta contiene los datos solicitados. 

# una vez que tenemos la respuesta que trajimos con GET,
# almacenada en una variable response, podemos obtener sus atributos: 
# .status_code (status HTTP), .content (contenido de la pg HTML), por ej: 
    if response.status_code == 200:
        print(response.content)

# de esta forma obtentemos el contenido de pg HTTML lo que podemos observar inspeccionandola. 
