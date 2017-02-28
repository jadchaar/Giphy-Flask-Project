from urllib.request import urlopen
import json
import webbrowser

def translate_gif(text):
    publicKey = "dc6zaTOxFJmzC"
    baseURL = "http://api.giphy.com/v1/gifs/translate"
    finalURL = baseURL + "?s=" + text + "&api_key=" + publicKey

    data = json.loads(urlopen(finalURL).read().decode('utf-8'))

    # return data["data"]["bitly_gif_url"]
    return data["data"]["images"]["fixed_height"]["url"]
