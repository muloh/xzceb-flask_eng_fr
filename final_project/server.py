from machinetranslation import translator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = language_translator.translate(text=textToTranslate, model_id='en-fr').get_result()
    translated_text = french_text['translations'][0]['translation']
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = language_translator.translate(text=textToTranslate, model_id='fr-en').get_result()
    translated_text = french_text['translations'][0]['translation']
    return translated_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    texted = "Welcome Home"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
