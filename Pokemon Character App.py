import requests

name=input("Enter the name of the pokemon you want to search for: ")
name=name.lower()
req=requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")

if(req.status_code==200):
    pokemon = req.json()
    print(f"Name\t\t{pokemon['name']}")
    print()
    print("Abilities:\t\t")
    for x in pokemon['abilities']:
        print(x['ability']['name'])
    print()
    print(f"Base Experience\t\t{pokemon['base_experience']}")
else:
    print("Pokemon not found")
