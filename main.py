from flask import Flask, render_template, request
from giphy_translation import translate_gif
from giphy_random import random_gif

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if "random" in request.form:
            giphyURL = random_gif()
            return render_template("form.html", giphy=giphyURL[0], source=giphyURL[1])
        else:
            text = request.form['inputText']

            # Changes spaces to dashes
            text = text.strip()
            if text.find(" ") != -1:
                text = text.replace(" ", "-")
            # DEBUGGING
            return render_template("form.html", text=text)

            # Checks if blank string is inputted
            if not text:
                error = "\u26A0\uFE0F Text input invalid, please try another."
                giphyURL = "https://media1.giphy.com/media/13NRvWtOiMXawM/200.gif"
                source = "https://giphy.com/gifs/things-13NRvWtOiMXawM"
                return render_template("form.html", giphy=giphyURL, error=error, source=source)
            else:
                # giphyURL = translate_gif(text)
                try:
                    giphyURL = translate_gif(text)
                except:
                    error = "\u26A0\uFE0F No GIFs found, please try another input."
                    giphyURL = "https://media1.giphy.com/media/13NRvWtOiMXawM/200.gif"
                    source = "https://giphy.com/gifs/things-13NRvWtOiMXawM"
                    return render_template("form.html", giphy=giphyURL, error=error, source=source)
                return render_template("form.html", giphy=giphyURL[0], source=giphyURL[1])
    else:
        # Default welcome gif is loaded
        giphyURL = "https://media2.giphy.com/media/l0MYC0LajbaPoEADu/200.gif"
        source = "https://giphy.com/gifs/welcome-austin-powers-dr-evil-l0MYC0LajbaPoEADu"
        return render_template("form.html", giphy=giphyURL, source=source)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
