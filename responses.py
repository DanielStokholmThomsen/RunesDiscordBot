import requests
def GetRandomDogFact():
    x = requests.get('http://dog-api.kinduff.com/api/facts')
    jsonResponse = x.json()
    return jsonResponse["facts"]

def GetPokemonFact(pokemon):
    x = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}')
    jsonResponse = x.json()
    vægt =int(jsonResponse["weight"])
    gennemsnitrunenumse = 30
    return f'Denne pokemon vejer {vægt} kg, det svarer til {vægt/gennemsnitrunenumse} gange runes numse'

def handle_response(message) -> str:
    text = message.content
    if text == 'Hvad har Rune?':
        return 'En kæmpe stor ladvogn'
    if text == 'Test':
        return 'Trussen'
    if text == "Hunde fact":
        return GetRandomDogFact()
    if text == "Image":
        return
    if str(text).startswith("Pokemon"):
        pokemon = str(text).split()[1]
        return GetPokemonFact(pokemon)
    return "I'm not able to understand that request yet. Try '?' for help"


