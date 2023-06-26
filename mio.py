#  Creamos una petición al servidor de google.   metodo GET
import requests

if __name__=='__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

    print(response)

#
# El codigo que devuelve la consulta corresponde al status de 
# la peticion, en valores de status HTTP. 

# si el status devuelto es 200,  la solicitud ha tenido éxito y 
# la respuesta contiene los datos solicitados.

