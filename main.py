from flask import Flask, render_template, request, session
from giphy_translation import translate_gif

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['inputText']
        giphyURL = translate_gif(text)
        # return render_template("form-action.html", giphy=giphyURL)
        return render_template("form.html", giphy=giphyURL)
        # session['gif'] = giphyURL
    else:
        # finalURL = session['gif']
        return render_template("form.html")

# @app.route('/', methods=['POST'])
# def index_post():
#     text = request.form['inputText']
#     giphyURL = translate_gif(text)
#     # return render_template("form-action.html", giphy=giphyURL)
#     session['giphyURL'] = giphyURL
#     return giphyURL

if __name__ == "__main__":
    app.run(debug=True)
