import os, pypandoc

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return pypandoc.convert_file("test.md", "html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
