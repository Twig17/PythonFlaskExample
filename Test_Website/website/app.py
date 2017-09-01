from flask import Flask
from website.views.index import bp as index_bp
from website.views.createNote import bp as createNote_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(createNote_bp)


# @app.route('/')
# def home():
#         return "Hello World"