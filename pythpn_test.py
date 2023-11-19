from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

#create mapping for in memory object
url_mapping = {}

  # create function encoding using hash library
def encode_url(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]
 
 # create function for encode request module
@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'Missing URL parameter'}), 400

    original_url = data['url']
    short_url = encode_url(original_url)

    # Store in-memory
    url_mapping[short_url] = original_url

    return jsonify({'short_url': short_url}), 200
