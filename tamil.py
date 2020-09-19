import stanza
from spacy_stanza import StanzaLanguage
from spacy import displacy
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import streamlit as st
import spacy_streamlit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ohmraj!'
bootstrap = Bootstrap(app)

snlp = stanza.Pipeline(lang="ta")
nlp = StanzaLanguage(snlp)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    a = []
    text = request.form['text']
    doc = nlp(text)
    for token in doc:
        a.append(token.text)
        a.append(token.lemma)
        a.append(token.pos_)
        a.append(token.dep_)
        a.append(token.ent_type_)
        # print(token.text, token.lemma_, token.pos_, token.dep_, token.ent_type_)

    return render_template('my-form.html', the_title='home', table=a)


# input_text = input("Enter the sentence to be analysed:")

# doc = nlp("2020 இல் ஷெஃபீல்ட் தமிழ் சங்கம் சிறப்பாக இயங்குகிறது.")


# Visualize dependencies
# displacy.serve(doc, port=5001)

if __name__ == '__main__':
    app.run(debug=True)
