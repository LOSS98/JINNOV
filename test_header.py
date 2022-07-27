import flask

from flask import*

app = Flask("__name__")

@app.route('/')
def accueil():
    return flask.render_template('base.html')

@app.route('/mobile')
def acceuil_mobile():
    return flask.render_template('base_mobile.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)