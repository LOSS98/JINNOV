import flask

from flask import*

app = Flask("__name__")

@app.route('/')
def accueil():
    return render_template('header.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)