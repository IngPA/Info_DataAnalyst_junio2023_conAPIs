#Ejemplo pokeAPI de forma recursiva
#Teniendo la url, voy con el navegador a la pg 
# veo que devuelve un json, y estudio sus lineas.
# observo y decido buscar el atributo 'name'; al tener
# muchos campos, la api limita la descarga mediante el 
# atributo offset = 20 (pasandole una cantidad que limita la descarga)

# Haremos una función para ello, que obtenga los nombres de forma recursiva: 

  
import requests

def get_potkemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):  # creamos una función
    args = {'offset':offset} if offset else{}                               # creo la variable args, que toma el valor de offest, si offeset tiene valor, si no darle un valor vacio. 

    response = requests.get(url, params=args)                               # solo puedo acceder a información, por lo que se usa el metodo get, y los parametros url y args. 

    if response.status_code == 200:                                         # si el codigo http que devuelve la pg es 200 (respuesta adecuada)

        payload = response.json()                                           
        results = payload.get('results',[]) # con un get pido que me devuelva el contenido, o cree una lista vacia. 

        if results:                         # si la lista no esta vacia
            for pokemon in results:         # de cada poquemnon, guardo el nombre en una lista. 
                name = pokemon['name']
                print(name)                 # pido que me imprima la lista de nombres. 

            next = input("¿Continuar listando? [Y/N]").lower()
            if next == 'y':
                get_potkemons(offset=offset+20)

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    get_potkemons()

# Esto me devuelve una lista de 20 pokemon, y luego pregunta si quiero seguir listandolos. 


