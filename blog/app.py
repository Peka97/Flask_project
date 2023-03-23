from flask import Flask


app = Flask(__name__)


@app.route('/', methods=('GET'))
def index():
    return '<h1>Index Page<h1>'


@app.errorhandler(404)
def handler_404(error):
    return f'<h1>404: Page Not Found<h1><h3>Check your URL<h3>'
