from urllib.request import urlopen
import json
import sys


def translate_gif(text):
    publicKey = "dc6zaTOxFJmzC"
    baseURL = "https://api.giphy.com/v1/gifs/translate?s="
    finalURL = baseURL + text + "&api_key=" + publicKey

    data = json.loads(urlopen(finalURL).read().decode('utf-8'))

    dataArray = [data["data"]["images"][
        "original"]["url"], data["data"]["url"]]

    return dataArray
