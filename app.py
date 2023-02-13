from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap 
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import bmi 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Fatty McFat'
bootstrap = Bootstrap(app)

# Make a form users to input their biometric data:
class BMIForm(FlaskForm):
    weight = FloatField("Enter your weight in kilograms here: ", validators = [DataRequired(), NumberRange(min = 0, max = 700, message = "What are you?")])
    height = FloatField("How tall are you? ", validators = [DataRequired(), NumberRange(), NumberRange(min = 1.0, max = 2.5, message = "You're not a human!")])
    name = StringField("What's your name? ", validators = [DataRequired()]) 
    submit = SubmitField("Guess your Weight!")

@app.route('/', methods = ['GET', 'POST'])
def index():
    name, height, weight, b, msg = None, None, None, None, None
    form = BMIForm()
    if form.validate_on_submit():
        name, height, weight = form.name.data, form.height.data, form.weight.data 
        form.name.data, form.height.data, form.weight.data = '', 0, 0
        b, msg = bmi.calculate_bmi(height, weight)
    return render_template('index.html', form = form, name = name, height = height, weight = weight, status = b, msg = msg), 200

@app.route('/bmi')
def what_is_bmi():
    return render_template('bmi.html'), 200

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404 

@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500