from flask import Flask, jsonify

app = Flask(__name__)

#  data
data = {
    'name': 'Chad Ward',
    'age': 51,
    'city': 'Clover'
}

# Route to retrieve the data
@app.route('/api/user', methods=['GET'])
def get_user():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
