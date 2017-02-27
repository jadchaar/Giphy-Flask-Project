from urllib.request import urlopen
import json
import webbrowser

def translate_gif(text):
    # userTranslation = input("Type in a phrase to view a relevant gif: ");

    publicKey = "dc6zaTOxFJmzC"
    baseURL = "http://api.giphy.com/v1/gifs/translate"
    # finalURL = baseURL + "?s=" + userTranslation + "&api_key=" + publicKey
    finalURL = baseURL + "?s=" + text + "&api_key=" + publicKey

    data = json.loads(urlopen(finalURL).read().decode('utf-8'))

    # print(json.dumps(data, sort_keys=True, indent=4))

    # giphyURL = data["data"]["bitly_gif_url"]

    # print(giphyURL)

    # webbrowser.open(giphyURL, new=2, autoraise=True)

    return data["data"]["bitly_gif_url"]
