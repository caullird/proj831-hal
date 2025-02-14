# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration

class ProfilAuthorForm(FlaskForm):
    author_name = StringField('Prénom',
                         id='author_name',
                         validators=[DataRequired()])

    author_forename = StringField('Nom de famille',
                             id='author_forname',
                             validators=[DataRequired()])


