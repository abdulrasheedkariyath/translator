from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['language']
        translation = translate_text(text_to_translate, target_language)
    return render_template('index.html', translation=translation)

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

if __name__ == '__main__':
    app.run(debug=True)
