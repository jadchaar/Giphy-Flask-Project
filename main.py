from flask import Flask, render_template, request, session
from giphy_translation import translate_gif

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['inputText']
        # Changes spaces to dashes
        if text.find(" ") != -1:
            text = text.replace(" ", "-")
        # Checks if blank string is inputted
        if not text:
            # display error to re input string
        giphyURL = translate_gif(text)
        return render_template("form.html", giphy=giphyURL)
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
