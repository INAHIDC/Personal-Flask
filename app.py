from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/relevant_experience')
def relevant_experience():
    return render_template('relevant_experience.html')

if __name__ == '__main__':
    app.run()
