import json
import string
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple in-memory storage for URL encoding/decoding
url_mapping = {}

testing code
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

def generate_short_url():
    # Generate a random short URL using uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'Missing URL parameter'}), 400

    original_url = data['url']
    short_url = generate_short_url()

    # Store the mapping in the in-memory storage
    url_mapping[short_url] = original_url

    response_data = {
        'original_url': original_url,
        'short_url': f'http://localhost/{short_url}'  # Replace with your domain
    }

    return jsonify(response_data)

@app.route('/decode/<short_url>', methods=['GET'])
def decode(short_url):
    # Retrieve the original URL from the in-memory storage
    original_url = url_mapping.get(short_url)
# print(original_url)
    if original_url is None:
        return jsonify({'error': 'Short URL not found'}), 404

    response_data = {
        'short_url': f'http://localhost/{short_url}',  # Replace with your domain
        'original_url': original_url
    }

    return jsonify(response_data)
# print(response_data)

# print(short_url)
if __name__ == '__main__':
    app.run(debug=True)
