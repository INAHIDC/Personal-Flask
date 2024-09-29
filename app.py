from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/PROJECT CYGNUS')
def PROJECT():
    return render_template('CYGNUS.html')


@app.route('/MEALWORM')
def keyl():
    return render_template('KEYLOGGER.html')


if __name__ == '__main__':
    app.run(debug=False, port=6060)
