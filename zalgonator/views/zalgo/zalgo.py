from flask import Blueprint, make_response, render_template
from flask.wrappers import Response

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, BooleanField, IntegerField

from zalgonator.zalgo.zalgonate import zalgonate

zalgo = Blueprint('zalgo', __name__)


class TextAreaForm(FlaskForm):
    textarea = TextAreaField('Enter text here:')
    rng_range_low = IntegerField('Minimum number of diacritics per character', default=4)
    rng_range_high = IntegerField('Maximum number of diacritics per character', default=50)
    rng_check = BooleanField('Randomize zalgonation')
    submit = SubmitField('Zalgonate')


@zalgo.route('/', methods=['GET', 'POST'])
def index() -> Response:
    form = TextAreaForm()
    if form.validate_on_submit():
        return render_template(
            'zalgo/index.html',
            form=form,
            zalgotext=zalgonate(
                form.textarea.data,
                form.rng_check.data,
                form.rng_range_low.data,
                form.rng_range_high.data
            )
        )
    return render_template(
        'zalgo/index.html',
        form=form
    )

