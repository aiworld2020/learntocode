from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/python')
def learn_python():
    return render_template("python.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    return (str(e))


@app.errorhandler(500)
def internal_server_error(e):
    try:
        return render_template("abc.html")
    except Exception as e:
        return render_template("500.html", error = e)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()