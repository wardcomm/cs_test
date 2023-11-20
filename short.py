# Import necessary libraries
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# In-memory dictionary to store encoded URLs
url_mapping = {}

# General Variables
# domain = localhost

# Rate limiting variables
request_count = 0
last_request_time = 0

# Function to encode a URL
def encode_url(original_url):
    # Using MD5 hash as a simple encoding algorithm
    hash_object = hashlib.md5(original_url.encode())
    encoded_url = hash_object.hexdigest()[:6]
    return f'http://localhost/{encoded_url}'

# Function to decode a URL
def decode_url(encoded_url):
    # Extracting the encoded part from the short URL
    encoded_part = encoded_url.split('/')[-1]
    # Reverse the encoding process (not guaranteed to be unique)
    for original_url, short_code in url_mapping.items():
        if short_code == encoded_part:
            return original_url
    return None

# /encode endpoint to shorten a URL
@app.route('/encode', methods=['GET', 'POST'])
def encode():
    global request_count, last_request_time
    # Rate limiting check
    current_time = time.time()
    if current_time - last_request_time < 0.5:
        return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

    request_count += 1
    last_request_time = current_time

    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    # Check if the URL has already been encoded
    if original_url in url_mapping:
        short_url = url_mapping[original_url]
    else:
        # Encode the URL and store it
        short_url = encode_url(original_url)
        url_mapping[original_url] = short_url

    return jsonify({"short_url": short_url}), 200

# /decode endpoint to retrieve the original URL
@app.route('/decode/<path:encoded_url>', methods=['GET', 'POST'])
def decode(encoded_url):
    original_url = decode_url(encoded_url)
    if original_url:
        return jsonify({"original_url": original_url}), 200
    else:
        return jsonify({"error": "Invalid short URL"}), 404

if __name__ == '__main__':
    app.run(debug=True)
