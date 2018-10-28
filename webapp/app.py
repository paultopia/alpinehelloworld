import os, pypandoc

from flask import Flask

app = Flask(__name__)

testmd = '''
# Hello Paul!

You should check out [your own webpage](https://gowder.io)!
'''

@app.route('/')
def hello():
    return pypandoc.convert_text(testmd, 'html', format='md')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
