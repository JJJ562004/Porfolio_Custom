from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/resume')
def resume():
    return render_template('resume.html')
@app.route('/project')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug = True)