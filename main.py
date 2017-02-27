from flask import Flask, render_template, request, Markup
from giphy_translation import translate_gif
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['inputText']
    giphyURL = translate_gif(text)
    # publicKey = "dc6zaTOxFJmzC"
    # baseURL = "http://api.giphy.com/v1/gifs/translate"
    # finalURL = baseURL + "?s=" + text + "&api_key=" + publicKey
    #
    # data = json.loads(urlopen(finalURL).read().decode('utf-8'))
    #
    # giphyURL = data["data"]["bitly_gif_url"]
    return render_template("form-action.html", giphy=Markup(giphyURL))

# webbrowser.open("http://127.0.0.1:5000/", new=2, autoraise=True)

if __name__ == "__main__":
    app.run(debug=True)
