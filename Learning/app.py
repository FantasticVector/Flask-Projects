from flask import Flask, jsonify

app = Flask(__name__)

stores = [
  {
    'name': 'My Wonderful store',
    'items': [
      {
      'name': 'My Item',
      'price': 15.99
      }
    ]
  }
]

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
  pass

# GET /store/<string:name
@app.route('/store/<string:name>')
def get_store(name):
  pass

# GET /store/
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
  pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
  pass

app.run(port=5000)