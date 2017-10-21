"""
   This is used with the wsgi to init the app on production
"""
from cerp import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
