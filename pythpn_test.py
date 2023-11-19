from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

#Create mapping for in memory object
url_mapping = {}

  # Create function encoding using hash library
def encode_url(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]
 
 # Create function for encode request module
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

# Create function for decoding request module
@app.route('/decode/<string:short_url>', methods=['GET'])
def decode(short_url):
    original_url = url_mapping.get(short_url)

    if original_url is None:
        return jsonify({'error': 'Short URL not found'}), 404

    return jsonify({'original_url': original_url}), 200

# Rate limiting decorator
def rate_limit(limit, per):
    def decorator(f):
        def wrapper(*args, **kwargs):
            identifier = request.remote_addr
            current_time = time.time()

            if identifier not in wrapper.access_data:
                wrapper.access_data[identifier] = {'timestamp': current_time, 'count': 1}
            else:
                data = wrapper.access_data[identifier]
                elapsed_time = current_time - data['timestamp']

                if elapsed_time < per:
                    if data['count'] >= limit:
                        return jsonify({'error': 'Rate limit exceeded'}), 429
                    else:
                        data['count'] += 1
                else:
                    data['timestamp'] = current_time
                    data['count'] = 1

            return f(*args, **kwargs)

        wrapper.access_data = {}
        return wrapper

    return decorator