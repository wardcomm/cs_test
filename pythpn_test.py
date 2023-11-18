from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

#create mapping for in memory object
url_mapping = {}
