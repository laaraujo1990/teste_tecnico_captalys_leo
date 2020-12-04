#!//usr/local/bin/python3
#Hello word com Flask

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello word!", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)