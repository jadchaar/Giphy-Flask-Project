from urllib.request import urlopen
import json, sys

def translate_gif(text):
    publicKey = "dc6zaTOxFJmzC"
    baseURL = "http://api.giphy.com/v1/gifs/translate"
    finalURL = baseURL + "?s=" + text + "&api_key=" + publicKey

    data = json.loads(urlopen(finalURL).read().decode('utf-8'))

    dataArray = [data["data"]["images"]["original"]["url"], data["data"]["url"]]

    return dataArray
