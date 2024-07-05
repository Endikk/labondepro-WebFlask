from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/f1')
def f1():
    return render_template('f1.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/projet')
def projet():
    return render_template('projet.html')

@app.route('/global')
def global_page():
    return render_template('global.html')

@app.route('/global/drone')
def global_drone():
    return render_template('drone.html')

if __name__ == '__main__':
    app.run(debug=True)
