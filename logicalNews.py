import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from newsExtractor import getNewsTitles

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_news():
    speech_text = "Hello, you can query like 'Ask, Logical Indian for News'"
    return statement(speech_text).simple_card('Hello', speech_text)

@ask.intent("ShortLatestNews")
def short_latest_news():
    shortNews = getNewsTitles(5)
    return statement(shortNews)

if __name__=='__main__':
    app.run(debug=True)
