from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from random import randint
app = Flask("__main__")
app.config.from_pyfile('config.py')
Bootstrap(app)

@app.route('/')
def home():
    # print(type(None))
    chance = randint(0,2)
    if chance == 1:
        flash("Çok şanslıyım", "success")
    elif chance == 0:
        flash("Orta şanslıyım", "warning")
    else:
        flash("Çok şanssızım", "danger")
    return render_template("index.html", title="Ana",
                                         name="Ozan",
                                         my_header="")

if __name__ == '__main__':
    app.run()
