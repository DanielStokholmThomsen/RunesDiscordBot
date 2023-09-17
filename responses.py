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
    text = str(message.content).lower()
    if text == 'hvad har rune?':
        return 'En kæmpe stor ladvogn'
    if text == 'test':
        return 'Trussen'
    if text == "hunde fact":
        return GetRandomDogFact()
    if text == "image":
        return
    if str(text).startswith("pokemon"):
        pokemon = str(text).split()[1]
        return GetPokemonFact(pokemon)
    if text == 'help':
        'The following commands are available:'
    return "I'm not able to understand that request yet. Try 'help' for help"


