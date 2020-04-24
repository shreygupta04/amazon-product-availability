from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '668f7da0282f35d4e18c8313'

from amazonbot import routes