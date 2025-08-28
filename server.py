import flask
import json

app = flask.Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        data = flask.request.get_json()
        print(data)
        
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = False)
