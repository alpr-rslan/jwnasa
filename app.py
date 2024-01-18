from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/photos')
def photos():
    return render_template("photos.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/submit', methods=['POST'])
def submit():
    return render_template("submit.html")

if __name__ == "__main__":
    app.run(debug=True)