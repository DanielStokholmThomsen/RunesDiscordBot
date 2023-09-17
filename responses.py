import requests
def GetRandomDogFact():
    x = requests.get('http://dog-api.kinduff.com/api/facts')
    jsonResponse = x.json()
    return jsonResponse["facts"]


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

