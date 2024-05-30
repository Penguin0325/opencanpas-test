from flask import flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def hello():
    return render_template('testapp/index.html')

def application(environ, start_response):
    status = '200 OK'

    response_body = app(environ, start_response)

    return response_body