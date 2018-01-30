from project import app
from flask import render_template, request, flash, redirect, url_for
from project.forms import SaveForm

@app.route('/')
def index():
    return render_template('index.html.j2', title="Anasayfa")

@app.route('/save')
def save():
    form = SaveForm()
    return render_template('save.html.j2', form=form)

@app.route('/register', methods=['POST'])
def register():
    form = SaveForm(request.form)
    name = form.contributer_name.data
    sentence = form.sentence.data
    print(name)
    print(sentence)
    if len(name) > 3:
        flash(name, "danger")
        if len(sentence) > 3:
            flash(sentence, "warning")

    return redirect(url_for('save'))
