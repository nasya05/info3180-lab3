from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Please Enter your full name."),
            Length(min=2, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Please enter your email address."),
            Email(message="Enter a valid email address.")
        ]
    )

    subject = StringField(
        "Subject",
        validators=[
            DataRequired(message="Please enter the subject of your message."),
            Length(min=3, max=150)
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Please enter the message you would like to send."),
            Length(min=10)
        ]
    )

    submit = SubmitField("Send Message")