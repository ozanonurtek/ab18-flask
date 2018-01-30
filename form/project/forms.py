from flask_wtf import FlaskForm
from wtforms import StringField

class SaveForm(FlaskForm):
    contributer_name = StringField("contributer_name")
    sentence = StringField("sentence")
