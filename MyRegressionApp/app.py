from flask import Flask, render_template, request
from werkzeug.datastructures import MultiDict
app = Flask(__name__)

@app.route('/')
def home():
  values = MultiDict(request.args)
  print(values['alpha'])
  return render_template('index.html', hello=values['alpha'])

if __name__ == '__main__':
  app.run(debug=True)