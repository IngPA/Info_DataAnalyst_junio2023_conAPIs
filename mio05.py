#  Hicimos una petición al servidor de httpbin.org, y    metodo GET
# le agregamos parametros en la barra de direcciones. 

# vemos que en la respuesta figuran los parametros
# enviados mediante la url (se puede ver en la url)

# Además, continua siendo distinto lo que 
# obtenemos al ejecutar el programa de python, con lo 
# obtenido al poner la url en la barra de direcciones 
# del explorador (más contenido en el ultimo). 

# Proemos ENVIAR PARAMETROS DE FORMA DINAMICA: 
# para ello trabajamos con un diccionario, con el que 
# pasaremos los argumentoes al metodo get, mediante
# params = diccionario. 
 
import requests

if __name__=='__main__':
    url = 'https://httpbin.org/get'
    args ={ 'nombre':'Paola', 'curso':'Python', 'nivel':'Intermedio'}
    response = requests.get(url, params= args)

    if response.status_code == 200:
        content = response.content
        print(content)

# el que en la respuesta que obtenemos se ven los 
# paraamtros enviados, gestionados internamente por get. 
# o sea, obtenemos los mismos resultados que enviando 
# la información por la url, pero no lo escribimos 
# directamente en la url.

#Veamos como se compone la url
print('Url contruido por el metodo get:')
print(response.url)

