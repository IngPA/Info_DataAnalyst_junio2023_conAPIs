#Ejemplo pokeAPI
#Teniendo la url, voy con el navegador a la pg
# veo que devuelve un json, y estudio sus lineas.
# observo y decido buscar el elemento name: 
  
import requests

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'

    response = requests.get(url)
    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results',[]) # con un get pido que me devuelva el contenido, o cree una lista vacia. 

        if results:                         # si la lista no esta vacia
            for pokemon in results:         # de cada poquemnon, guardo el nombre en una lista. 
                name = pokemon['name']
                print(name)                 # pido que me imprima la lista de nombres. 

# Esto me devuelve una lista de 20 pokemon. 
# Resulta que hay muchos pokemon, la pg lista 913, pero no podemos listar todos de una vez
# La API permite instarlos de a poco en poco, mediante un atributo llamado offset, y pasandole la cantidad (20)
# (puedo ver este atributo y su valor asociado entrando al buscador la url)

