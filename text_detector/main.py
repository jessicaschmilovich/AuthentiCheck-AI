import os
import requests
from mltext import classifyText, storeText
from mlmodel import trainModel, checkModel
from flask import Flask, request


def process(test_text):
  s = "<b>text:</b>&nbsp;" + test_text + "</br>"
  status = checkModel(API_KEY)
  demo = classifyText(API_KEY, test_text)
  label = demo["class_name"]
  confidence = demo["confidence"]
  s += ("<b>result:</b> '%s' with %d%% confidence" % (label, confidence))
  return s


API_KEY = os.environ['API_KEY']

app = Flask(__name__)


@app.route("/")
def hello_world():
  text = request.args.get('text')
  form = "<form action='/' method='get'><input type='text' name='text'><input type='submit' value='Classify'></form>"

  if text == None:
    return form
  else:
    return form + "<p> " + process(text) + "</p>"


app.run(host='0.0.0.0')
