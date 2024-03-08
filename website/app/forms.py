from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = StringField("Email address", validators=[DataRequired(), Email()])
    message = TextAreaField(
        "Message", validators=[DataRequired(), Length(min=1, max=512)]
    )
    submit = SubmitField("Send")


class WaitlistForm(FlaskForm):
    email = StringField("name@email.com", validators=[DataRequired(), Email()])
    submit = SubmitField("Join Waitlist")
