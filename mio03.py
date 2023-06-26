#  Creamos una petición al servidor de httpbin.org .   metodo GET

import requests

if __name__=='__main__':
    url = 'https://httpbin.org/get'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        print(content)

#si comparamos esto con lo que nos devuelve ingresar
#la url en el buscador, veremos que corriendo este 
# codigo de python nos devuelve **menos** lineas. 

