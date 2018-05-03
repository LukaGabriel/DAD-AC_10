from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

from Routes import *

from ErrorHandlers import *

if __name__ == '__main__':
    app.run(port = 80)
