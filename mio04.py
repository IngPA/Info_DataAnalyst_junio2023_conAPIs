#  Hicimos una petición al servidor de httpbin.org    metodo GET
# comparamos lo que nos devueve con lo que obtenemos al
# poner la url en la barra de direcciones del explorador. 
# No nos trae todo el contenido. 

# En la barra de direcciones del explorador, pruebo agregar 
#argumentos a la url, agregando un signo de interrogación y
#los argumentos a continnuación. De esta forma enviamos 
#los argumentos en el metodo GET,  a través de la url. 


import requests

if __name__=='__main__':
    url = 'https://httpbin.org/get? nombre=Paola & curso=Python'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        print(content)

#si comparamos esto con lo que nos devuelve ingresar
#la url en el buscador, veremos que corriendo este 
# codigo de python nos devuelve **menos** lineas. 
#entre las cuales, se incorporan loa argumentos que 
# enviamos (en args, en arl, por ej. )
# ESta no es la mejor forma de enviar parametros, ni la mas segura
# Existe otra forma...
