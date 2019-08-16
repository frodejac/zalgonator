from typing import Any

from flask import Blueprint, make_response, render_template
from flask.wrappers import Response

from flask_wtf import FlaskForm
from werkzeug.datastructures import ImmutableMultiDict
from wtforms import TextAreaField, SubmitField, BooleanField, IntegerField, Field

from zalgonator.zalgo.zalgonate import zalgonate

zalgo = Blueprint('zalgo', __name__)


class TextAreaForm(FlaskForm):
    textarea = TextAreaField('Enter text here:', render_kw={'rows': 10, 'cols': 60})
    rng_range_low = IntegerField('Min. diacritics/char', default=4, render_kw={'cols':4})
    rng_range_high = IntegerField('Max. diacritics/char', default=50)
    rng_select = BooleanField('Randomize')
    bold_select = BooleanField('Bold')
    submit = SubmitField('Zalgonate')


@zalgo.route('/', methods=['GET', 'POST'])
def index() -> Response:
    def full_field_process(field: Field, val: Any):
        field.process(ImmutableMultiDict([(field.short_name, str(val))]))

    def fix_ranges(form_: TextAreaForm):
        lo = form_.rng_range_low.data
        hi = form_.rng_range_high.data
        if lo > 1000:
            lo = 1000
        if lo < 0:
            lo = 0
        if lo > hi:
            hi = lo
        full_field_process(form_.rng_range_low, lo)
        full_field_process(form_.rng_range_high, hi)

    form = TextAreaForm()
    if form.validate_on_submit():
        fix_ranges(form)
        return render_template(
            'zalgo/index.html',
            form=form,
            zalgotext=zalgonate(
                text=form.textarea.data,
                rng=form.rng_select.data,
                range_low=form.rng_range_low.data,
                range_high=form.rng_range_high.data,
                bold=form.bold_select.data
            )
        )
    return render_template(
        'zalgo/index.html',
        form=form
    )

