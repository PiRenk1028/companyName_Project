import flask
import json
import database_management as dbm


app = flask.Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        data = flask.request.get_json()
        return dbm.get_info(data['fname'],data['lname'])
        
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = False)
