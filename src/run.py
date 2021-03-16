from src.app import app

__author__ = 'yuqian'

app.run(debug=app.config['DEBUG'], port=4990)
