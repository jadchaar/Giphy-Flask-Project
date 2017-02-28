from flask import Flask, render_template, request, Markup
from giphy_translation import translate_gif

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['inputText']
        # Changes spaces to dashes
        text = text.strip()
        if text.find(" ") != -1:
            text = text.replace(" ", "-")
        # Checks if blank string is inputted
        if not text:
            error = "Please input a valid gif name \U0001F642"
            giphyURL = "https://media1.giphy.com/media/13NRvWtOiMXawM/200.gif"
            return render_template("form.html", giphy=giphyURL, error = error)
        else:
            giphyURL = translate_gif(text)
            return render_template("form.html", giphy=giphyURL)
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
