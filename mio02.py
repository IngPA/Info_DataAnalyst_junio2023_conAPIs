#  Creamos una petición al servidor de google.   metodo GET
# obtenemos los atributos de interes de esa respuesta, 
# y los guardamos en un archivo. 

import requests

if __name__=='__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

# si el status devuelto es 200,  la solicitud ha tenido éxito y 
# la respuesta contiene los datos solicitados. 

# una vez que tenemos la respuesta que trajimos con GET, 
# almacenada en una variable response, podemos 
# obtener su contenido HTML usando el atributo '.content'  (1)
# guardar ese contenido en una variable 'contenido'        (2)
# abrir/crear un archivo para guardarlo                    (3)
# cargarle el contenido del HTML, y cerrarlo...

    if response.status_code == 200:
        content = response.content                        #(1)(2)
        file = open('google.html','wb')                   #(3)
        file.write(content)
        file.close()

# de esta forma obtentemos el contenido de pg HTTML en un archivo 'google.html'. 
