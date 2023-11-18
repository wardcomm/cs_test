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
