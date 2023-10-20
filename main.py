from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap5

# APP Initialization
app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/download')
def download_cv():
    return send_file(path_or_file='static/Dmytro_Balakin_-_Junior_Python_Developer.pdf', as_attachment=True)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
