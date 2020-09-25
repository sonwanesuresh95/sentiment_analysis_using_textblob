from flask import Flask, request, render_template
from textblob import TextBlob
import re

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    orig_text = request.form['text']
    text = orig_text.lower()
    text = re.sub(r'[^a-zA-Z]+', ' ', text)
    text = re.sub(r'[^\w\s]+', ' ', text)
    tb = TextBlob(text)
    sentiment = 'Negative'
    subj = 'Fact'
    polarity, subjectivity = tb.sentiment[0], tb.sentiment[1]
    if polarity >= 0.5:
        sentiment = 'Positive'
    if subjectivity >= 0.5:
        subj = 'Opinion'
    return render_template('index.html',sentiment=sentiment, subj=subj, orig_text=orig_text, polarity=polarity, subjectivity=subjectivity)


if __name__ == '__main__':
    app.run()