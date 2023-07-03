# Chunks    -Veremos un michi_
"""
"Chunks" es un término utilizado en el contexto de la transferencia de datos a través de HTTP. 
"Chunks" se refiere a la técnica de dividir una respuesta HTTP en partes más pequeñas 
llamadas "chunks" y enviarlas secuencialmente en lugar de enviar la respuesta completa 
de una vez. Esto permite una entrega continua y eficiente de datos, especialmente en 
casos de transmisión en tiempo real o transferencias de archivos grandes.

Cuando realizamos una petición a un servidor, lo que hace la libreria es
realizar la peticion por el metodo que escogimos, obtener el contenido y 
posteriormente cerrar la conexión.
Pero para descargar un archivo grande, una imagen en este caso, querremos 
mantener la conexion abierta para posteriormente poder descargar el archivo. 

Poniendo el parametro stream en True, la conexión queda abierta
Luego la cerramos en nuestro codigo con respoonse.closer()

La petición de informacion la realizamos mediante iteraciones. 
"""

import requests

if __name__== '__main__':
    url = 'http://i.imgur.com/n9z3sLg.jpg'
    response = requests.get(url,stream=True) #realliza la peticion sin descargar el contenido
    with open('image.jpg','wb') as file: 
        for chunk in response.iter_content(): #descarga el contenido poco a poco. 
            file.write(chunk)
    response.close()
# Al ejecutarse vemos que crea un archivo, y que tarda un poco. 
# Al final, abriendo el archivo, vemos al michi :)
