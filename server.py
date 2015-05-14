#!/usr/bin/python
from routes import *

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'), debug=DEBUG)
